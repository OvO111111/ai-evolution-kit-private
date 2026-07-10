# Excel Import Rules

Use these rules for periodic Excel/CSV sources that should feed Metabase reports.

## Core Decision

Do not make Metabase read Excel directly. Load every file into `bi_codex`, validate it, then expose a clean table or view to Metabase.

## Required Questions Per File Type

Answer these before creating the final report:

| Question | Why It Matters |
| --- | --- |
| Is the file full refresh, append-only, upsert by key, or date-partition replacement? | Determines delete/insert strategy and whether old rows survive |
| Which sheet is authoritative? | Avoids loading summary or hidden sheets by mistake |
| What is the business primary key? | Prevents duplicate metrics and supports upserts |
| What is the business date column? | Controls default date filters and partition replacement |
| Which columns are dimensions, amounts, statuses, and identifiers? | Controls Metabase filters and field types |
| Does the file include sensitive personal or payment data? | Controls masking, partner access, and export permissions |

## Table Pattern

Use this table pattern unless there is a strong reason not to:

| Layer | Naming | Purpose |
| --- | --- | --- |
| Import batch log | `etl_file_import_batch` | One row per file import, with file name, file hash, expected rows, loaded rows, status, and error summary |
| Raw file table | `ods_file_<area>_raw` or `ods_excel_<area>_raw` | Preserve rows exactly enough to audit the file |
| Clean/current table | `mart_file_<area>` or business `mart_*` | Typed, deduped, report-ready rows |
| Optional mapping table | `dim_<area>_*` | Code-to-Chinese-name mappings or static dimensions |

## Required Audit Columns

Every raw file table should include:

| Column | Meaning |
| --- | --- |
| `import_batch_id` | Batch ID linking rows to the file import log |
| `source_file_name` | Original file name |
| `source_file_hash` | Hash of file content to detect duplicate imports |
| `source_sheet_name` | Excel sheet name |
| `source_row_number` | Original row number in the file |
| `imported_at` | Import timestamp |
| `raw_payload` | Optional JSON copy of the raw row when schema drift is likely |

## Update Modes

| Mode | Use When | Safe Load Strategy |
| --- | --- | --- |
| Full refresh | Each file contains the complete current dataset | Load into staging, validate row count, replace current table in one transaction |
| Append-only | Each file contains new rows only | Insert only unseen business keys or unseen file rows; fail on unexpected duplicates |
| Upsert by key | File can correct prior rows | Load staging, validate, then update/insert by confirmed key |
| Date partition replacement | File covers one or more business dates | Delete only those dates from current table, then insert validated rows |

Never guess the mode from row count alone. If the mode is not known, import into raw/staging only and ask for confirmation before publishing to `mart_*`.

## Validation Gate

Before Metabase uses the import, verify:

- File can be opened and the intended sheet is selected.
- Header names are stable or mapped explicitly.
- Expected rows equal loaded rows.
- Critical columns are not unexpectedly null.
- Business date range is plausible.
- Amount fields parse to the intended unit.
- Duplicate key behavior matches the selected update mode.
- Row-level errors are recorded with enough detail to fix the source file.
- Import batch status is `validated` or `published`, not `loaded_only` or `failed`.

## 25 万 Row Practical Rule

250,000 rows is manageable. Prefer converting Excel to CSV/parquet-like local staging and bulk-loading into MySQL rather than row-by-row inserts. If formulas, merged cells, hidden rows, or multiple sheets exist, inspect them before bulk load.

## Metabase Exposure

- Metabase should read clean `mart_*` or validated current views by default.
- Raw `ods_file_*_raw` tables are for audit/debug, not normal operations views.
- Field names shown to users should be Chinese or clear business names.
- Add dropdown mappings only after the imported values are validated and stable.
- Partner-facing copies require separate collections and permission tests.

## Failure Handling

- Duplicate file hash: do not re-import unless explicitly forced.
- Partial load: mark batch failed and do not publish to mart.
- Schema drift: keep raw file, record missing/new columns, and ask for mapping.
- Ambiguous update mode: stop before replacing current reporting data.
- Sensitive data: do not expose to external partner reports without a separate controlled copy.
