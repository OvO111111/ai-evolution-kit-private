from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def first_existing(*paths: Path) -> Path:
    for path in paths:
        if path.exists():
            return path
    joined = ", ".join(str(path) for path in paths)
    raise SystemExit(f"missing required file; tried: {joined}")


PORTFOLIO = first_existing(
    ROOT / "config" / "skill-portfolio.jsonl",
    ROOT / "memories" / "vault_summaries" / "skill-portfolio.jsonl",
)
TESTS = first_existing(
    ROOT / "config" / "skill-trigger-tests.jsonl",
    ROOT / "memories" / "vault_summaries" / "skill-trigger-tests.jsonl",
)


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_no}: invalid JSONL: {exc}") from exc
    return rows


def main() -> int:
    portfolio = read_jsonl(PORTFOLIO)
    tests = read_jsonl(TESTS)

    by_name: dict[str, list[dict]] = defaultdict(list)
    by_folder: dict[str, list[dict]] = defaultdict(list)
    for item in portfolio:
        by_name[item["name"]].append(item)
        by_folder[item["folder"]].append(item)

    failures: list[str] = []
    warnings: list[str] = []

    for case in tests:
        allowed_tiers = set(case.get("allowed_tiers") or [])
        expected_skills = case.get("expected_skills") or []
        if not expected_skills and case.get("expected_tool"):
            continue
        for skill in expected_skills:
            matches = by_name.get(skill, []) + by_folder.get(skill, [])
            if not matches:
                failures.append(f"{case['case_id']}: expected skill not found: {skill}")
                continue
            tiers = {m.get("tier") for m in matches}
            if allowed_tiers and not (tiers & allowed_tiers):
                failures.append(
                    f"{case['case_id']}: {skill} tier {sorted(tiers)} not in allowed {sorted(allowed_tiers)}"
                )
            if "active" not in tiers and "active" in allowed_tiers:
                warnings.append(f"{case['case_id']}: {skill} is not active; current tiers={sorted(tiers)}")

    duplicate_names = {name: vals for name, vals in by_name.items() if len(vals) > 1}
    for name, vals in sorted(duplicate_names.items()):
        tiers = sorted({v["tier"] for v in vals})
        paths = ", ".join(v["relative_path"] for v in vals)
        warnings.append(f"duplicate skill name {name}: tiers={tiers}; paths={paths}")

    active_count = sum(1 for item in portfolio if item.get("tier") == "active")
    if active_count > 30:
        warnings.append(f"active skill count is high: {active_count} > 30")

    print(f"portfolio_items={len(portfolio)}")
    print(f"test_cases={len(tests)}")
    print(f"active_count={active_count}")
    print(f"failures={len(failures)}")
    print(f"warnings={len(warnings)}")

    if warnings:
        print("\nWARNINGS")
        for item in warnings:
            print(f"- {item}")

    if failures:
        print("\nFAILURES")
        for item in failures:
            print(f"- {item}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
