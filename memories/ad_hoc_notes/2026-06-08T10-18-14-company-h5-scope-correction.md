# Company H5 app-factory scope correction

User correction: the 声之境 / 每周穿搭 / 750px H5 / unified-admin app-factory knowledge is company/work project context, not global Codex behavior and not a default for all H5, PRD, frontend, admin, personal, open-source, or external-client tasks.

Operating rule:
- Apply `app-factory-h5-admin` only when the user names the matching company project family, works inside a private registered company workspace, or explicitly asks to reuse the company H5 plus unified-admin pattern.
- Do not apply it to generic H5 pages, personal projects, open-source projects, generic landing pages, ordinary frontend implementation, unrelated admin dashboards, or unrelated product planning.
- If scope is unclear, treat `app-factory-h5-admin` as out of scope and use normal product/design/frontend/admin skills.

Fixes applied:
- Synced the local live skill with the company/work scope boundary, because the export had already been corrected but the live skill was still broad.
- Updated both local and export `agents/openai.yaml` descriptions so generated/default prompts do not imply generic H5 usage.
- Corrected exported ad-hoc notes that still described the app-factory flow as broad "future projects" or mixed H5 with mini-app output.

Validation:
- Remote export already contains `memories/vault_summaries/context-scope-boundaries.md`, `skill-routing.md`, `skill-portfolio.jsonl`, and the scoped `app-factory-h5-admin/SKILL.md`.
- Local live skill now has the same frontmatter trigger boundary as the GitHub export.
