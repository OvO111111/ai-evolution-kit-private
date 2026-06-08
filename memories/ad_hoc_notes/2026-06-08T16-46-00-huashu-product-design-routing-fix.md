# Huashu and Product Design routing fix

User reported that design work was still not truly loading Huashu/Product Design skills and only applying them superficially.

Findings:
- `huashu-design` was not installed as a local Codex skill under `.codex/skills` or `.agents/skills`, so it could not trigger even if the user named it.
- Product Design was installed, but design tasks could still bypass `product-design:index` and `get-context` when the agent treated the request as ordinary HTML/frontend work.
- The durable fix is not more AGENTS.md text; it is local skill metadata and router coverage.

Changes made:
- Installed an adapted local `huashu-design` skill at `C:\Users\skzjc\.codex\skills\huashu-design`.
- Preserved upstream Huashu assets/references/scripts locally, but replaced the giant upstream entrypoint with a concise local `SKILL.md`.
- Updated `ui-product-design-router` so mentions of `huashu`, `花叔`, `Product Design`, design skills, ugly/generic UI, high-fidelity HTML, motion demos, design variants, and app mockups route through the correct design gate.

Durable rule:
- If a user names a design skill and the answer does not explicitly open/use the skill entrypoint and report `Design route: ...`, treat that as a routing failure.
- Huashu owns polished visual artifacts, prototype boards, HTML decks, motion demos, and design-direction exploration.
- Product Design owns plugin workflows that require brief confirmation, ideation, prototype, URL/image-to-code, and design QA.
- Admin/internal tools still start with `admin-platform-execution-gate`; Huashu/Product Design may help visual direction only after page tasks are clear.
