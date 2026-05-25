---
page_type: decision
created_at: "2026-05-20"
updated_at: "2026-05-20"
sensitivity: personal
source_ids: ["open_design_repo", "user_ui_quality_feedback"]
confidence: high
status: active
---

# Admin UI Design Standard

## Decision

Backend, admin, CRM, operations dashboard, approval system, payment/customer-data console, and internal-tool work must not start from generic styling language. It must start from a closest-match product/design-system reference.

`open-design-design-systems` is promoted from candidate to active for this specific role.

## Source Takeaways

`nexu-io/open-design` is useful because it treats design as a selectable, prompt-readable system:

- design systems are packaged as portable `DESIGN.md` references
- the catalog covers product categories such as Productivity & SaaS, Backend & Data, Fintech, Developer Tools, and Chinese social/product surfaces
- the workflow combines skill selection, design-system selection, preview, lint/self-critique, and export

Adopt the workflow pattern, not the full runtime.

## Default Reference Routing

- Dense SaaS/productivity console: `linear-app.md`
- Analytics, operations, metrics, monitoring, or reporting: `dashboard.md`
- Knowledge/workflow/editor-like backend: `notion.md`
- Developer, deployment, logs, API, or infrastructure console: `vercel.md`
- Payment, billing, finance, risk, or merchant tooling: `stripe.md`
- WeChat-adjacent Chinese app, mini-program, or social commerce surface: `wechat.md`
- Content/community/creator operations in China: `xiaohongshu.md`

If none match, inspect or search for a real reference product before styling.

## Backend UI Bar

- Dense but organized information architecture.
- Tables, filters, bulk actions, status chips, empty/error/loading states, audit trails, permissions, and destructive-action confirmation are first-class.
- Avoid marketing hero layout, decorative nested cards, huge gradients, fake metrics, random illustrations, and one-note palettes.
- Before coding major screens, define palette, typography scale, spacing scale, table density, panel radius, status colors, icon set, and responsive behavior.
- After coding, run browser/screenshot verification when possible.
