from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tomllib
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_CODEX_HOME = Path.home() / ".codex"
DEFAULT_AGENTS_HOME = Path.home() / ".agents"
DEFAULT_PROJECTS_ROOT = Path.home() / "Documents" / "Codex"

MOJIBAKE_MARKERS = ("锟", "鈥", "鈩", "姣", "鍚", "妫", "瀹", "绯", "鎶", "璇")
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".jsonl", ".toml", ".yaml", ".yml", ".py",
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".html", ".css", ".sql",
    ".ps1", ".cmd", ".bat", ".sh", ".ini", ".cfg", ".csv", ".xml",
}
PROJECT_IGNORE_PARTS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build",
    ".next", ".cache",
}

FAILURE_PATTERNS: dict[str, tuple[re.Pattern[str], ...]] = {
    "skill_not_applied": tuple(
        re.compile(p, re.I)
        for p in (
            r"没触发", r"触发不了", r"没有触发", r"没用到.*skill", r"skill.*没.*用",
            r"根本.*没有.*加载", r"没有正确.*吸收", r"一个都没触发",
        )
    ),
    "verification_or_truth_gap": tuple(
        re.compile(p, re.I)
        for p in (
            r"没测试", r"没有测试", r"测过.*没有", r"瞎编", r"胡扯", r"放屁",
            r"骗", r"不相信", r"真假", r"并没有", r"实际.*没",
        )
    ),
    "execution_stopped_early": tuple(
        re.compile(p, re.I)
        for p in (
            r"一步一问", r"走一步", r"只.*其中一个步骤", r"不执行", r"没有执行",
            r"只说.*废话", r"你执行了吗", r"上传了吗", r"做完.*一件事",
        )
    ),
    "reporting_missed_outcome": tuple(
        re.compile(p, re.I)
        for p in (
            r"汇报.*废话", r"要求到底怎么样", r"我知道这些有个屁用", r"核心没说清楚",
            r"看不懂.*方案", r"说清楚", r"全.*废话",
        )
    ),
    "design_quality_failure": tuple(
        re.compile(p, re.I)
        for p in (
            r"丑", r"设计.*垃圾", r"垃圾.*设计", r"毫无规范", r"结构.*不合理",
            r"审美", r"卡片堆", r"没有.*设计规范", r"学生.*水平",
        )
    ),
    "scope_boundary_failure": tuple(
        re.compile(p, re.I)
        for p in (
            r"应用边界", r"怎么能是全局经验", r"公司项目", r"乱写", r"绑死",
            r"项目.*根本不重要", r"不符合.*项目",
        )
    ),
    "browser_or_computer_capability_failure": tuple(
        re.compile(p, re.I)
        for p in (
            r"登录态", r"computer\s*use", r"无法读取", r"不能读取", r"控制我电脑",
            r"Chrome.*不通", r"文章.*读", r"浏览器.*问题",
        )
    ),
    "automation_or_update_failure": tuple(
        re.compile(p, re.I)
        for p in (
            r"自动.*没.*执行", r"周一.*没更新", r"多久更新", r"检测.*更新",
            r"为什么没执行", r"每周.*检查", r"版本.*没.*汇报",
        )
    ),
    "memory_or_export_failure": tuple(
        re.compile(p, re.I)
        for p in (
            r"备份.*用不了", r"导出", r"所有记忆", r"记忆系统", r"知识库",
            r"重新调教", r"github.*备份", r"存储下来",
        )
    ),
}


@dataclass
class SkillRecord:
    name: str
    description: str
    path: str
    root_kind: str
    lines: int
    content_hash: str
    mojibake_hits: int
    has_openai_yaml: bool
    valid_frontmatter: bool
    active_surface: bool


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def short_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:16]


def iter_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in PROJECT_IGNORE_PARTS]
        base = Path(dirpath)
        for filename in filenames:
            yield base / filename


def frontmatter(text: str) -> tuple[dict[str, str], bool]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, False
    values: dict[str, str] = {}
    closed = False
    for line in lines[1:]:
        if line.strip() == "---":
            closed = True
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("'\"")
    return values, closed and "name" in values and "description" in values and bool(values.get("name"))


def active_plugin_version_roots(cache_root: Path) -> set[Path]:
    active: set[Path] = set()
    for group_name in ("openai-bundled", "openai-curated-remote", "openai-primary-runtime", "personal"):
        group = cache_root / group_name
        if not group.exists():
            continue
        for plugin in (path for path in group.iterdir() if path.is_dir()):
            versions = [path for path in plugin.iterdir() if path.is_dir() and path.name.casefold() != "latest"]
            if not versions:
                versions = [path for path in plugin.iterdir() if path.is_dir()]
            if versions:
                active.add(max(versions, key=lambda path: path.stat().st_mtime))
    return active


def discover_skills(codex_home: Path, agents_home: Path) -> tuple[list[SkillRecord], dict[str, Any]]:
    plugin_cache = codex_home / "plugins" / "cache"
    active_plugin_roots = active_plugin_version_roots(plugin_cache)
    roots: list[tuple[str, Path]] = [
        ("codex-local", codex_home / "skills"),
        ("agents-shared", agents_home / "skills"),
        ("plugin-cache", plugin_cache),
    ]
    records: list[SkillRecord] = []
    read_errors: list[str] = []
    for root_kind, root in roots:
        if not root.exists():
            continue
        for path in root.rglob("SKILL.md"):
            try:
                data = path.read_bytes()
                text = data.decode("utf-8", errors="replace")
            except OSError:
                read_errors.append(str(path))
                continue
            meta, valid = frontmatter(text)
            active_surface = root_kind != "plugin-cache" or any(
                version_root == path or version_root in path.parents for version_root in active_plugin_roots
            )
            records.append(
                SkillRecord(
                    name=meta.get("name") or path.parent.name,
                    description=meta.get("description", ""),
                    path=str(path),
                    root_kind=root_kind,
                    lines=text.count("\n") + 1,
                    content_hash=sha256_bytes(data),
                    mojibake_hits=sum(text.count(marker) for marker in MOJIBAKE_MARKERS),
                    has_openai_yaml=(path.parent / "agents" / "openai.yaml").exists(),
                    valid_frontmatter=valid,
                    active_surface=active_surface,
                )
            )

    by_name: dict[str, list[SkillRecord]] = defaultdict(list)
    by_hash: dict[str, list[SkillRecord]] = defaultdict(list)
    active_records = [record for record in records if record.active_surface]
    for record in active_records:
        by_name[record.name.casefold()].append(record)
        by_hash[record.content_hash].append(record)

    conflicts = []
    exact_duplicates = []
    plugin_scoped_duplicates = []
    for name, rows in sorted(by_name.items()):
        if len(rows) < 2:
            continue
        item = {
            "name": name,
            "paths": [row.path for row in rows],
            "root_kinds": sorted({row.root_kind for row in rows}),
            "hashes": sorted({row.content_hash for row in rows}),
        }
        plugin_namespaces = set()
        for row in rows:
            if row.root_kind != "plugin-cache":
                continue
            try:
                relative = Path(row.path).relative_to(plugin_cache)
            except ValueError:
                continue
            if len(relative.parts) >= 2:
                plugin_namespaces.add("/".join(relative.parts[:2]))
        item["plugin_namespaces"] = sorted(plugin_namespaces)
        if len(item["hashes"]) == 1:
            exact_duplicates.append(item)
        elif len(plugin_namespaces) == len(rows):
            plugin_scoped_duplicates.append(item)
        else:
            conflicts.append(item)

    summary = {
        "skill_files": len(records),
        "active_skill_files": len(active_records),
        "stale_cache_skill_files": len(records) - len(active_records),
        "unique_names": len(by_name),
        "invalid_frontmatter": [row.path for row in active_records if not row.valid_frontmatter],
        "over_500_lines": [row.path for row in active_records if row.lines > 500],
        "mojibake_suspects": [row.path for row in active_records if row.mojibake_hits >= 3],
        "missing_openai_yaml": [
            row.path
            for row in active_records
            if row.root_kind == "codex-local" and not row.has_openai_yaml
        ],
        "owner_managed_without_openai_yaml": {
            root_kind: len(
                [
                    row
                    for row in active_records
                    if row.root_kind == root_kind and not row.has_openai_yaml
                ]
            )
            for root_kind in ("agents-shared", "plugin-cache")
        },
        "exact_duplicate_names": exact_duplicates,
        "plugin_scoped_duplicate_names": plugin_scoped_duplicates,
        "conflicting_duplicate_names": conflicts,
        "read_errors": read_errors,
    }
    return records, summary


def extract_message_text(payload: dict[str, Any]) -> str:
    content = payload.get("content")
    if isinstance(content, str):
        return content
    texts: list[str] = []
    if isinstance(content, list):
        for item in content:
            if isinstance(item, str):
                texts.append(item)
            elif isinstance(item, dict):
                value = item.get("text") or item.get("input_text") or item.get("output_text")
                if isinstance(value, str):
                    texts.append(value)
    return "\n".join(texts)


def scan_sessions(sessions_root: Path, skill_records: list[SkillRecord]) -> dict[str, Any]:
    files = sorted(sessions_root.rglob("*.jsonl")) if sessions_root.exists() else []
    failure_counts: Counter[str] = Counter()
    failure_sessions: dict[str, set[str]] = defaultdict(set)
    skill_reads: Counter[str] = Counter()
    skill_read_sessions: dict[str, set[str]] = defaultdict(set)
    user_messages = 0
    assistant_messages = 0
    tool_calls = 0
    parse_errors = 0
    records = 0
    bytes_scanned = 0
    session_rows: list[dict[str, Any]] = []
    folder_to_names: dict[str, set[str]] = defaultdict(set)
    for record in skill_records:
        folder_to_names[Path(record.path).parent.name.casefold()].add(record.name)
    latest_model_timestamp = ""
    latest_model: str | None = None

    for path in files:
        session_id = path.stem.rsplit("-", 1)[-1]
        session_cwd: str | None = None
        session_model: str | None = None
        session_user_messages = 0
        session_assistant_messages = 0
        session_records = 0
        try:
            fh = path.open("rb")
        except OSError:
            continue
        with fh:
            for raw in fh:
                bytes_scanned += len(raw)
                records += 1
                session_records += 1

                is_tool_call = b'"type":"function_call"' in raw or b'"type":"custom_tool_call"' in raw
                if is_tool_call:
                    tool_calls += 1
                    if b"SKILL.md" in raw:
                        try:
                            tool_row = json.loads(raw)
                        except (json.JSONDecodeError, UnicodeDecodeError):
                            parse_errors += 1
                            tool_row = {}
                        tool_payload = tool_row.get("payload") or {}
                        tool_input = tool_payload.get("input") or tool_payload.get("arguments") or ""
                        if not isinstance(tool_input, str):
                            tool_input = json.dumps(tool_input, ensure_ascii=False)
                        read_intent = re.search(
                            r"Get-Content|\bcat\s|\bsed\s+-n|skills\.read|read_mcp_resource",
                            tool_input,
                            re.I,
                        )
                        if read_intent:
                            matched_names: set[str] = set()
                            for folder in re.findall(
                                r"([A-Za-z0-9][A-Za-z0-9._:-]{0,100})[\\/]+SKILL\.md", tool_input, re.I
                            ):
                                matched_names.update(folder_to_names.get(folder.casefold(), set()))
                            if matched_names:
                                for skill_name in matched_names:
                                    skill_reads[skill_name] += 1
                                    skill_read_sessions[skill_name].add(session_id)
                            else:
                                skill_reads["<unmapped-skill-path>"] += 1
                                skill_read_sessions["<unmapped-skill-path>"].add(session_id)

                if b'"role":"assistant"' in raw and b'"type":"message"' in raw:
                    assistant_messages += 1
                    session_assistant_messages += 1

                interesting = (
                    b'"type":"session_meta"' in raw
                    or b'"type":"turn_context"' in raw
                    or (b'"role":"user"' in raw and b'"type":"message"' in raw)
                )
                if not interesting:
                    continue
                try:
                    row = json.loads(raw)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    parse_errors += 1
                    continue
                payload = row.get("payload") or {}
                row_type = row.get("type")
                payload_type = payload.get("type")
                if row_type == "session_meta":
                    session_id = str(payload.get("id") or session_id)
                    session_cwd = payload.get("cwd") or session_cwd
                if row_type == "turn_context":
                    session_cwd = payload.get("cwd") or session_cwd
                    session_model = payload.get("model") or session_model
                    timestamp = str(row.get("timestamp") or "")
                    if session_model and timestamp >= latest_model_timestamp:
                        latest_model_timestamp = timestamp
                        latest_model = str(session_model)
                role = payload.get("role")
                if payload_type == "message" and role == "user":
                    text = extract_message_text(payload)
                    user_messages += 1
                    session_user_messages += 1
                    for category, patterns in FAILURE_PATTERNS.items():
                        if any(pattern.search(text) for pattern in patterns):
                            failure_counts[category] += 1
                            failure_sessions[category].add(session_id)
        session_rows.append(
            {
                "session_id": session_id,
                "path": str(path),
                "bytes": path.stat().st_size,
                "records": session_records,
                "cwd": session_cwd,
                "model": session_model,
                "user_messages": session_user_messages,
                "assistant_messages": session_assistant_messages,
            }
        )

    return {
        "session_files": len(files),
        "bytes_scanned": bytes_scanned,
        "records_scanned": records,
        "parse_errors": parse_errors,
        "user_messages": user_messages,
        "assistant_messages": assistant_messages,
        "tool_calls": tool_calls,
        "latest_model": latest_model,
        "latest_model_timestamp": latest_model_timestamp,
        "failure_categories": {
            category: {
                "message_count": failure_counts[category],
                "session_count": len(failure_sessions[category]),
                "session_ids": sorted(failure_sessions[category]),
            }
            for category in FAILURE_PATTERNS
        },
        "skill_reads": [
            {
                "skill": name,
                "read_events": count,
                "session_count": len(skill_read_sessions[name]),
            }
            for name, count in skill_reads.most_common()
        ],
        "sessions": session_rows,
    }


def project_roots(projects_root: Path) -> list[Path]:
    roots: list[Path] = []
    if not projects_root.exists():
        return roots
    for group in sorted(p for p in projects_root.iterdir() if p.is_dir()):
        children = sorted(p for p in group.iterdir() if p.is_dir())
        if group.name == "exports":
            roots.extend(children)
        else:
            roots.extend(children or [group])
    return roots


def scan_projects(projects_root: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    total_files = 0
    total_bytes = 0
    for root in project_roots(projects_root):
        count = 0
        size = 0
        generated_or_dependency_files = 0
        extensions: Counter[str] = Counter()
        instruction_files: list[str] = []
        top_level_files: list[str] = []
        read_errors = 0
        for dirpath, _dirnames, filenames in os.walk(root):
            base = Path(dirpath)
            relative_parts = {part.casefold() for part in base.relative_to(root).parts}
            generated_dir = bool(relative_parts & {part.casefold() for part in PROJECT_IGNORE_PARTS})
            for filename in filenames:
                path = base / filename
                try:
                    stat = path.stat()
                except OSError:
                    read_errors += 1
                    continue
                count += 1
                size += stat.st_size
                extensions[path.suffix.lower() or "<none>"] += 1
                if generated_dir:
                    generated_or_dependency_files += 1
                if not generated_dir and path.name.casefold() in {
                    "agents.md", "claude.md", "readme.md", "readme.zh.md", "readme.zh-cn.md"
                }:
                    instruction_files.append(str(path))
                if path.parent == root and len(top_level_files) < 80:
                    top_level_files.append(path.name)
        total_files += count
        total_bytes += size
        rows.append(
            {
                "path": str(root),
                "files": count,
                "bytes": size,
                "git_repo": (root / ".git").exists(),
                "generated_or_dependency_files": generated_or_dependency_files,
                "instruction_files": instruction_files,
                "top_level_files": sorted(top_level_files),
                "top_extensions": extensions.most_common(12),
                "read_errors": read_errors,
            }
        )
    return {
        "projects_root": str(projects_root),
        "project_roots": len(rows),
        "files_scanned": total_files,
        "bytes_scanned": total_bytes,
        "projects": rows,
    }


def scan_memories(memories_root: Path) -> dict[str, Any]:
    files = sorted(path for path in iter_files(memories_root)) if memories_root.exists() else []
    by_hash: dict[str, list[str]] = defaultdict(list)
    mojibake: list[dict[str, Any]] = []
    frontmatter_missing_scope: list[str] = []
    read_errors: list[str] = []
    total_bytes = 0
    for path in files:
        try:
            data = path.read_bytes()
        except OSError:
            read_errors.append(str(path))
            continue
        total_bytes += len(data)
        by_hash[sha256_bytes(data)].append(str(path))
        if path.suffix.lower() in TEXT_SUFFIXES:
            text = data.decode("utf-8", errors="replace")
            hits = sum(text.count(marker) for marker in MOJIBAKE_MARKERS)
            if hits >= 3:
                mojibake.append({"path": str(path), "marker_hits": hits})
            meta, _valid = frontmatter(text)
            if meta and path.name not in {"MEMORY.md", "memory_summary.md"}:
                has_scope = bool(meta.get("scope") or meta.get("applies_to") or meta.get("page_type"))
                if not has_scope:
                    frontmatter_missing_scope.append(str(path))
    duplicates = [paths for paths in by_hash.values() if len(paths) > 1]
    mirror_duplicates = [
        paths
        for paths in duplicates
        if any("evolution-kit-private" in Path(path).parts for path in paths)
    ]
    unexplained_duplicates = [paths for paths in duplicates if paths not in mirror_duplicates]
    return {
        "memory_files": len(files),
        "bytes_scanned": total_bytes,
        "exact_duplicate_groups": duplicates,
        "exact_duplicate_files": sum(len(group) for group in duplicates),
        "mirror_duplicate_groups": mirror_duplicates,
        "unexplained_duplicate_groups": unexplained_duplicates,
        "mojibake_suspects": mojibake,
        "frontmatter_missing_scope": frontmatter_missing_scope,
        "read_errors": read_errors,
    }


def scan_automations(codex_home: Path, current_model: str | None) -> dict[str, Any]:
    root = codex_home / "automations"
    rows: list[dict[str, Any]] = []
    for path in sorted(root.glob("*/automation.toml")) if root.exists() else []:
        raw = path.read_bytes()
        try:
            data = tomllib.loads(raw.decode("utf-8"))
            parse_error = None
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as exc:
            data = {}
            parse_error = str(exc)
        text = raw.decode("utf-8", errors="replace")
        rows.append(
            {
                "path": str(path),
                "id": data.get("id"),
                "name": data.get("name"),
                "kind": data.get("kind"),
                "status": data.get("status"),
                "rrule": data.get("rrule"),
                "model": data.get("model"),
                "model_stale": bool(current_model and data.get("model") and data.get("model") != current_model),
                "mojibake_hits": sum(text.count(marker) for marker in MOJIBAKE_MARKERS),
                "parse_error": parse_error,
            }
        )
    return {"current_model": current_model, "automations": rows}


def detect_current_model(session_report: dict[str, Any]) -> str | None:
    model = session_report.get("latest_model")
    return str(model) if model else None


def markdown_report(report: dict[str, Any]) -> str:
    sessions = report["sessions"]
    skills = report["skills"]
    projects = report["projects"]
    memories = report["memories"]
    automations = report["automations"]
    lines = [
        "# Codex System Audit",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "This report stores aggregate evidence only. It does not copy chat bodies, secrets, or project contents.",
        "",
        "## Coverage",
        "",
        f"- Sessions: {sessions['session_files']} files, {sessions['bytes_scanned']} bytes, {sessions['records_scanned']} records",
        f"- Projects: {projects['project_roots']} roots, {projects['files_scanned']} files, {projects['bytes_scanned']} bytes",
        f"- Memories: {memories['memory_files']} files, {memories['bytes_scanned']} bytes",
        f"- Skills: {skills['skill_files']} SKILL.md files on disk; {skills['active_skill_files']} active-surface files; {skills['unique_names']} active unique names",
        "",
        "## Historical Failure Signals",
        "",
        "| Category | User messages | Sessions |",
        "|---|---:|---:|",
    ]
    for category, item in sessions["failure_categories"].items():
        lines.append(f"| `{category}` | {item['message_count']} | {item['session_count']} |")
    lines += [
        "",
        "## Skill Integrity",
        "",
        f"- Exact duplicate names: {len(skills['exact_duplicate_names'])}",
        f"- Plugin-scoped duplicate names: {len(skills['plugin_scoped_duplicate_names'])}",
        f"- Conflicting duplicate names: {len(skills['conflicting_duplicate_names'])}",
        f"- Invalid frontmatter: {len(skills['invalid_frontmatter'])}",
        f"- Skills over 500 lines: {len(skills['over_500_lines'])}",
        f"- Mojibake suspects: {len(skills['mojibake_suspects'])}",
        "",
        "## Memory Integrity",
        "",
        f"- Exact duplicate groups: {len(memories['exact_duplicate_groups'])}",
        f"- Files in duplicate groups: {memories['exact_duplicate_files']}",
        f"- Expected private-mirror duplicate groups: {len(memories['mirror_duplicate_groups'])}",
        f"- Unexplained duplicate groups: {len(memories['unexplained_duplicate_groups'])}",
        f"- Mojibake suspects: {len(memories['mojibake_suspects'])}",
        f"- Scoped frontmatter gaps: {len(memories['frontmatter_missing_scope'])}",
        "",
        "## Automation Integrity",
        "",
        f"- Current observed model: `{automations.get('current_model')}`",
        "",
        "| Automation | Kind | Model | Stale | Mojibake hits |",
        "|---|---|---|---:|---:|",
    ]
    for item in automations["automations"]:
        lines.append(
            f"| `{item.get('id')}` | `{item.get('kind')}` | `{item.get('model')}` | "
            f"{str(item.get('model_stale')).lower()} | {item.get('mojibake_hits')} |"
        )
    lines += [
        "",
        "## Strong Skill Usage Evidence",
        "",
        "| Skill | SKILL.md read events | Sessions |",
        "|---|---:|---:|",
    ]
    for item in sessions["skill_reads"][:40]:
        lines.append(f"| `{item['skill']}` | {item['read_events']} | {item['session_count']} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Codex memories, sessions, projects, skills, and automations.")
    parser.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    parser.add_argument("--agents-home", type=Path, default=DEFAULT_AGENTS_HOME)
    parser.add_argument("--projects-root", type=Path, default=DEFAULT_PROJECTS_ROOT)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--md-out", type=Path)
    args = parser.parse_args()

    skill_records, skill_summary = discover_skills(args.codex_home, args.agents_home)
    sessions = scan_sessions(args.codex_home / "sessions", skill_records)
    current_model = detect_current_model(sessions)
    report = {
        "generated_at": utc_now(),
        "skills": skill_summary,
        "sessions": sessions,
        "projects": scan_projects(args.projects_root),
        "memories": scan_memories(args.codex_home / "memories"),
        "automations": scan_automations(args.codex_home, current_model),
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(markdown_report(report), encoding="utf-8")

    print(
        json.dumps(
            {
                "generated_at": report["generated_at"],
                "sessions": {key: sessions[key] for key in ("session_files", "bytes_scanned", "records_scanned", "parse_errors")},
                "projects": {key: report["projects"][key] for key in ("project_roots", "files_scanned", "bytes_scanned")},
                "memories": {
                    "memory_files": report["memories"]["memory_files"],
                    "exact_duplicate_groups": len(report["memories"]["exact_duplicate_groups"]),
                    "mirror_duplicate_groups": len(report["memories"]["mirror_duplicate_groups"]),
                    "unexplained_duplicate_groups": len(report["memories"]["unexplained_duplicate_groups"]),
                    "mojibake_suspects": len(report["memories"]["mojibake_suspects"]),
                },
                "skills": {
                    "skill_files": skill_summary["skill_files"],
                    "active_skill_files": skill_summary["active_skill_files"],
                    "stale_cache_skill_files": skill_summary["stale_cache_skill_files"],
                    "unique_names": skill_summary["unique_names"],
                    "exact_duplicate_names": len(skill_summary["exact_duplicate_names"]),
                    "plugin_scoped_duplicate_names": len(skill_summary["plugin_scoped_duplicate_names"]),
                    "conflicting_duplicate_names": len(skill_summary["conflicting_duplicate_names"]),
                },
                "current_model": current_model,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
