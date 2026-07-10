# WeChat doc login-state access and Computer Use routing failure

Date: 2026-06-09T11:31:44+08:00

Authoritative note.

When the user provides a WeChat document URL or another login-state document, do not stop at static/guest fetch failure. Static fetch only proves public guest access is insufficient.

Required escalation:

1. Try the official Chrome plugin when the task depends on the user's Chrome login state.
2. If Chrome reports a browser security policy block for the target domain, stop that browser-access path. Do not try to achieve the same read through raw CDP, another browser surface, or Computer Use.
3. Computer Use is for Windows app automation and fallback desktop inspection, but it must not be used to bypass a Chrome/Browser Use domain policy block.
4. For blocked WeChat docs, ask for a safer input path: user exports/copies the document text, changes document sharing permission, uploads an allowed file export, or pastes the relevant sections.

Capability refresh fix:

- Do not mark Computer Use healthy from plugin installation, cache path, or `codex-computer-use.exe` presence alone.
- The live smoke test must verify that `nodeRepl.env.SKY_CUA_NATIVE_PIPE_DIRECTORY` is present and that `sky.list_apps()` succeeds.
- Failure observed on 2026-06-09: official Computer Use plugin `26.602.71036` and `codex-computer-use.exe` existed, and a `\\.\pipe\codex-computer-use-*` pipe existed, but `nodeRepl.env` had no `SKY_CUA_NATIVE_PIPE_DIRECTORY`; `sky.list_apps()` failed with `Computer Use native pipe is unavailable: failed to connect native pipe: os error 2 (file not found)`.

User-facing reporting rule:

- Report the actual capability tier: `static guest failed`, `Chrome login-state blocked by policy`, `Computer Use helper not connected`, or `content extracted`.
- Do not write a template answer while implying the real document was inspected.
