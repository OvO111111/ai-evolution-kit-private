---
scope: global-codex-evolution
authority: superseding-correction
source: user-correction-after-incomplete-system-report
validated: 2026-07-10
---

# Evolution completeness correction

A system-wide evolution task is incomplete if the final report only gives abstract
outcomes. It must list every changed skill or grouped official update, the old
problem, new behavior, reason, behavioral test, degraded state, and deliberately
unchanged items.

Current validated baseline:

- 77 local/shared portfolio entries: 34 active, 35 reference, 8 candidate; zero
  active item without file-read, assistant-plan, or real tool-call evidence.
- 26 fresh GPT-5.6 route cases passed; the operating-dashboard case is explicitly
  degraded because remote Data Analytics `build-dashboard` was unavailable in the
  independent CLI session and bundled visualization handled the fallback.
- 30 static evolution contracts pass, including report-completeness and export-safety checks.
- Local `xlsx`, `docx`, `pptx`, raw-CDP browser, desktop control, PDF, and
  image-to-code skills are non-implicit legacy fallbacks behind official plugins.
- Route evaluations are serial by default. Parallel `codex exec` caused a shared
  model-cache read/write race and must not be used by automation.
- Weekly capability refresh must run static checks and only affected dynamic cases,
  then report an exact changed-skill manifest. It must not claim a preferred remote
  plugin worked when only a fallback route was available.

Portable exact manifests live in the evolution export vault summaries:

- `skill-change-manifest-2026-07-10.md`
- `evolution-mechanism-manifest-2026-07-10.md`
