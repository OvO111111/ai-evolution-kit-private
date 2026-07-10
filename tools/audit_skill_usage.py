from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_CODEX_HOME = Path.home() / ".codex"
DEFAULT_AGENTS_HOME = Path.home() / ".agents"
DEFAULT_EXPORT_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH_RE = re.compile(r"(?i)([A-Za-z0-9_.:-]+)[\\/]SKILL\.md")


@dataclass(frozen=True)
class Skill:
    folder: str
    name: str
    path: Path
    root_label: str
    root: Path
    tier: str = "unknown"

    @property
    def portable_path(self) -> str:
        try:
            relative = self.path.relative_to(self.root).as_posix()
        except ValueError:
            relative = self.path.name
        return f"{self.root_label}/{relative}"

    @property
    def has_openai_yaml(self) -> bool:
        return (self.path.parent / "agents" / "openai.yaml").exists()


def iter_texts(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_texts(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_texts(item)


def payload_text(payload: dict[str, Any]) -> str:
    return "\n".join(iter_texts(payload))


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
        name = row.get("name")
        folder = row.get("folder")
        if name:
            tiers[str(name).casefold()] = str(tier)
        # A reference copy can share a folder name with the maintained adapter.
        # Only let folder aliases set a tier when they describe the same name.
        if folder and (not name or str(folder).casefold() == str(name).casefold()):
            tiers[str(folder).casefold()] = str(tier)
    return tiers


def discover_skills(
    roots: list[tuple[str, Path]], tiers: dict[str, str]
) -> list[Skill]:
    discovered: list[Skill] = []
    for root_label, root in roots:
        if not root.exists():
            continue
        for path in root.rglob("SKILL.md"):
            folder = path.parent.name
            name = parse_frontmatter_name(path)
            tier = tiers.get(name.casefold()) or tiers.get(folder.casefold()) or "unknown"
            discovered.append(
                Skill(
                    folder=folder,
                    name=name,
                    path=path,
                    root_label=root_label,
                    root=root,
                    tier=tier,
                )
            )

    # Prefer the Codex-global copy when the same logical name exists in both roots.
    by_name: dict[str, Skill] = {}
    for skill in discovered:
        key = skill.name.casefold()
        current = by_name.get(key)
        if current is None or (skill.root_label == "codex" and current.root_label != "codex"):
            by_name[key] = skill
    return sorted(by_name.values(), key=lambda item: (item.tier, item.name.casefold()))


def build_alias_index(
    skills: list[Skill],
) -> tuple[re.Pattern[str], dict[str, set[str]], dict[str, set[str]]]:
    alias_to_names: dict[str, set[str]] = defaultdict(set)
    folder_to_names: dict[str, set[str]] = defaultdict(set)
    for skill in skills:
        for alias in {skill.name, skill.folder}:
            alias_to_names[alias.casefold()].add(skill.name)
        folder_to_names[skill.folder.casefold()].add(skill.name)
        folder_to_names[skill.name.casefold()].add(skill.name)

    aliases = sorted(alias_to_names, key=len, reverse=True)
    if not aliases:
        return re.compile(r"(?!x)x"), alias_to_names, folder_to_names
    body = "|".join(re.escape(alias) for alias in aliases)
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_-])(?:{body})(?![A-Za-z0-9_-])", re.IGNORECASE
    )
    return pattern, alias_to_names, folder_to_names


def audit(
    sessions_root: Path,
    skills: list[Skill],
    cutoff: str | None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    alias_re, alias_to_names, folder_to_names = build_alias_index(skills)
    counts = {
        skill.name: {
            "skill_file_reads": 0,
            "assistant_mentions": 0,
            "user_mentions": 0,
            "tool_arg_mentions": 0,
            "evidence_events": 0,
            "sessions": set(),
        }
        for skill in skills
    }

    session_files = sorted(sessions_root.rglob("*.jsonl")) if sessions_root.exists() else []
    records = 0
    parse_errors = 0
    for file in session_files:
        session_id = file.stem
        try:
            fh = file.open("r", encoding="utf-8", errors="replace")
        except OSError:
            continue
        with fh:
            for line in fh:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    parse_errors += 1
                    continue
                timestamp = row.get("timestamp")
                if cutoff and isinstance(timestamp, str) and timestamp >= cutoff:
                    continue
                payload = row.get("payload") or {}
                payload_type = payload.get("type")
                role = payload.get("role")
                if not (
                    (payload_type == "message" and role in {"assistant", "user"})
                    or payload_type in {"function_call", "custom_tool_call"}
                ):
                    continue
                text = payload_text(payload)
                if not text:
                    continue
                records += 1

                if payload_type == "message" and role == "assistant":
                    bucket = "assistant_mentions"
                elif payload_type == "message" and role == "user":
                    bucket = "user_mentions"
                else:
                    bucket = "tool_arg_mentions"

                matched_names: set[str] = set()
                for match in alias_re.finditer(text):
                    matched_names.update(alias_to_names.get(match.group(0).casefold(), set()))

                if bucket == "tool_arg_mentions" and "SKILL.md" in text:
                    for match in SKILL_PATH_RE.finditer(text):
                        for name in folder_to_names.get(match.group(1).casefold(), set()):
                            counts[name]["skill_file_reads"] += 1
                            counts[name]["sessions"].add(session_id)
                            matched_names.add(name)

                for name in matched_names:
                    counts[name][bucket] += 1
                    counts[name]["evidence_events"] += 1
                    counts[name]["sessions"].add(session_id)

    rows: list[dict[str, Any]] = []
    for skill in skills:
        current = counts[skill.name]
        rows.append(
            {
                "name": skill.name,
                "folder": skill.folder,
                "tier": skill.tier,
                "skill_file_reads": current["skill_file_reads"],
                "assistant_mentions": current["assistant_mentions"],
                "user_mentions": current["user_mentions"],
                "tool_arg_mentions": current["tool_arg_mentions"],
                "evidence_events": current["evidence_events"],
                "session_count": len(current["sessions"]),
                "openai_yaml": skill.has_openai_yaml,
                "path": skill.portable_path,
            }
        )

    return rows, {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sessions_root": "CODEX_HOME/sessions",
        "session_files": len(session_files),
        "records_scanned": records,
        "parse_errors": parse_errors,
        "cutoff": cutoff,
        "skill_count": len(skills),
    }


def write_reports(
    rows: list[dict[str, Any]], meta: dict[str, Any], out_dir: Path, report_date: str
) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"skill-usage-audit-{report_date}.json"
    md_path = out_dir / f"skill-usage-audit-{report_date}.md"
    json_path.write_text(
        json.dumps({"meta": meta, "rows": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    active = [row for row in rows if row["tier"] == "active"]
    zero_active = [
        row
        for row in active
        if row["skill_file_reads"] == 0
        and row["assistant_mentions"] == 0
        and row["tool_arg_mentions"] == 0
    ]
    top = sorted(
        rows,
        key=lambda row: (
            row["skill_file_reads"],
            row["assistant_mentions"],
            row["tool_arg_mentions"],
        ),
        reverse=True,
    )[:30]

    lines = [
        "---",
        "page_type: audit",
        f'created_at: "{report_date}"',
        "scope: global-codex-evolution",
        "status: active",
        "---",
        "",
        f"# Skill Usage Audit {report_date}",
        "",
        "## Scope",
        "",
        f"- Session files scanned: {meta['session_files']}",
        f"- Relevant records scanned: {meta['records_scanned']}",
        f"- Parse errors: {meta['parse_errors']}",
        f"- Skills discovered: {meta['skill_count']}",
        f"- Cutoff: `{meta['cutoff']}`",
        "",
        "`skill_file_reads` is the strongest evidence because it records a concrete "
        "`SKILL.md` path in a tool call. Mentions alone do not prove execution.",
        "",
        "## Summary",
        "",
        f"- Active portfolio skills: {len(active)}",
        f"- Active skills with zero file-read, assistant, or tool-call evidence: {len(zero_active)}",
        "",
        "## Top Evidence",
        "",
        "| Skill | Tier | SKILL.md reads | Sessions | Assistant | User | Tool args |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in top:
        lines.append(
            f"| `{row['name']}` | {row['tier']} | {row['skill_file_reads']} | "
            f"{row['session_count']} | {row['assistant_mentions']} | "
            f"{row['user_mentions']} | {row['tool_arg_mentions']} |"
        )

    lines.extend(["", "## Active Skills With Zero Strong Evidence", ""])
    if zero_active:
        for row in sorted(zero_active, key=lambda item: item["name"].casefold()):
            lines.append(
                f"- `{row['name']}`: user_mentions={row['user_mentions']}, "
                f"path=`{row['path']}`"
            )
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Complete Local And Shared Portfolio",
            "",
            "| Skill | Tier | Reads | Tool calls | Sessions | openai.yaml | Path |",
            "|---|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in sorted(rows, key=lambda item: (item["tier"], item["name"].casefold())):
        lines.append(
            f"| `{row['name']}` | {row['tier']} | {row['skill_file_reads']} | "
            f"{row['tool_arg_mentions']} | {row['session_count']} | "
            f"{'yes' if row['openai_yaml'] else 'no'} | `{row['path']}` |"
        )

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit skill usage in one indexed pass.")
    parser.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    parser.add_argument("--agents-home", type=Path, default=DEFAULT_AGENTS_HOME)
    parser.add_argument("--export-root", type=Path, default=DEFAULT_EXPORT_ROOT)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DEFAULT_EXPORT_ROOT / "memories" / "vault_summaries",
    )
    parser.add_argument("--cutoff", help="Optional ISO timestamp upper bound.")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    tiers = load_portfolio_tiers(args.export_root)
    skills = discover_skills(
        [
            ("codex", args.codex_home / "skills"),
            ("agents", args.agents_home / "skills"),
        ],
        tiers,
    )
    rows, meta = audit(args.codex_home / "sessions", skills, args.cutoff)
    json_path, md_path = write_reports(rows, meta, args.out_dir, args.date)
    active_zero = sum(
        1
        for row in rows
        if row["tier"] == "active"
        and row["skill_file_reads"] == 0
        and row["assistant_mentions"] == 0
        and row["tool_arg_mentions"] == 0
    )
    print(
        json.dumps(
            {
                "meta": meta,
                "active_zero": active_zero,
                "json_report": str(json_path),
                "markdown_report": str(md_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
