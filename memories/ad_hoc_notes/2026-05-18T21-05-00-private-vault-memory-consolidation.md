# Private vault memory consolidation

Trigger: the user asked to start building the memory system now, focusing on project-extraction ability, habits, consensus, evolution, and lookup pointers rather than concrete project code or large task-local materials.

Applied:

- Created first compiled knowledge pages under `%USERPROFILE%\.codex\private\knowledge-vault\wiki`.
- Added project registry entries that record what projects were done and where to inspect details, without copying code or large files.
- Added source map, query guide, Chinese alias index, and source registry.
- Created rebuildable SQLite/FTS cache at `%USERPROFILE%\.codex\private\knowledge-vault\db\vault.sqlite`.

Scope:

- Included reusable habits, self-evolution rules, skill routing, HTML artifact strategy, vault architecture, export boundaries, multi-agent context protocol, WeChat work-context constraints, and WeChat Pay product-design retrieval pattern.
- Excluded raw project code, raw work chat contents, account state, secrets, customer/payment data, and large private files.

Policy:

- Project knowledge in the vault should answer "what did we do and where should I inspect details", not duplicate whole project workspaces.
- SQLite and FTS are caches. Canonical storage remains Markdown, HTML, JSONL, YAML, CSV, source files, and logs.
