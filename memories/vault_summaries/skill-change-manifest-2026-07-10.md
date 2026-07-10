# Skill Change Manifest 2026-07-10

This is the exact portable change list for the GPT-5.6 system correction. It does
not include project data, chat bodies, credentials, account state, or private browser
details.

## Workflow And Routing Rewrites

| Skill | Previous problem | New behavior | Behavioral evidence |
|---|---|---|---|
| `absorb-lessons` | Could improve only the named example and omit affected siblings or a concrete report | Requires real source acquisition, impact map, before/after test, and exact change manifest | `evolution_intake` passed with `absorb-lessons` + `web-access` |
| `web-access` | Old CDP-heavy body could bypass official GitHub, Chrome, Browser, and Playwright ownership | Explicit route order for connectors, GitHub, static web, Chrome, in-app Browser, Playwright, Agent Reach, and CDP fallback | GitHub, login-state Chrome, in-app Browser, public WeChat, evolution URL cases passed |
| `ui-product-design-router` | Generic H5 and company H5 could leak into each other; focused Product Design skills were not guaranteed | Separates company scope, generic Product Design, admin, redesign, visual, and four-lane comparison paths | Generic H5, company H5, admin, dashboard, and four-lane cases passed |
| `app-factory-h5-admin` | Declared itself the default for every H5 and could write admin/PRD too early | Company/work only; analysis -> H5 review -> admin review -> PRD | Company H5 ordering case passed; generic H5 excludes it |
| `admin-platform-execution-gate` | Hard stop, fixed dark/Linear-like template, and planning-only completion | Short product/state/permission/visual contract followed by same-stage implementation | Admin redesign and dashboard fallback cases passed |
| `pm-prd` | One-question turns and PRD drafting before source truth | Source-first context packet, one compact question batch, end-to-end continuation | PRD source-gate case passed |
| `agent-reach` | Broad default, cookie-import guidance, and account-action risk | Platform-specific public/social/article escalation after normal web access; no cookie import or account actions by default | Public WeChat article case passed |
| `data-analysis-report` | Swallowed dashboard construction and referenced old local Office skills as defaults | Explicit report-only boundary; dashboards/KPI/data quality/notebooks defer to focused Data Analytics routes; official Office plugins preferred | Analysis report passed; dashboard excludes this skill and uses a degraded visualization fallback when Data Analytics is unavailable |
| `huashu-design` | Triggered on any ugly-UI complaint and had invalid upstream frontmatter | Explicit Huashu/high-fidelity lane only; upstream metadata moved under valid `metadata` | Validator passed, v2.0 upstream check passed, four-lane case passed |
| `open-design-design-systems` | Triggered on any request for a beautiful UI or admin complaint | Explicit Open Design/design-system/reference-benchmark lane only | Four-lane case passed; generic H5 excludes it |
| `design-taste-frontend` | 1,200-line entrypoint inflated context and mixed many frontend situations | Concise public/landing/editorial lane with full guide behind `references/` | Four-lane case passed |
| `playwright` | Could consume ordinary public browsing | Limited to local/dev-server, reproducible UI flow, DOM debugging, and screenshot regression | In-app Browser case excludes Playwright and passes |

## Official-First Legacy Fallbacks

All of these now have distinct fallback names and
`policy.allow_implicit_invocation: false`.

| Skill folder | New skill name | Official default | Evidence |
|---|---|---|---|
| `image-to-code` | `image-to-code-fallback` | `product-design:image-to-code` | Generic H5 and four-lane tests exclude the fallback |
| `pdf` | `pdf-legacy-fallback` | `pdf:pdf` | Official PDF case passed |
| `xlsx` | `xlsx-legacy-fallback` | `spreadsheets:Spreadsheets` | Analysis-report and official spreadsheet routes passed |
| `docx` | `docx-legacy-fallback` | `documents:documents` | Official Word case passed |
| `pptx` | `pptx-legacy-fallback` | `presentations:Presentations` | Official presentation case passed |
| `browser-harness` | `browser-cdp-fallback` | official Chrome, in-app Browser, or Playwright | Chrome and in-app Browser cases passed |
| `desktop-control` | `desktop-control-fallback` | `computer-use:computer-use` | Windows Excel case passed |

## Trigger Metadata Added

These maintained local skills received explicit `agents/openai.yaml` display,
default-prompt, and implicit-invocation policy metadata. Their domain boundaries
remain in `SKILL.md`.

| Skill | Scope |
|---|---|
| `data-analysis-report` | explicit analysis-report artifact |
| `web-access` | access-layer routing |
| `huashu-design` | explicit high-fidelity visual lane |
| `open-design-design-systems` | explicit reference-backed design-system lane |
| `redesign-existing-projects` | source-first redesign of an existing product |
| `wechat-pay-product-design` | current WeChat Pay product/operations guidance |
| `ocr-and-documents` | scans and document-image OCR |
| `video-frames` | ffmpeg frame extraction |
| `diagram-drawing-router` | diagram artifact and technology selection |
| `wechat-work-context` | read-only, allowlisted, group-isolated WeChat work context |
| `playwright` | terminal browser verification |
| `metabase-bi-semantic-layer` | matching self-hosted Metabase project only |

## Duplicate And Reference Copies

| Skill copy | Change |
|---|---|
| shared `.agents/skills/agent-reach` | Renamed `agent-reach-upstream-reference`; implicit invocation disabled |
| project `cavecrew` | Renamed project reference; implicit invocation disabled |
| project `caveman` | Renamed project reference; implicit invocation disabled |
| project `caveman-commit` | Renamed project reference; implicit invocation disabled |
| project `caveman-compress` | Renamed project reference; implicit invocation disabled |
| project `caveman-help` | Renamed project reference; implicit invocation disabled |
| project `caveman-review` | Renamed project reference; implicit invocation disabled |
| project `caveman-stats` | Renamed project reference; implicit invocation disabled |

## Updated But Not Manually Rewritten

- Lark CLI and 27 official Lark skills were synchronized from 1.0.65 to 1.0.68.
  Wrapper safety and auth/docs/drive/whiteboard routes were smoke-tested.
- Official Documents, PDF, Presentations, Spreadsheets, and Template Creator moved
  from 26.630.12135 to 26.709.11516. Local legacy skills were demoted instead of
  modifying official plugin content.
- Product Design 0.1.50, Data Analytics 0.2.6, Chrome/Browser/Computer Use
  26.707.31428, and GitHub were tested or capability-inventoried without rewriting
  vendor files.

## Deliberately Not Changed

- The eight Open Design adaptations remain candidates or one explicit active design
  system lane. Missing upstream metadata prevents honest update claims.
- Official Lark skill bodies were not given local `openai.yaml` files because the
  CLI updater owns and may replace them.
- Data Analytics `build-dashboard` is preferred, but it was unavailable in the
  independent CLI route session. The tested degraded route used UI/product routing,
  admin execution gate, and bundled `visualize`; this remains reported as degraded.
- Memory mirror duplicates were indexed as non-authoritative but not physically
  deleted without explicit permission.

## Adversarial Review Addition

| Skill | Exact change | Evidence |
|---|---|---|
| `adversarial-review` | New two-mode skill for blind live-product walkthroughs and consequential-plan red-team review; explicitly excludes routine reversible work. | `quick_validate.py` pass; fresh route and live browser behavior tests pass. |
| `app-factory-h5-admin` | Added conditional pre-build red team, blind H5 checkpoint, blind operator checkpoint, same-journey retest, and real 375/390px mobile verification while preserving company-only scope. | Company route and H5-checkpoint fresh sessions passed and opened required skills. |
| `project-prd-h5-audit` | Readiness claims now require live black-box evidence when a runnable H5/admin exists; the audit remains read-only. | Static contract pass. |
| `pm-prd` | Added conditional red-team mode for high-cost, hard-to-reverse, compliance-sensitive, or repeated plans; routine reversible work is excluded. | Red-team route pass; low-risk non-trigger pass. |
| `absorb-lessons` | Added red-team adoption, blind before/after tests, and separate route/static/artifact/live evidence tiers. | Red-team route pass; 33 evolution contracts pass. |

Global `AGENTS.md` was deliberately left unchanged; routing and detailed procedures live in skill metadata and bodies.
