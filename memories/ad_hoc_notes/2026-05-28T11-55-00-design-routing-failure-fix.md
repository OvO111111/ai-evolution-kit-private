# Design routing failure fix

Trigger:
- User reported another Codex window produced an ugly, structurally weak backend/admin design and did not apply the installed/evaluated design skills.

Failure diagnosis:
- Existing rules said backend/admin UI should use `open-design-design-systems`, but the rule was still too easy to skip in practice.
- Taste Skill had been evaluated as a candidate/reference, so future windows would not automatically route public-facing design/redesign work through it.
- The failure is a routing/enforcement failure, not a lack of more design inspiration.

Changes made:
- Installed selected Taste Skill capabilities into global skills and export bundle:
  - `design-taste-frontend`
  - `redesign-existing-projects`
  - `image-to-code`
- Updated global `AGENTS.md` and export `AGENTS.md`:
  - public frontend/landing/brand/portfolio/redesign/image-first website tasks must use Taste routing.
  - backend/admin/dashboard/internal tool work remains routed to `open-design-design-systems`.
  - backend/admin design gate is now a stop condition: selected reference, page task matrix, primary actions, table/form/filter density, states, metrics, permission/audit behavior, responsive behavior, and screenshot review plan must be locked before coding or completion claims.
- Updated export `skill-routing.md`, `skill-portfolio.jsonl`, and `skill-trigger-tests.jsonl` to make the routing testable.

Adopted rule:
- If mandatory design routing is skipped and the output is ugly, structurally weak, or unverified, treat it as a routing failure. Patch the gate and add a trigger test before discussing more candidate tools.
