# Computer Use pipe fallback fix after plugin update

Date: 2026-06-09T11:48:20+08:00

Authoritative note.

Problem:

- Official Computer Use plugin `26.602.71036` was installed, but `sky.list_apps()` failed because the runtime tried an unavailable native pipe path.
- `\\.\pipe\codex-computer-use-*` existed on Windows, but the JS runtime did not expose a usable `SKY_CUA_NATIVE_PIPE_DIRECTORY` value.

Fix applied:

- Patched `%USERPROFILE%\.codex\plugins\cache\openai-bundled\computer-use\26.602.71036\scripts\computer-use-client.mjs`.
- The client now discovers a fallback pipe only when exactly one `codex-computer-use-*` pipe exists.
- If a stale injected pipe fails, the client retries the single discovered pipe before reporting failure.

Validation:

- After patch and JS reset, `setupComputerUseRuntime()` succeeded.
- `sky.list_apps()` returned `ok: true`, `appCount: 40`.
- Visible apps included Chrome, WeChat, Word, Excel, Open Design, VPN apps, and other local Windows apps.

Boundary:

- This restores Windows app control capability.
- It does not authorize using Computer Use to bypass a Browser Use policy block on `doc.weixin.qq.com/doc/...`.
- For WeChat document content blocked by official Chrome policy and unavailable through public guest fetch, use a safer source path: user clipboard copy, file export/upload, sharing permission change, or a proper document API/connector.
