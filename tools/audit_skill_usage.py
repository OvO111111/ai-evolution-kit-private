from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CODEX_HOME = Path.home() / ".codex"
DEFAULT_AGENTS_HOME = Path.home() / ".agents"
DEFAULT_EXPORT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Skill:
    folder: str
    name: str
    path: Path
    root: Path
    tier: str = "unknown"


def parse_frontmatter_name(path: Path) -> str:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[:20]
    except OSError:
        return path.parent.name
    for line in lines:
        match = re.match(r"\s*name:\s*(.+?)\s*$", line)
        if match:
            return match.group(1).strip().strip('"').strip("'")
    return path.parent.name


def load_portfolio_tiers(export_root: Path) -> dict[str, str]:
    tiers: dict[str, str] = {}
    path = export_root / "memories" / "vault_summaries" / "skill-portfolio.jsonl"
    if not path.exists():
        return tiers
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        tier = row.get("tier")
        if not tier:
            continue
        for key in (row.get("name"), row.get("folder")):
            if key:
                tiers[str(key).lower()] = str(tier)
    return tiers


def discover_skills(roots: list[Path], tiers: dict[str, str]) -> list[Skill]:
    seen: set[Path] = set()
    discovered: list[Skill] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("SKILL.md"):
            if path in seen:
                continue
            seen.add(path)
            folder = path.parent.name
            name = parse_frontmatter_name(path)
            tier = tiers.get(name.lower()) or tiers.get(folder.lower()) or "unknown"
            discovered.append(Skill(folder=folder, name=name, path=path, root=root, tier=tier))

    # Some skills are mirrored in both .codex and .agents. Count one logical skill,
    # preferring the .codex copy when present because it is the Codex-global source.
    by_name: dict[str, Skill] = {}
    for skill in discovered:
        key = skill.name.lower()
        current = by_name.get(key)
        if current is None:
            by_name[key] = skill
            continue
        current_is_codex = "\\.codex\\" in str(current.path).lower()
        candidate_is_codex = "\\.codex\\" in str(skill.path).lower()
        if candidate_is_codex and not current_is_codex:
            by_name[key] = skill

    return sorted(by_name.values(), key=lambda s: (s.tier, s.name.lower(), str(s.path).lower()))


def iter_texts(value: Any) -> list[str]:
    out: list[str] = []
    if value is None:
        return out
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        for item in value.values():
            out.extend(iter_texts(item))
    elif isinstance(value, list):
        for item in value:
            out.extend(iter_texts(item))
    return out


def payload_text(payload: dict[str, Any]) -> str:
    return "\n".join(iter_texts(payload))


def find_current_audit_cutoff(session_files: list[Path]) -> str | None:
    markers = [
        "你检索下全局，查查各种skill被调用次数",
        "全局审计：从本机 Codex session/rollout 记录里统计",
    ]
    cutoff: str | None = None
    for path in session_files:
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for line in lines:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            text = payload_text(row.get("payload") or {})
            if any(marker in text for marker in markers):
                ts = row.get("timestamp")
                if isinstance(ts, str) and (cutoff is None or ts < cutoff):
                    cutoff = ts
    return cutoff


def compile_alias_regexes(skill: Skill) -> list[re.Pattern[str]]:
    aliases = {skill.name, skill.folder}
    patterns: list[re.Pattern[str]] = []
    for alias in aliases:
        escaped = re.escape(alias)
        patterns.append(re.compile(rf"(?<![A-Za-z0-9_-]){escaped}(?![A-Za-z0-9_-])", re.IGNORECASE))
    return patterns


def path_regex(skill: Skill) -> re.Pattern[str]:
    folder = re.escape(skill.folder)
    name = re.escape(skill.name)
    return re.compile(
        rf"(?:[\\/](?:{folder}|{name})[\\/]SKILL\.md|(?:{folder}|{name})[\\/]SKILL\.md)",
        re.IGNORECASE,
    )


def audit(sessions_root: Path, skills: list[Skill], cutoff: str | None) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    session_files = sorted(sessions_root.rglob("*.jsonl")) if sessions_root.exists() else []
    alias_res = {skill.name: compile_alias_regexes(skill) for skill in skills}
    path_res = {skill.name: path_regex(skill) for skill in skills}

    counts: dict[str, dict[str, int]] = {
        skill.name: {
            "skill_file_reads": 0,
            "assistant_mentions": 0,
            "user_mentions": 0,
            "tool_arg_mentions": 0,
            "evidence_events": 0,
        }
        for skill in skills
    }
    evidence: dict[str, list[str]] = defaultdict(list)

    records = 0
    scanned_files = 0
    for file in session_files:
        scanned_files += 1
        try:
            fh = file.open("r", encoding="utf-8", errors="replace")
        except OSError:
            continue
        with fh:
            for line_no, line in enumerate(fh, 1):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ts = row.get("timestamp")
                if cutoff and isinstance(ts, str) and ts >= cutoff:
                    continue
                if row.get("type") == "session_meta":
                    continue
                payload = row.get("payload") or {}
                payload_type = payload.get("type")
                role = payload.get("role")
                text = payload_text(payload)
                if not text:
                    continue
                records += 1

                bucket: str | None = None
                if payload_type == "message" and role == "assistant":
                    bucket = "assistant_mentions"
                elif payload_type == "message" and role == "user":
                    bucket = "user_mentions"
                elif payload_type in {"function_call", "custom_tool_call"}:
                    bucket = "tool_arg_mentions"

                for skill in skills:
                    matched = False
                    if bucket == "tool_arg_mentions" and path_res[skill.name].search(text):
                        counts[skill.name]["skill_file_reads"] += 1
                        matched = True
                    if bucket and any(regex.search(text) for regex in alias_res[skill.name]):
                        counts[skill.name][bucket] += 1
                        matched = True
                    if matched:
                        counts[skill.name]["evidence_events"] += 1
                        if len(evidence[skill.name]) < 3:
                            rel = str(file)
                            evidence[skill.name].append(f"{rel}:{line_no}:{bucket or 'match'}")

    rows: list[dict[str, Any]] = []
    for skill in skills:
        c = counts[skill.name]
        rows.append(
            {
                "name": skill.name,
                "folder": skill.folder,
                "tier": skill.tier,
                "skill_file_reads": c["skill_file_reads"],
                "assistant_mentions": c["assistant_mentions"],
                "user_mentions": c["user_mentions"],
                "tool_arg_mentions": c["tool_arg_mentions"],
                "evidence_events": c["evidence_events"],
                "path": str(skill.path),
                "evidence": evidence.get(skill.name, []),
            }
        )

    meta = {
        "sessions_root": str(sessions_root),
        "session_files": scanned_files,
        "records_scanned": records,
        "cutoff": cutoff,
        "skill_count": len(skills),
    }
    return rows, meta


def write_reports(rows: list[dict[str, Any]], meta: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "skill-usage-audit-2026-05-28.json"
    md_path = out_dir / "skill-usage-audit-2026-05-28.md"
    json_path.write_text(json.dumps({"meta": meta, "rows": rows}, ensure_ascii=False, indent=2), encoding="utf-8")

    active = [r for r in rows if r["tier"] == "active"]
    zero_active = [r for r in active if r["skill_file_reads"] == 0 and r["assistant_mentions"] == 0]
    zero_all = [r for r in rows if r["skill_file_reads"] == 0 and r["assistant_mentions"] == 0 and r["user_mentions"] == 0]
    top = sorted(rows, key=lambda r: (r["skill_file_reads"], r["assistant_mentions"], r["tool_arg_mentions"]), reverse=True)[:20]

    lines: list[str] = []
    lines.append("---")
    lines.append('page_type: audit')
    lines.append('created_at: "2026-05-28"')
    lines.append('status: active')
    lines.append("---")
    lines.append("")
    lines.append("# Skill Usage Audit 2026-05-28")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(f"- Sessions root: `{meta['sessions_root']}`")
    lines.append(f"- Session files scanned: {meta['session_files']}")
    lines.append(f"- Records scanned: {meta['records_scanned']}")
    lines.append(f"- Skills discovered: {meta['skill_count']}")
    lines.append(f"- Cutoff: `{meta['cutoff']}`")
    lines.append("")
    lines.append("Counting rule: `skill_file_reads` is strongest evidence because it means a historical turn opened or referenced a concrete `SKILL.md` path in tool arguments. Assistant/user mentions are secondary evidence and can include discussion rather than execution.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Active skills: {len(active)}")
    lines.append(f"- Active skills with zero strong/assistant evidence: {len(zero_active)}")
    lines.append(f"- All skills with zero evidence: {len(zero_all)}")
    lines.append("")
    lines.append("## Top Evidence")
    lines.append("")
    lines.append("| Skill | Tier | SKILL.md reads | Assistant mentions | Tool arg mentions |")
    lines.append("|---|---:|---:|---:|---:|")
    for r in top:
        lines.append(f"| `{r['name']}` | {r['tier']} | {r['skill_file_reads']} | {r['assistant_mentions']} | {r['tool_arg_mentions']} |")
    lines.append("")
    lines.append("## Active Skills With Zero Strong/Assistant Evidence")
    lines.append("")
    if zero_active:
        for r in sorted(zero_active, key=lambda x: x["name"].lower()):
            lines.append(f"- `{r['name']}` (`{r['folder']}`): user_mentions={r['user_mentions']}, path=`{r['path']}`")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## All Skill Rows")
    lines.append("")
    lines.append("| Skill | Folder | Tier | SKILL.md reads | Assistant | User | Tool args |")
    lines.append("|---|---|---:|---:|---:|---:|---:|")
    for r in sorted(rows, key=lambda x: (x["tier"], x["name"].lower())):
        lines.append(
            f"| `{r['name']}` | `{r['folder']}` | {r['tier']} | {r['skill_file_reads']} | {r['assistant_mentions']} | {r['user_mentions']} | {r['tool_arg_mentions']} |"
        )
    lines.append("")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    parser.add_argument("--agents-home", type=Path, default=DEFAULT_AGENTS_HOME)
    parser.add_argument("--export-root", type=Path, default=DEFAULT_EXPORT_ROOT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_EXPORT_ROOT / "memories" / "vault_summaries")
    args = parser.parse_args()

    tiers = load_portfolio_tiers(args.export_root)
    roots = [
        args.codex_home / "skills",
        args.agents_home / "skills",
    ]
    skills = discover_skills(roots, tiers)
    session_files = sorted((args.codex_home / "sessions").rglob("*.jsonl"))
    cutoff = find_current_audit_cutoff(session_files)
    rows, meta = audit(args.codex_home / "sessions", skills, cutoff)
    write_reports(rows, meta, args.out_dir)
    print(json.dumps({"meta": meta, "active_zero": sum(1 for r in rows if r["tier"] == "active" and r["skill_file_reads"] == 0 and r["assistant_mentions"] == 0)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
