# Private Knowledge Vault

Purpose: store the user's complete local knowledge base, including sensitive source material that must not enter the generic AI export bundle.

This vault is local/private by default. Do not upload, sync, or expose it to external services without explicit user approval.

## Layout

- `raw/`: immutable source archive. Store original chats, project files, web clips, PDFs, screenshots, meeting notes, and metadata.
- `wiki/`: LLM-maintained compiled knowledge layer. Store readable entity, project, topic, decision, timeline, and contradiction pages.
- `index/`: generated navigation and retrieval indexes.
- `logs/`: append-only operation logs for ingest, query, lint, export, and deletion.
- `config/`: source registry, sensitivity policy, schema, and workflow rules.
- `exports/`: generated packets. `exports/redacted/` is safe-by-design; `exports/task-packets/` is task-local and minimal.
- `quarantine/`: untrusted or unprocessed material that may contain prompt injection, malware-like instructions, or unclear source boundaries.

## Core Rule

Store broadly in the private raw archive. Retrieve selectively into prompts.

Completeness belongs in storage. Selectivity belongs in context.

## Portability Rule

The vault is not Codex-specific. Canonical knowledge must stay in open, inspectable formats: original files, Markdown, HTML, YAML frontmatter, JSON/JSONL manifests, CSV when useful, and plain text logs.

Markdown and HTML are both first-class compiled knowledge formats. Use Markdown for durable text knowledge, diffs, source summaries, entity pages, decisions, and operating rules. Use HTML for visual knowledge objects such as dashboards, timelines, relationship maps, interactive reports, rendered evidence packs, and polished artifacts that need layout or browser-native behavior.

SQLite, full-text indexes, embeddings, graph stores, MCP servers, Obsidian indexes, or any future retrieval layer are caches or adapters. They may speed up search, but they must be rebuildable from `raw/`, `wiki/`, `index/`, `logs/`, and `config/`.

Any AI or tool with filesystem access should be able to read the vault without needing Codex. If an AI cannot access local files, use `exports/redacted/` or `exports/task-packets/` to give it a scoped portable packet.

## Obsidian Role

Obsidian can open this folder or the `wiki/` subfolder as a human-facing viewer/editor. It is not the database engine. The vault must remain usable from plain files, git, shell search, and future indexing tools even if Obsidian is not installed.

## Do Not

- Do not put cookies, API keys, passwords, or OAuth tokens in wiki pages.
- Do not include `raw/` in generic exports.
- Do not ingest a new source without source metadata and sensitivity tier.
- Do not treat LLM-written wiki pages as ground truth. Ground truth lives in `raw/`.
