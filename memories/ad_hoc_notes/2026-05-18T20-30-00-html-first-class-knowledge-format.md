# HTML as first-class knowledge format

The user challenged the earlier private knowledge vault design for omitting HTML. Adopt the correction: Markdown and HTML should be complementary first-class formats, not a hierarchy where HTML is only a raw webpage snapshot.

Decision:

- Markdown is preferred for durable text knowledge: summaries, entity pages, decisions, operating rules, diffs, and portable text exports.
- HTML is preferred for visual and interactive knowledge objects: timelines, relationship maps, dashboards, report pages, rendered evidence packs, browser-native artifacts, and polished visual summaries.
- HTML must stay portable: relative links, local assets, visible citations, and no hard dependency on Codex, Obsidian, a hosted app, a vector database, or any specific AI vendor.
- If HTML uses JavaScript, keep the source local and provide adjacent JSONL/summary data so another AI can still inspect the content without executing the page.

Applied:

- Updated `%USERPROFILE%\.codex\private\knowledge-vault\README.md`.
- Updated `%USERPROFILE%\.codex\private\knowledge-vault\config\SCHEMA.md`.
