# Open Design Admin UI Absorption

Date: 2026-05-20

Source: https://github.com/nexu-io/open-design

User criticism: Codex backend/admin UI output has been low quality and too often invented from generic adjectives. The requested correction is to learn from matching design-system references before building, especially for backend and admin products.

Adopted:

- Promote `open-design-design-systems` to active for backend/admin UI, dashboards, internal tools, CRMs, approval systems, payment/customer-data consoles, and prototypes.
- Add a hard rule: pick the closest real product/design-system reference before coding UI.
- Use reference routing: `linear-app` for dense SaaS/productivity, `dashboard` for analytics/ops, `notion` for workflow/editor backends, `vercel` for developer/infrastructure consoles, `stripe` for payment/finance, `wechat` for WeChat-adjacent Chinese surfaces, and `xiaohongshu` for Chinese creator/content operations.
- Keep other Open Design skills as candidate/reference unless a task proves they should become active.

Rejected / not adopted:

- Do not install or run the whole Open Design daemon/runtime as the default UI path.
- Do not copy brand systems as official assets or imitate trademarked identity.
- Do not stack multiple design skills by default; use the smallest matching design-system gate.

Validation:

- Added `backend_admin_ui_design` to the skill trigger tests.
- Re-run `check_skill_routing.py` after edits before claiming the route is active.
