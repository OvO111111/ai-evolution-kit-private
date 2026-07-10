---
created_at: "2026-05-28T16:30:00+08:00"
source: "user rejected repeated internal-tool-platform design outputs"
sensitivity: personal
status: active
---

# Admin Template-First Design Fix

The user correctly pointed out that prior fixes still trusted the agent's weak freehand design ability. The right correction is not more abstract standards; it is to make admin/internal UI work template-first.

Adopted correction:
- Added `assets/admin-console-reference.html` to `admin-platform-execution-gate` as a concrete mature console scaffold.
- Added `scripts/validate_admin_template.py` so the template has to pass structural checks.
- Updated the skill with a Template-First Rule: after admin/internal UI quality failure, start by copying and adapting the reference template instead of starting from a blank page or broken project page.
- Rendered the template with headless Chrome and saved a screenshot in the export vault.

Validation:
- `python scripts/validate_admin_template.py`: PASS on global skill and export copy.
- `python tools/check_admin_ui_quality_gate.py`: PASS.
- `python tools/check_skill_routing.py`: 34 test cases, 0 failures.
- Headless Chrome screenshot: `memories/vault_summaries/admin-console-reference-screenshot-2026-05-28.png`.
