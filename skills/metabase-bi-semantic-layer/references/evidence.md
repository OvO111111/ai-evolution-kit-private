# Evidence Register

| Fact Or Claim | Source Type | Source Link Or Path | Retrieved Or Observed | Confidence | Notes |
| --- | --- | --- | --- | --- | --- |
| Operating reports default to latest 30 calendar days including today | Local/Feishu glossary | `metabase_field_glossary_v4_business_formulas.md`; Feishu doc `<PRIVATE_FEISHU_DOC_ID>` | 2026-06-15 | High | User changed rule from prior yesterday-ended logic to including today |
| Totals must recompute rates from summed numerators and denominators | Local/Feishu glossary | `metabase_field_glossary_v4_business_formulas.md` | 2026-06-15 | High | Applies to all operating tables with `合计` row |
| `tengwei / 验收页` is internal test traffic excluded from operating reports | Local/Feishu glossary and scripts | `exclude_tengwei_from_reports.py`; glossary | 2026-06-15 | High | Source rows are not physically deleted |
| Old Metabase SQL is not automatically authoritative | Local glossary and incident history | `metabase_field_glossary_v4_business_formulas.md` | 2026-06-15 | High | Use business invariants and live checks |
| Partner permissions require hard guards | Permission SQL and incident docs | `ops/bi_metabase_permission_guard.sql`; `ops/protect_partner_forbidden_membership.sql`; Feishu incident update | 2026-06-15 | High | Trigger and cron were verified after incident |
| Excel imports should land in `bi_codex` before Metabase reads them | User requirement plus semantic design | Current conversation and this semantic layer | 2026-06-15 | Medium | Needs first real Excel file to finalize table schema |
| 250,000 rows is operationally manageable for MySQL-backed import | Engineering judgment | Current environment and import rules | 2026-06-15 | Medium | Actual performance depends on file shape, indexes, and load method |
