---
created_at: "2026-05-28T15:35:00+08:00"
source: "internal-tool-platform chat audit"
sensitivity: personal
status: active
---

# Internal Tool Platform Skill Failure

The 2026-05-27 internal-tool-platform window shows a real skill absorption failure. It was not that design/PM/admin skills were never opened; `pm-prd`, `open-design-design-systems`, `admin-platform-execution-gate`, and `design-taste-frontend` all had strong usage evidence. The failure was execution: skills were treated as references or after-the-fact justification instead of hard gates.

Root cause:
- The agent kept making local patches after the user rejected the whole admin platform structure.
- The multi-application platform PRD/HTML reference was not converted into a reference-inheritance packet before rebuilding the UI.
- Page model, navigation hierarchy, metric definitions, fake-control states, table/detail ergonomics, and visual system were not locked as completion blockers.
- Screenshots and API checks were treated as verification even when the product structure and visual quality still failed.

Adopted rule:
- For backend/admin/internal-tool UI rejected twice, or when the user says the whole platform is ugly/structurally wrong/not improved by skills, stop incremental patching.
- Re-run `admin-platform-execution-gate` plus `open-design-design-systems`.
- Produce a reset packet and isolated review artifact or explicit before-code redesign plan before touching project code again unless the user explicitly orders direct implementation.
- `design-taste-frontend` may critique visual quality when explicitly named, but it must not override the admin/internal-tool gate.

Validation:
- Added `admin_ui_rejected_loop_breaker` and `admin_ui_reference_inheritance_failure` trigger tests.
- Updated global and export copies of `admin-platform-execution-gate`, `open-design-design-systems`, `AGENTS.md`, and `skill-routing.md`.
