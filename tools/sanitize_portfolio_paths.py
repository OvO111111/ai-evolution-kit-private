from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_PATH = (
    Path(__file__).resolve().parents[1]
    / "memories"
    / "vault_summaries"
    / "skill-portfolio.jsonl"
)


def portable_root(value: str) -> str:
    normalized = value.replace("/", "\\").casefold()
    if normalized.endswith("\\.codex\\skills"):
        return "%USERPROFILE%/.codex/skills"
    if normalized.endswith("\\.agents\\skills"):
        return "%USERPROFILE%/.agents/skills"
    return re.sub(r"(?i)^C:\\Users\\[^\\]+", "%USERPROFILE%", value)


def main() -> int:
    parser = argparse.ArgumentParser(description="Make skill portfolio roots portable.")
    parser.add_argument("path", type=Path, nargs="?", default=DEFAULT_PATH)
    args = parser.parse_args()

    records: list[dict[str, object]] = []
    for line in args.path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        if isinstance(record.get("root"), str):
            record["root"] = portable_root(record["root"])
        records.append(record)

    if not any(record.get("name") == "adversarial-review" for record in records):
        records.append(
            {
                "record_type": "skill_portfolio_item",
                "name": "adversarial-review",
                "folder": "adversarial-review",
                "root": "%USERPROFILE%/.codex/skills",
                "relative_path": "adversarial-review/SKILL.md",
                "tier": "active",
                "reason": "validated blind product walkthrough and conditional red-team workflow",
                "description": (
                    "Runs implementation-blind first-time-user walkthroughs or falsifiable "
                    "red-team reviews for consequential plans while excluding routine reversible work."
                ),
            }
        )

    names = [str(record.get("name")) for record in records]
    if len(names) != len(set(names)):
        raise ValueError("duplicate skill names in portfolio")

    text = "\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n"
    args.path.write_text(text, encoding="utf-8")
    print(json.dumps({"records": len(records), "path": str(args.path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
