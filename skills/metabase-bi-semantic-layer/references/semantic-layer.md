# Metabase BI Semantic Layer

## Quick Reference

- Area: Self-hosted Metabase BI, `bi_codex`, developer-synced source tables, and periodic Excel-import reporting.
- Intended users: Codex agents implementing or validating reports for internal operations and controlled partner-facing subsets.
- Coverage level: Strong for current report rules and permission guardrails; Directional for future Excel imports until real files are inspected.
- Source inventory: `references/source-inventory.md`
- Last synthesized: 2026-06-15
- Freshness expectations: developer-synced `ods_*` tables are expected to be near 5-minute delayed; `mart_*` tables may refresh less frequently and must be checked before being used for current-day reporting.
- Default date and time zone rules: Asia/Shanghai. Operating reports default to the latest 30 calendar days including today: start date = today - 29 days, end date = today. Order search defaults to a shorter recent window when performance requires it.

## Entity Clarification

| Entity | Means | Does Not Mean | Primary IDs | Grain Notes | Sources |
| --- | --- | --- | --- | --- | --- |
| Developer-synced source table | Tables copied into `bi_codex` on a schedule, usually named `ods_*` | A guaranteed canonical metric table | Table name and source business keys | Preserve source grain; do not mutate source rows for reporting convenience | `metabase_daily_consistency_check.py`, source inventory |
| Excel-import source table | Periodic user/developer-provided file data loaded into `bi_codex`, usually `ods_file_*` or `ods_excel_*` | A manual Metabase upload or one-off spreadsheet view | Import batch, source file hash, source row number, business key | Preserve raw file rows; clean into `mart_*` only after validation | `excel-import-rules.md` |
| Reporting mart | Query-friendly table or view used by Metabase, usually `mart_*` | The only source of truth if it cannot be reconciled to source tables | Business date, dimensions, business keys | Materialize when performance or repeatability requires it | Local report scripts, audit scripts |
| Metabase card | Saved question/report in Metabase | A safe source of truth by itself | Card ID, collection ID, source card ID | Card SQL may contain business logic; inspect before reusing | Metabase app DB, local scripts |
| Partner report | A controlled subset for external partner viewing | A normal internal report with filters hidden by UI only | Partner group, collection, fixed channel/product filters | Must be fixed at SQL/permission layer, not only by visible filters | `permissions-and-audit.md` |

## Key Metrics And Report Rules

| Metric Or Rule | Definition | Numerator | Denominator | Time Grain | Canonical Source | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| 合计行 | First row summarizing the current filter range | Sum base counts/amounts first | Recompute rates from summed numerator/denominator | Current filter range | Field glossary v4 | Never sum or average daily rates directly |
| 日维度流水数据表 | Daily event/transaction view | Count or sum events by business occurrence date | Not applicable unless rate fields exist | Day | Field glossary v4 and card SQL | No color blocks by default |
| 用户质量表 | Cohort view by signing/low-deduction date | Cohort outcomes within same day or 30-day windows | Cohort base or confirmed metric denominator | Signing date or low-deduction date | Field glossary v4 | 30-day windows can continue changing |
| 当日退费 | Refund whose refund-success time falls on the same relevant business day | Same-day refund count or amount | The confirmed base for that table | Event day or cohort day | Field glossary v4 | Do not use eventual refund amount without refund-success time |
| 30日内退费 | Refund whose refund-success time falls in 0-30 days after the cohort event | 30-day refund count or amount | The confirmed base for that table | Cohort day | Field glossary v4 | Refund cannot exceed cancellation in same event window unless source rows are missing or formula is wrong |
| 后置扣费 | 30-day post-signing successful deduction minus same-day successful deduction where that business definition applies | Later successful deductions in 30-day window | Cohort base or postpaid base depending field | Cohort day | Field glossary v4 | Title should explicitly include `签约30日内` when the window is 30 days |
| Excel imported rows | Rows successfully loaded from a file | Database imported row count | Excel expected row count | Import batch | `excel-import-rules.md` | Must reconcile row count before report use |

## Standard Filters And Dimensions

| Filter Or Dimension | Default Logic | Override When | Applies To | Sources |
| --- | --- | --- | --- | --- |
| Date filters | Start date first, end date second; default latest 30 calendar days including today for operating reports | Order search and other operational tools may use shorter defaults for performance | All reports | Field glossary v4 |
| Product filters | Show Chinese business names, not raw codes, where mapping exists | Raw IDs may be exposed only in internal debug or unresolved mapping workflows | Operating reports | Field glossary v4, mapping scripts |
| Channel filters | Show Chinese channel names, exclude `tengwei / 验收页` from operating reports | Source-level troubleshooting may inspect excluded rows | Operating reports | Field glossary v4 |
| Activity product | Use separate field/value domains when normal and high-low products share base IDs but differ by `contentid` | Do not merge high-low and normal products into one filter if definitions differ | 沃橙支付宝 | High-low update scripts and Feishu updates |
| Partner fixed channel | Partner reports fix sensitive dimensions in SQL and hide corresponding filters | Never rely on hidden UI filters alone for external access | Partner reports | Permission incident docs |

## Key Tables

| Table | When To Use | Grain | Join Keys | Freshness | Caveats | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| `ods_*` | Developer-synced raw/reporting source tables | Source-defined | Source business keys | Expected near 5-minute delayed for critical tables | Validate row count/update time before current reporting | `metabase_daily_consistency_check.py` |
| `ods_wc_lxby_callback` | 沃橙 callback-derived metrics and daily flow | Callback/payment/refund event rows | `ordernumber`, `agreementno`, `customerid`, `productid`, `contentid` depending business line | Critical table, checked by daily script | Use business event times, not `created_at`, for经营 dates | Field glossary v4 |
| `ods_wc_lxby_order_form` | 沃橙 order-form support and mapping | Order rows | Order number and product keys | Critical table, checked by daily script | Historically had sync-zero risk, keep checking | Daily script |
| `mart_wc_alipay_highlow_contract` | 高低扣 user-quality cohort reporting | Low-deduction order / contract-derived rows | `agreementno + contentid` and order keys | Refreshed by mart process | Low deduction is the cohort base; high deduction and renewal are later events | High-low scripts |
| `v_order_search` | Internal order detail lookup | Order row | Order ID, phone, transaction IDs, product/channel names | Depends on source tables | Must not use SQL `LIMIT 1000` if user requires full matching result | Order-search Feishu update |
| `ods_file_*` / `ods_excel_*` | Future periodic Excel sources | Raw file row plus import batch | File hash, row number, business key | On file arrival | Must not be queried by final reports until validation passes | `excel-import-rules.md` |
| `mart_file_*` / business `mart_*` | Cleaned file-derived reporting table | Business-defined | Confirmed business key and date | Refreshed after import validation | Create only after update mode is known | `excel-import-rules.md` |

## Query Patterns

- Pattern: Build an operating report from developer-synced tables
  - Use when: The source is maintained by developers and refreshed into `bi_codex`.
  - Key tables: `ods_*`, optionally `mart_*`.
  - Required filters: business date range, product/channel mappings, internal-test exclusion when applicable.
  - Common joins: dimensions/mappings for product and channel names.
  - Example skeleton: source CTE -> daily CTE -> totals CTE -> union `合计` plus daily rows.

- Pattern: Build a report from an Excel file
  - Use when: The source is a periodic file instead of a 5-minute synced table.
  - Key tables: `ods_file_<area>_raw`, `etl_file_import_batch`, `mart_file_<area>`.
  - Required filters: `import_batch_id`, business date, validation status, and update mode.
  - Common joins: optional mapping tables to convert codes to Chinese names.
  - Example skeleton: load raw batch -> validate -> publish current mart -> Metabase reads mart.

- Pattern: Create a partner-facing controlled copy
  - Use when: External partner should see a restricted report.
  - Key tables: same source/mart as internal report, but SQL fixed to allowed partner dimensions.
  - Required filters: hidden sensitive dimensions must be fixed in SQL; partner group must not have data/query permissions.
  - Common joins: none beyond internal source unless needed for labels.
  - Example skeleton: source card -> derived card with fixed predicate -> partner collection -> permission audit -> negative test.

## Gotchas

- Gotcha: `All Users` is inherited by every Metabase account.
  - Impact: Any business collection or root permission on `All Users` can leak internal reports to external users.
  - How to avoid: Keep `All Users` out of business collections; grant internal access through explicit internal groups only.
  - Source: Permission incident docs and guards.

- Gotcha: `非管理员活跃用户` is not the same as internal staff.
  - Impact: Bulk-adding non-admin users to internal groups can leak data to partners.
  - How to avoid: Use explicit group membership and the database hard-block trigger.
  - Source: 2026-06-15 permission incident.

- Gotcha: Old SQL may encode wrong business logic.
  - Impact: Replicating old tables can perpetuate errors such as refund/cancel window mistakes.
  - How to avoid: Check business invariants, event-time windows, and current Feishu definitions before reusing SQL.
  - Source: Field glossary v4 and incident notes.

- Gotcha: Excel imports without a batch and file hash cannot be audited.
  - Impact: Duplicate or partial imports look like real metric changes.
  - How to avoid: Always store batch metadata, row count, source row number, and hash.
  - Source: `excel-import-rules.md`.

## Related Dashboards And Docs

| Source | Use It For | Caveats |
| --- | --- | --- |
| Feishu field/rules document | Human-facing latest report formulas and operating principles | Must be synchronized after changes |
| `metabase_field_glossary_v4_business_formulas.md` | Local source-backed copy of report definitions | May lag Feishu append-only updates |
| `metabase_daily_consistency_check.py` | Operational regression checks | Add checks when creating new rule classes |
| Metabase app DB | Current card SQL, parameters, collections, permissions | Requires careful writes; prefer API/scripts and backups |

## Open Questions

- Question: What is the first concrete Excel file's business area, update mode, and unique key?
  - Why it matters: Determines whether to overwrite, append, upsert, or replace date partitions.
  - Best owner or source to check next: User-provided Excel file and business owner explanation.

- Question: Should Excel imports be triggered manually by Codex, by a server watch directory, or by a developer-owned job?
  - Why it matters: Determines automation, error reporting, and permission boundaries.
  - Best owner or source to check next: User and developer deployment decision.
