# Taste Skill evaluation

Source:
- GitHub: https://github.com/Leonxlnx/taste-skill
- Homepage: https://tasteskill.dev

Assessment:
- High-value design/front-end candidate, especially for the user's repeated complaint that AI-built UI and images look generic or ugly.
- Repo checked on 2026-05-28: active, MIT, about 24.6k stars and 1.9k forks, latest push 2026-05-26, default branch commit `3c7017d`.
- It is not one skill. It is a portfolio of frontend/design/image-generation skills: `design-taste-frontend`, `gpt-taste`, `image-to-code`, `redesign-existing-projects`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`, plus style variants.

What is useful:
- `design-taste-frontend`: strong anti-slop landing/portfolio/redesign rules, brief inference, design-system map, AI-tell bans, redesign mode, final pre-flight checklist.
- `redesign-existing-projects`: practical audit -> diagnose -> targeted fix loop for existing UI without breaking the stack.
- `image-to-code`: image-first workflow for visually important websites: generate references, analyze them, then implement.
- `brandkit` and imagegen skills: useful for visual direction boards and generated design references before coding.

Overlap:
- Overlaps with local `open-design-*` and prior `huashu-design` candidate. Taste Skill is more specific about AI design tells, landing pages, redesign audits, and image-first workflows.
- Local `open-design-design-systems` remains better for backend/admin/dashboard/product-console routing because Taste Skill explicitly says it is not for dashboards, data tables, multi-step forms, code editors, native mobile, or realtime collaboration UI.

Adoption decision:
- Do not bulk-install every Taste Skill as active yet. Too much trigger overlap would worsen skill routing.
- Treat as high-priority candidate/reference for public-facing frontend, landing pages, portfolio sites, brand pages, image-first website design, and redesign polish.
- Immediate best strategy: benchmark `design-taste-frontend` + `redesign-existing-projects` against current `open-design-*` / Huashu-style workflow on one real UI task. If it wins, selectively absorb its brief inference, AI-tell bans, redesign preflight, and image-first rules into local design routing.

Not adopted:
- Do not apply Taste Skill to admin dashboards or internal operations consoles by default.
- Do not adopt blanket rules like banning all Lucide/icons/fonts globally; keep them scoped to public-facing premium pages where the design direction calls for it.
