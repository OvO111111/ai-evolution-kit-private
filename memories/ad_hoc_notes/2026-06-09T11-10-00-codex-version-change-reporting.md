# Codex version change reporting

## User requirement

The user noticed another Codex/plugin update and said every new version must be proactively reported with what changed.

## What was found on 2026-06-09

- Codex Windows package path shows `OpenAI.Codex_26.602.4764.0_x64__2p2nqsd0c76g0`.
- Official curated plugin caches now use `cd0fccd4` for `build-web-apps`, `github`, `superpowers`, and `vercel`.
- `Data Analytics` cache includes `0.1.41-cf2b8b6c00d3`.
- `Product Design` cache includes `0.1.44`.
- `lark-cli` had `1.0.49` available; it was updated from `1.0.48` to `1.0.49`, npm wrappers were patched again to clear `HERMES_HOME`, and `auth status --verify`, `docs --help`, `drive --help`, and `whiteboard --help` passed with injected `HERMES_HOME`.

## Fix applied

- Added `tools/codex_capability_snapshot.py` to create and compare version snapshots for Codex app path, official plugin caches, npm/global CLI outdated status, and external skill upstream state.
- Wrote current baseline to `C:\Users\skzjc\.codex\version-snapshots\codex-capabilities-latest.json`.
- Updated the existing heartbeat automation `automation` from weekly to daily. It must notify only when versions/capabilities change, and must explicitly report what changed, expected workflow impact, smoke tests, low-risk updates, skipped risky updates, and whether restart/new window is needed.

## Durable rule

Do not wait for the user to notice Codex/plugin updates. Daily refresh must compare a saved version snapshot. If a Codex app, official plugin, remote plugin, CLI, or external skill upstream changes, notify with concrete changes. If no change, stay quiet.
