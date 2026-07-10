# Codex capability refresh, 2026-06-08

Context: user noticed multiple Codex updates during the week and asked what changed and whether the new capabilities can actually be used.

Findings:
- Codex desktop package resolved locally to `OpenAI.Codex_26.602.4764.0_x64__2p2nqsd0c76g0`; direct `codex --version` failed with WindowsApps access denied, so use the package path as local evidence instead of claiming CLI version output.
- Official bundled `Computer Use`, `Chrome`, and in-app `Browser` are now cached at `26.602.40724`.
- Official `Product Design` is cached at `0.1.43`.
- Official `Data Analytics` is cached at `0.1.38-cf2b8b6c00d3`.
- Official curated `GitHub`, `Build Web Apps`, `Vercel`, and `Superpowers` are cached at `3f0def1b`.
- Official primary runtime remains `26.601.10930` for spreadsheets, presentations, documents, PDFs, images, and related runtimes.

Smoke tests:
- `Computer Use` `sky.list_apps()` passed and returned 40 apps, including running Chrome and WeChat plus discoverable Excel and Word.
- `Chrome` setup checks passed: Chrome running, extension installed/enabled, native messaging manifest correct.
- `Chrome` runtime control passed: connected to the extension backend and listed 12 open tabs, then finalized the browser session without exposing tab details.
- Workspace dependency runtime loaded successfully at bundle `26.601.10930`.
- `Data Analytics` `validate_artifact` passed after using the correct native report schema: `blocks[]` reading path, `manifest.charts[]`, `snapshot.datasets`, and `encodings.x/y`.
- `gh auth status` passed as user `OvO111111`; GitHub CLI remains a verified route.

Adoption strategy:
- Use official `Computer Use` as the primary route for Windows desktop apps such as WeChat, Excel, Word, PowerPoint, and Feishu when no safer API/CLI route exists. Keep local `desktop-control` as legacy fallback only.
- Use official `Chrome` only for tasks that need the user's Chrome state: logged-in sessions, current tabs, cookies, or extensions. Prefer APIs, CLIs, or dedicated connectors first when they can satisfy the task.
- Use official in-app `Browser` as the default browser surface for localhost, file URLs, and local frontend verification.
- Use `Product Design` for UI/product design work through its brief gate; do not build from prose alone when a visual target is missing. For serious redesigns, require source capture and QA comparison.
- Use `Data Analytics` as the primary route for source-backed reports, KPI work, dashboards, metric diagnostics, and analysis artifacts. It should preserve datasets, source queries, metric definitions, and chart encodings, not just produce prose.
- Keep official Office runtimes as primary for spreadsheet/document/presentation work; local `xlsx`, `docx`, and `pptx` remain fallback/repair skills.
- Treat `Superpowers` as workflow reference for planning/debugging/review when useful, not as a blanket always-on trigger that bloats context.

Validation boundary:
- Runtime access improved and was smoke-tested. Real quality improvement for design, analytics, and complex app delivery still requires task-level validation against actual project materials and screenshots.
- No immediate GitHub export push from this note alone; weekly sync should batch safe evolution updates unless the user asks to push.
