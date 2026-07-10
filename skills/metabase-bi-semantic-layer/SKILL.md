---
name: metabase-bi-semantic-layer
description: Use when answering or implementing data work for the user's self-hosted Metabase BI workspace, including bi_codex tables, ods_/mart_ modeling, Excel file imports, report metric definitions, filters, permissions, data-quality checks, and reconciliation between old/new Metabase reports.
---

# Metabase BI Semantic Layer

Use this skill before planning, changing, validating, or explaining reports in the user's self-hosted Metabase workspace.

## Start Here

1. Read `references/semantic-layer.md`.
2. For Excel or periodic file imports, also read `references/excel-import-rules.md`.
3. For permission-sensitive partner or external reports, also read `references/permissions-and-audit.md`.
4. Use the cited source inventory and evidence as source-selection guidance, not as a substitute for live DB/API checks.

## Operating Rules

- Treat `bi_codex` as the reporting database. Developer-synced source tables and Excel-import tables both land there before Metabase reads them.
- Prefer raw immutable import/source tables plus explicit `mart_*` reporting tables or views over one-off SQL hidden only inside a Metabase card.
- Verify metric grain, business date, filters, and permissions before saying a report is correct.
- Do not blindly copy old Metabase SQL. Old tables are evidence, not authority, when business invariants or confirmed user rules contradict them.
- Keep the Feishu field/rules document synchronized when report definitions, import rules, permissions, or metric formulas change.

## References

- `references/semantic-layer.md`: canonical reporting, metric, table, filter, and workflow rules.
- `references/excel-import-rules.md`: how periodic Excel files should be staged, audited, loaded, refreshed, and validated.
- `references/permissions-and-audit.md`: external partner permissions, All Users risks, guard triggers, and audit expectations.
- `references/source-inventory.md`: sources checked, coverage level, and update boundaries.
- `references/evidence.md`: source-backed evidence register and known gaps.
