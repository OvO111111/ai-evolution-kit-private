# Weekly capability refresh

## Check time

2026-06-08 18:10 +08:00

## Updated

- `lark-cli` updated from `1.0.43` to `1.0.48` via `lark-cli update`.
- Lark skills updater reported `0 official, 0 updated, 0 added, 0 skipped because deleted locally`.
- The update regenerated npm wrappers and removed the previous Hermes guard workaround, so the wrappers were patched again to clear `HERMES_HOME` before launching `@larksuite/cli`.

## Verified

- `lark-cli --version`: `1.0.48`.
- With `HERMES_HOME=C:\Users\skzjc\.hermes` injected, `lark-cli auth status --verify` succeeded; bot and user identities are ready and verified.
- With the same injected `HERMES_HOME`, `lark-cli docs --help`, `lark-cli drive --help`, and `lark-cli whiteboard --help` all loaded normally, proving the Hermes-bound error path is not active.
- Official Computer Use plugin `26.602.40724` live smoke passed through the official runtime path: `sky.list_apps()` returned `ok: true`, `appCount: 40`, with Chrome, WeChat, Excel, and Word visible.
- Official Chrome plugin `26.602.40724` live smoke passed through extension bootstrap: `openTabCount: 14`, documentation contained `openTabs` and `claimTab`, and browser control was finalized after the read-only check.
- Primary runtime bundle for Documents, Presentations, and Spreadsheets is available at version `26.601.10930`.
- Design routing smoke remains at `partial pass`; four-lane design comparison has a rendered HTML artifact and screenshot with `skill_lane_count: 4`.

## Skipped / needs confirmation

Global npm outdated check found newer versions for `@cloudbase/cli`, `@cloudbase/cloudbase-mcp`, `@cloudcli-ai/cloudcli`, `agent-browser`, `mcporter`, and `openclaw`. These were not auto-updated because they may affect cloud/resource operations, browser automation, MCP schemas, or existing workflows.

## Backup threshold

The threshold of 3 or more unsynced evolution-related updates is met. Safe export sync should include curated notes and skill/router files only; do not stage raw `memories/extensions/`, raw sessions, screenshots, tokens, OAuth grants, Feishu/Lark document tokens, or project-specific large files.
