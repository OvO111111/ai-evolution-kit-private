# Feishu sync routing and Hermes cleanup

User correction: project-level requests like "上传飞书", "同步飞书", "发布到飞书", "归档到飞书", or "把资料放到飞书" were falling through to low-level `lark-*` CLI skills instead of the project archive/sync skill. Lark commands also inherited `HERMES_HOME`, causing the wrong Hermes-bound path to appear.

Fixes applied:
- Expanded `feishu-prd-html-sync` trigger metadata and examples to cover natural upload/sync/archive phrases.
- Clarified routing: project materials, PRDs, 方案, HTML prototypes, screenshots, handoff packages, navigation/index docs, naming/merge conflicts, preview insertion, permissions, and verification must use `feishu-prd-html-sync` first; `lark-doc`, `lark-drive`, and `lark-shared` are implementation skills under that workflow.
- Kept one-off file uploads out of the archive workflow: single-file uploads with no project archive/navigation/preview/naming requirement should use `lark-drive` directly.
- Removed the persistent user-level `HERMES_HOME` environment variable and cleared process-level `HERMES_HOME` before validating `lark-cli`.
- Updated the Feishu runbook so Lark commands run with `HERMES_HOME` cleared and do not restore it inside Feishu execution sessions.
- Patched local `lark-cli`, `lark-cli.cmd`, and `lark-cli.ps1` wrappers to clear `HERMES_HOME` before launching the Lark CLI, with `.codex-bak` backups kept next to the wrappers.
- Synced the `feishu-prd-html-sync` skill into the GitHub export workspace and added routing/portfolio/trigger-test entries.

Validation:
- `lark-cli auth status` succeeded with clean `HERMES_HOME` and showed bot/user identities ready.
- Wrapper-level cleanup means future `lark-cli` calls should avoid Hermes even while the current Codex parent process still has a stale process-level `HERMES_HOME`.
- `feishu-prd-html-sync` and `diagram-drawing-router` passed `quick_validate.py` with `PYTHONUTF8=1`.
- Trigger text search confirms live skill now includes `上传飞书`, `同步飞书`, `发布到飞书`, `归档到飞书`, and `把资料放到飞书`.
