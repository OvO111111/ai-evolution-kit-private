---
created_at: "2026-05-28T16:05:00+08:00"
source: "user validation failure after internal-tool-platform test"
sensitivity: personal
status: active
---

# Admin UI Quality Contract Fix

The user retested the internal-tool-platform workflow and reported that outputs were still poor. This proved the previous fix was incomplete: it strengthened natural trigger/routing, but did not force the design output to inherit concrete patterns from good references.

Adopted correction:
- Admin/internal design skills must not stop at "use Linear/Dashboard" or color-token changes.
- The artifact must specify and implement app shell proportions, navigation model, first-screen decision, 3-5 decision metrics, table row density, filter/search toolbar, detail drawer/split-pane pattern, action states, empty/error/loading states, and what each page must not show.
- If output remains a CRUD/card pile with better colors, the skill was not applied.
- Added `Reference-Grade Execution Contract` to `admin-platform-execution-gate`.
- Added "reference docs are not mood boards" rule to `open-design-design-systems`.
- Added `tools/check_admin_ui_quality_gate.py` to verify these hard requirements exist in the export bundle.

Validation:
- `python tools/check_skill_routing.py`: 34 test cases, 0 failures.
- `python tools/check_admin_ui_quality_gate.py`: PASS.
