# GPT-5.6 Codex System Correction Report

Date: 2026-07-10

## Outcome

The locally discoverable Codex history, memory vault, project roots, skills, plugin
caches, and automations were audited. High-impact routing and execution failures were
corrected and tested in fresh GPT-5.6 sessions. This report contains aggregate and
portable evidence only; it excludes chat bodies, project contents, account state,
credentials, document tokens, customer/payment data, and private browser details.

## Audit Coverage

- 34 session files, 178,605 records, 4.10 GB scanned, 0 parse errors.
- 26 project roots, 40,925 files, 3.33 GB indexed.
- 145 memory files audited, including the superseding correction notes.
- 272 `SKILL.md` files found, including active and stale plugin cache versions.

Historical user-correction signals:

| Failure family | Messages | Sessions |
|---|---:|---:|
| skill not applied | 30 | 11 |
| verification or truth gap | 47 | 11 |
| stopped after a substep | 17 | 5 |
| outcome missing from report | 32 | 8 |
| design quality failure | 39 | 11 |
| scope boundary failure | 6 | 3 |
| browser/computer capability failure | 69 | 17 |
| automation/update failure | 26 | 4 |
| memory/export failure | 32 | 4 |

## Corrections

1. Company H5 reuse is now explicitly company/work scoped. Generic, personal,
   client, and open-source H5 work routes through generic Product Design instead.
2. Company H5 sequencing is analysis, H5, H5 review, admin, admin review, then PRD.
   The workflow no longer drafts a PRD or admin system before the frontend behavior
   is confirmed.
3. Admin planning is a short execution gate, not a stopping point. It no longer
   forces one dark template or a fixed reference style.
4. PRD work inspects sources before drafting and asks at most one compact batch of
   three material questions. Routine steps continue without asking.
5. Design routing now distinguishes Product Design, Huashu, Open Design, and taste
   lanes by structure and purpose. Multi-option requests cannot be recolors of one
   design.
6. Agent Reach is a platform-specific escalation after normal web access. Cookie
   import and account-changing actions are not defaults.
7. Local legacy `image-to-code` and PDF skills were renamed and disabled for
   implicit invocation so official plugin routes win. Long fallback manuals were
   moved behind progressive-disclosure references.
8. Seven project-local Caveman copies were renamed as reference copies and disabled
   for implicit invocation. Active skill-name conflicts are now zero.
9. All three scheduled automations now use `gpt-5.6-sol` with high reasoning. The
   Metabase task was repaired from a corrupted prompt to a short project-local,
   source-driven, secret-free check.
10. Lark CLI was updated from 1.0.65 to 1.0.68; official skills and the CLI are in
    sync at 1.0.68. PowerShell, cmd, and shell wrappers continue to clear
    `HERMES_HOME`.
11. Exported company-H5 references were redacted. Exact prices, contacts, company
    subjects, Feishu tokens, and local project paths remain private.
12. Local `xlsx`, `docx`, `pptx`, raw-CDP browser, and desktop-control skills were
    demoted to non-implicit legacy fallbacks so official runtime capabilities win.
13. `web-access` was rebuilt as the ownership router for GitHub, static web,
    login-state Chrome, in-app Browser, Playwright, Agent Reach, and CDP fallback.
14. Huashu and Open Design descriptions were narrowed so ordinary ugly-UI or
    beautiful-UI wording no longer activates both design lanes.
15. `absorb-lessons` now requires an impact map, before/after test, exact changed-skill
    manifest, and residual-risk report for system-wide evolution work.
16. The portable export was mechanically redacted and now has a fail-closed safety
    scanner for personal paths, Feishu document identifiers, private hosts, known
    contacts, Lark identities, and secret-shaped values.

## Tests

Static contracts: 30/30 passed. Current Product Design version was 0.1.50; local
skill names had zero duplicate conflicts.

The skill-usage audit was rewritten from an O(records x skills) scan that timed out
after 124 seconds to a one-pass indexed scan that completed in about 24 seconds.
It classified 77 local/shared skills: 34 active, 35 reference, and 8 candidate. Every
active item had file-read, assistant-plan, or real tool-call evidence.

Fresh-session route evaluations: 26/26 passed with `gpt-5.6-sol`. One case is
explicitly degraded: the preferred remote Data Analytics dashboard skill was not
visible in the independent CLI session, so the safe bundled visualization route was
selected and recorded as a preference miss.

| Case | Required route proved |
|---|---|
| generic H5 | generic Product Design; company factory excluded |
| company H5 | company factory and H5-before-admin-before-PRD order |
| admin redesign | UI router plus admin execution gate; continued execution |
| PRD rewrite | source inspection before drafting |
| four design lanes | four structurally distinct design skill lanes |
| login-state document | official Chrome route |
| Windows Excel | official Computer Use; desktop fallback excluded |
| data report | data-analysis report plus official spreadsheet route |
| Feishu project sync | project sync plus native document/drive routes |
| public WeChat article | web-access escalation route |
| ordinary PDF | official primary-runtime PDF; legacy fallback excluded |
| Word document | official Documents; DOCX fallback excluded |
| PowerPoint | official Presentations; PPTX fallback excluded |
| dynamic public page | web-access plus in-app Browser; Playwright excluded |
| Feishu whiteboard | diagram router plus native whiteboard and Lark shared setup |
| Feishu drive upload | native drive route; project sync excluded |
| Feishu group read | native Lark IM route; WeChat context excluded |
| WeChat Pay planning | scoped WeChat Pay product-design route |
| WeChat work groups | read-only group-isolated context route |
| scanned images | OCR and documents route |
| local HTML architecture diagram | diagram router; Feishu excluded |
| evolution intake URL | absorb-lessons plus web-access; installer excluded |
| Metabase BI | project-scoped semantic-layer route |
| operating dashboard | safe visualization fallback; preferred Data Analytics recorded unavailable |
| video frames | ffmpeg video-frames route |
| GitHub triage | official GitHub route; publishing route excluded |

Live callable checks:

- Official Computer Use initialized and returned the current Windows app list.
- Official Chrome initialized through the extension and returned live open tabs.
- A separate GPT-5.6 smoke session exited successfully with no skill-icon warning,
  no default-prompt warning, and no stream disconnect.
- Lark auth verification and docs/drive/whiteboard help routes passed without Hermes.

## Current Versions

- Windows Codex app: 26.707.3748.0.
- Codex CLI used by tests: 0.144.0-alpha.4.
- Browser, Chrome, Computer Use: 26.707.31428.
- Product Design: 0.1.50.
- Data Analytics: 0.2.6-d37358633e00.
- Documents, PDF, Presentations, Spreadsheets, Template Creator: 26.709.11516.
- Lark CLI and official Lark skills: 1.0.68.

## Residuals

Post-adversarial refresh on 2026-07-10 scanned 34 session files with 179,921
records, 26 project roots with 40,841 files, 146 memory files, and 273 skill files.
There were 175 active skill files, no invalid frontmatter, no mojibake suspects,
and no duplicate-name conflicts. The local/shared portfolio contains 78 governed
entries: 35 active, 35 reference, and 8 candidate, with zero active entries lacking
usage evidence.

The new adversarial layer addresses the two largest historical failure categories:
skill-not-applied and verification/truth gaps. It does not rewrite old session
counts; it adds route-entrypoint proof and blind live-behavior evidence for future
work.

- 43 exact memory-duplicate groups remain because export mirrors duplicate the
  authoritative notes. Indexing must treat `extensions/ad_hoc/notes` as authority;
  physical deletion requires explicit approval.
- Nine older memory files lack explicit scope metadata. They were not rewritten;
  the new superseding correction defines their current boundaries.
- Nine external Open Design adaptations and Caveman Help lack upstream metadata, so
  their update status is unknown. Huashu v2.0 is the only externally adapted design
  skill currently proven up to date.
- `agent-browser` 0.25.4 -> 0.31.1 and `mcporter` 0.10.2 -> 0.12.3 were not updated
  because these are compatibility-relevant pre-1.0 jumps.
- The current export passes the corrected safety scanner. Already-published Git
  history can still contain values from older commits, so this batch uses the user's
  explicit approval for a one-time clean root-history push followed by a fresh-clone
  verification. Automatic weekly sync must never rewrite history.
- Four-lane design and Feishu sync route tests passed but consumed large contexts;
  they remain explicit-only workflows.
- PowerShell shell-snapshot, invalid UTF-8 from two MCP subprocesses, and MCP
  shutdown handshake warnings remain runtime issues. VPN/remote compact disconnects
  were not reproduced or fixed by this skill audit.

## Evidence Files

- `tools/audit_codex_system.py`
- `tools/audit_skill_usage.py`
- `tools/check_evolution_contracts.py`
- `tools/check_export_safety.py`
- `tools/run_skill_route_evals.py`
- `memories/vault_summaries/skill-change-manifest-2026-07-10.md`
- `memories/vault_summaries/evolution-mechanism-manifest-2026-07-10.md`
- local private aggregate audit and route-evaluation JSON files

Git publication remains a separately verified step: safety scan, reviewed staged
tree, one clean root commit, force-with-lease, fresh clone, and repeat validation.
