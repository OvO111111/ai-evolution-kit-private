---
name: open-design-design-systems
description: "Use when the user explicitly asks for Open Design, a brand-grade DESIGN.md, design-system construction, or adaptation from a real reference benchmark; also use when the UI/product-design router selects Open Design as a distinct comparison lane. Do not select merely because a UI should be beautiful, an admin page is ugly, or a normal frontend needs styling."
---

# Open Design Design Systems

Use this before producing visual artifacts when the request needs strong taste, brand direction, or a non-generic style. For admin panels, backends, internal tools, dashboards, and product prototypes, use it as a hard design gate rather than a decorative reference.

## Workflow

1. Pick one visual direction before making anything.
2. For product UI, admin panels, dashboards, and backend prototypes, first identify the closest matching real product/design-system reference. Do not invent a style from vague words like "modern" or "premium".
3. Read only the relevant reference file from `references/`.
4. Convert the design system into concrete tokens: palette, typography, spacing, composition, density, component shape, icon style, interaction states, and avoid-list.
5. Produce the artifact or image prompt from those tokens.
6. Before finalizing, self-review against hierarchy, specificity, restraint, execution quality, data density, and brand fit.

Reading this skill or a reference file is not adoption. For admin/internal products, the output must visibly carry the chosen system through navigation, page hierarchy, tables, forms, controls, empty/error/loading states, and metric presentation. If the review finds only cosmetic changes on top of a broken IA or page model, restart from the admin platform gate.

## Admin And Backend UI Defaults

When building or revising a backend, admin console, CRM, operations dashboard, approval system, payment/customer-data console, or internal tool, this skill is mandatory.

Default benchmark routing:

- Dense SaaS/productivity console: `linear-app.md`
- Analytics, operations, metrics, monitoring, or reporting: `dashboard.md`
- Knowledge/workflow/editor-like backend: `notion.md`
- Developer, deployment, logs, API, or infrastructure console: `vercel.md`
- Payment, billing, finance, risk, or merchant tooling: `stripe.md`
- WeChat-adjacent Chinese app, mini-program, or social commerce surface: `wechat.md`
- Content/community/creator operations in China: `xiaohongshu.md`
- If none match, search or inspect a real product reference before styling.

Backend UI standard:

- Prioritize scan speed, table ergonomics, filters, status chips, empty/error/loading states, bulk actions, audit trails, and clear information hierarchy.
- Use restrained visual styling. Avoid marketing hero composition, decorative cards, huge gradients, random illustrations, fake metrics, and one-note color palettes.
- Prefer dense but organized layouts: sticky table headers, predictable side navigation, compact toolbars, readable forms, clear destructive-action confirmation, and visible permissions/state.
- For every important screen, define at least palette, typography scale, spacing scale, table density, card/panel border radius, status colors, icon set, and responsive behavior before coding.
- After coding, verify with screenshot/browser review when possible. If no visual verification ran, say so.
- If the user says the whole platform still looks amateur, stop polishing individual widgets. Rebuild the layout contract first: left navigation purpose, first-screen decision, content density, primary action, detail pattern, and what each page must not show.
- Reference docs are not mood boards. The final UI must inherit concrete structure: shell proportions, density, type scale, border/radius discipline, status vocabulary, table/detail pattern, and interaction states. If only the colors changed, the skill was not applied.

## Reference Choices

- `openai.md`: restrained AI/product interface.
- `linear-app.md`: dense, polished SaaS/productivity UI.
- `vercel.md`: developer/product marketing and sharp monochrome UI.
- `apple.md`: premium consumer hardware/app presentation.
- `stripe.md`: SaaS/fintech marketing polish.
- `notion.md`: calm knowledge/productivity interfaces.
- `xiaohongshu.md`: Chinese social/creator marketing style.
- `wechat.md`: WeChat-adjacent app and social surfaces.
- `editorial.md`: magazine/poster/editorial layouts.
- `dashboard.md`: analytics/ops/data-heavy surfaces.
- `luxury.md`, `premium.md`: high-end product presentation.
- `minimal.md`, `modern.md`, `professional.md`: safe commercial UI baselines.
- `brutalism.md`: intentionally raw experimental direction.

## Rules

- Do not mix more than two design systems unless the user asks.
- Do not copy trademarked brand marks or imply official affiliation.
- For product mockups, use the system as style inspiration, then adapt it to the user's domain.
- Prefer fewer, stronger visual decisions over many decorative effects.
