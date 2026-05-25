# Skill Trigger Test Harness

Date: 2026-05-19

User criticism: many skills have been installed or adapted, but correct triggering had not been tested. The immediate failure example was `pm-prd`: another conversation produced a PRD/prototype-style answer without first reading the referenced PRDs, HTML mockups, samples, interface docs, and confirmed business boundaries.

Correction:

- Added a global skill gate to `C:\Users\skzjc\.codex\AGENTS.md`: every non-trivial task must classify the task family, name selected skills or state why no skill applies, identify required source inspection, and stop if a mandatory skill has not been opened or applied.
- Added mandatory PRD/product/prototype routing to `pm-prd`.
- Added `C:\Users\skzjc\.codex\private\knowledge-vault\config\skill-trigger-tests.jsonl` with 25 representative task-family checks.
- Added `C:\Users\skzjc\.codex\private\knowledge-vault\scripts\check_skill_routing.py` to validate expected skills against the portfolio tiers.

Validation:

- Command: `python C:\Users\skzjc\.codex\private\knowledge-vault\scripts\check_skill_routing.py`
- Result: `portfolio_items=61`, `test_cases=25`, `active_count=27`, `failures=0`, `warnings=9`.

Interpretation:

- This is not proof that all future routing will be perfect.
- It is a concrete regression harness that catches missing skills, wrong active/reference/candidate assumptions, and accidental claims that an unvalidated skill is active.
- Warnings are intentional for reference/candidate skills such as some `open-design-*`, `imagegen`, `openai-docs`, `caveman*`, and `skill-creator`.
