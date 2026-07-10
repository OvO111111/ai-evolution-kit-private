---
page_type: decision
created_at: "2026-05-22"
updated_at: "2026-05-22"
sensitivity: personal
source_ids: ["sensenova_skills_article", "sensenova_skills_repo", "user_data_report_quality_feedback"]
confidence: high
status: active
---

# Data Analysis Report Standard

## Decision

Professional data analysis reports need a dedicated workflow. `xlsx` can process files, but it does not by itself enforce decision framing, evidence synthesis, report structure, or final deliverable quality.

Created `data-analysis-report` as the mandatory routing skill for data analysis reports, Excel/CSV analysis, KPI/trend/comparison/cohort/root-cause reports, visualized HTML reports, Word/PPT analysis reports, and feedback that an analysis report is not professional enough.

## Adopted From SenseNova-Skills

Useful ideas:

- Treat data analysis as an end-to-end office workflow, not a single pandas script.
- Start with data profiling, schema alignment, cleaning, aggregation, and export discipline.
- For large Excel, count rows first and switch to Parquet/streaming patterns instead of blindly loading the file.
- Combine data analysis with research when explanation or external benchmark evidence is needed.
- Use report-format discovery before writing when the report type is unclear.
- Deliver in the right artifact format: Excel for auditability, HTML for browsable visual reports, Word/Markdown for reading, PPT for meeting communication.
- Quality checks must cover both data correctness and communication quality.

Rejected / deferred:

- Do not install all SenseNova skills as default. The local skill surface is already large.
- Do not depend on SenseNova API/runtime for basic report quality.
- Do not copy its full implementation. Absorb the workflow standard and keep local tools as the execution layer.

## Professional Report Bar

- The report must answer the user's decision question first.
- Data inventory must include sources, row counts, date ranges, grain, key fields, missingness, duplicates, and metric definitions.
- Findings must be ranked by business impact and tied to evidence.
- Charts need units, denominators, readable titles, and a stated decision purpose.
- Separate fact, interpretation, recommendation, uncertainty, and next monitoring action.
- Technical proof such as tests, endpoints, files, and screenshots is evidence only; it is not the report headline.

## Validation

Added a trigger case for `data_analysis_report` to the skill routing harness. Current expected route is:

- primary: `data-analysis-report`
- support: `xlsx` when Excel/CSV files are involved
