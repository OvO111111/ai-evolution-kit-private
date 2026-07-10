# Evolution Mechanism Manifest 2026-07-10

## Intake Contract

`absorb-lessons` now requires:

1. obtain and identify the real source;
2. define the improvement target;
3. map every affected sibling skill, router, automation, memory boundary, export
   rule, and test;
4. deduplicate against current capabilities;
5. classify adopt, adapt, candidate, reference, reject, or no-change;
6. record a failing baseline and a post-change behavioral test;
7. produce an exact change manifest and residual-risk list.

A source URL is acquired through `web-access` and a source-owning tool such as
GitHub. Installation is not an intake default.

## Inventory And Evidence

| Mechanism | Previous problem | Current behavior |
|---|---|---|
| `audit_codex_system.py` | No repeatable full-history/project/memory/skill integrity scan | Scans locally discoverable sessions, projects, memories, skills, and automations; reports aggregate evidence without copying content |
| `audit_skill_usage.py` | O(records x skills), timed out after 124 seconds, hard-coded old report date | One-pass alias/path index, current dated reports, complete 77-skill table, evidence counts, tier, path, and `openai.yaml`; completes in about 24 seconds |
| `skill-portfolio.jsonl` | 62 stale entries, old fallback names active, Agent Reach duplicate, new skills unknown | 78 classified entries after adversarial review: 35 active, 35 reference, 8 candidate; zero active item without read/assistant/tool evidence |
| `skill-trigger-tests.jsonl` | Expected local PDF as active and did not reflect official-first routing | Legacy fallback test is explicit; official behavior is tested in fresh sessions |
| `check_external_skill_updates.py` | Upstream metadata format conflicted with current skill validator | Reads legal nested `metadata` and still verifies Huashu v2.0; missing metadata remains `needs_metadata` |
| `check_export_safety.py` | Public export already contained personal paths, Feishu document/board identifiers, a private host, and company contact values | Scans tracked and untracked export candidates and fails closed without printing the sensitive value |

## Validation Layers

| Layer | Purpose | Current result |
|---|---|---|
| skill validator | syntax/frontmatter validity | all changed maintained skills pass |
| `check_evolution_contracts.py` | durable scope, fallback, web, dashboard, design, evolution, report-completeness, and export-safety contracts | expanded from 15 to 30 checks, zero failures |
| `check_skill_routing.py` | portfolio/test consistency | zero failures; active budget scales with portfolio instead of a stale fixed 30 |
| `run_skill_route_evals.py` | fresh GPT-5.6 behavioral route proof | 26 core cases pass; one is explicitly degraded because preferred remote Data Analytics was unavailable |
| live callable smoke | distinguish installed files from usable capability | Chrome, Computer Use, and Lark routes tested through live clients/CLI |

## Route-Evaluation Safety

The route evaluator previously launched several `codex exec` processes in parallel.
They share `models_cache.json` and plugin caches, which caused a JSON read/write race
and false runtime failures. The evaluator now forces one worker by default. Parallel
execution requires explicit `--allow-parallel` and is not used by automation.

The evaluator records separate states:

- `passed`: required route selected;
- `degraded`: safe fallback selected but preferred plugin missing;
- `failed`: wrong route, forbidden route, invalid output, timeout, or nonzero process;
- `preference_misses`: exact preferred skill not selected;
- stderr signals: catalog, model refresh, stream, MCP, or tool failures kept as
  evidence rather than silently discarded.

Full dynamic regression is reserved for major model or routing changes. Weekly
maintenance runs static checks plus only the affected route cases.

## Capability Refresh

The weekly capability refresh automation now:

- snapshots exact Codex/plugin/Lark/external-skill versions;
- checks external metadata honestly;
- runs static evolution contracts and portfolio tests;
- runs only affected dynamic cases, sequentially;
- reports exact changed skills, old/new behavior, reason, test, and residual;
- distinguishes route failure, degraded fallback, plugin unavailability, and network
  or catalog failure;
- keeps backup push separate in `weekly-evolution-sync`.

All automations use `gpt-5.6-sol` with high reasoning. The Metabase automation reads
its project-local handoff and scripts rather than embedding server addresses,
credentials, card IDs, or volatile business rules.

## Memory And Export

- New correction notes supersede conflicting old global guidance without rewriting
  historical evidence.
- Company H5/project patterns remain company-scoped and cannot become generic defaults.
- `extensions/ad_hoc/notes` is authoritative over export mirrors.
- Public export receives only portable skills, aggregate evidence, tests, and
  redacted manifests. Exact prices, contacts, company subjects, document tokens,
  local source paths, account state, chat bodies, customer/payment data, and browser
  details are excluded.
- The weekly sync must pass `check_export_safety.py` before staging. A finding blocks
  commit and push.
- GitHub push remains a separate account action; this correction updates the local
  export repository but does not push it automatically.

## Adversarial Evidence Upgrade

- Route tests now support ordered semantic aliases and can require that selected workflow entrypoints were actually opened. This prevents name-only routing claims.
- High-impact evolution adoption now receives a red-team falsification gate before broad defaults or routing are changed.
- Before/after evaluation is blind: the evaluator gets the natural request and acceptance contract, not the suspected defect, intended answer, change diff, or author reasoning.
- Route selection, static contracts, artifact quality, and live behavior are reported as separate evidence tiers.
- A controlled H5 fixture now proves the outside-in loop: five seeded defects found, one additional browser-history defect found after initial fixes, and a final fresh zero-finding pass.
- Heavy black-box review is confined to meaningful confirmation/release gates because measured runs took several minutes; the low-risk non-trigger control passed.
- Public export is now a curated projection rather than a raw mirror. A real raw-copy regression produced 25 safety findings and was blocked before staging; sanitized placeholder projections returned zero findings. Weekly sync explicitly forbids recursive overwrite of project-derived/private-context skills.
- Export safety now recognizes Windows paths in normal text and JSON/JSONL escaped form. The stronger rule exposed 316 historical personal-path findings across four artifacts; obsolete/private-project reports were removed, the portfolio was made portable, and the final 286-file scan returned zero findings.
- Cross-machine restore now installs public project-skill projections only when absent. A temporary-home smoke test proved first install succeeds and a second run preserves an existing private/full local skill instead of overwriting it.

The current user explicitly approved a one-time safe export sync and public-history cleanup after these checks. This is separate from unattended weekly capability refresh behavior.

## Remaining Mechanism Limits

- Remote plugin catalog/model refresh is slow and intermittently returns EOF or
  timeout errors in fresh CLI sessions.
- Data Analytics `build-dashboard` could not be proven in the independent CLI route
  test even though the app inventory exposes Data Analytics 0.2.6. The fallback is
  reported as degraded, not normal success.
- Dynamic route testing is expensive: complex design/dashboard cases can exceed
  300k input tokens. It is targeted, not run indiscriminately.
- Nine external adapted skills still lack upstream metadata.
- Physical memory-mirror deletion and broad plugin disabling require a separate
  explicit decision because they remove history or capability.
