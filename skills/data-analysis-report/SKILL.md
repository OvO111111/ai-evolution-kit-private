---
name: data-analysis-report
description: "Create, review, or improve professional data analysis reports from Excel/CSV/files, dashboards, business datasets, complaint/customer/payment data, or research-backed quantitative findings. Use when the user asks for data analysis, analysis report, Excel report, business insight report, KPI analysis, trend/comparison/cohort/root-cause analysis, visualized HTML report, Word report, PPT report, or says a data analysis report is not professional enough."
---

# Data Analysis Report

Use this skill to turn raw data into a decision-grade report. The goal is not to prove that code ran; the goal is to answer the business question with traceable evidence, clear judgment, and usable deliverables.

Inspired by the useful parts of OpenSenseNova `SenseNova-Skills`: Excel workflow, report-format discovery, deep-research planning/synthesis, HTML/PPT report delivery, and quality checks. Do not copy or depend on its runtime by default.

## Mandatory Gate

This skill is mandatory when the user asks for:

- data analysis report, Excel analysis, business analysis, KPI report, trend/comparison/cohort/root-cause analysis
- report based on `.xlsx`, `.xls`, `.csv`, screenshots, charts, dashboards, or multiple files
- visualized HTML report, Word report, PPT report, or "make this analysis professional"
- data-backed PRD/operations/business decision material

Also load the relevant file-format skill as needed:

- `xlsx` for Excel/CSV reading, formulas, workbook outputs, or spreadsheet validation.
- `ocr-and-documents` for screenshots/scans/table OCR.
- `docx`, `pptx`, or presentation skills for final Word/PPT outputs.
- `web-access`/research skills only when external evidence is needed to explain causes or benchmark context.

## Workflow

1. **Define the decision question.** State what decision, diagnosis, or operational action the report must support. Do not start with charts.
2. **Inventory the data.** List files/sheets/tables, row counts, date ranges, key fields, grain, missingness, duplicates, and obvious schema problems.
3. **Build a context packet.** Capture business background, metric definitions, target audience, acceptance criteria, and known constraints.
4. **Prepare the data.** Clean and normalize with an audit trail. For large Excel, count rows first and use Parquet/streaming strategy instead of blindly loading full files.
5. **Analyze by question, not by tool.** Use trend, composition, comparison, cohort, funnel, distribution, outlier, correlation, root-cause, or segmentation analysis only when it serves the decision question.
6. **Separate facts, interpretation, and recommendation.** Every key claim should trace to data, a chart/table, or an external source. Do not mix unsupported guesses into findings.
7. **Create deliverables.** Choose the right output: concise Markdown/Word for reading, Excel workbook for auditability, HTML dashboard/report for browsing, PPT for meetings, infographic only when a compressed visual summary is useful.
8. **Verify.** Check row counts, totals, percentages, chart labels, units, metric definitions, and whether the recommendation follows from the evidence.

## Report Structure

Use this default structure unless the user or domain has a stronger format:

1. **Conclusion First:** one-paragraph answer to the user's question.
2. **What Changed / What Matters:** 3-5 key findings ranked by business impact.
3. **Evidence:** tables/charts with source, metric definition, denominator, unit, date range, and sample size.
4. **Diagnosis:** drivers, segments, exceptions, root causes, and uncertainty.
5. **Recommendation:** actions, owners or decision options, expected impact, risks, and what to monitor next.
6. **Appendix:** data inventory, cleaning notes, assumptions, query/code summary, and reproducibility notes.

## Professional Bar

- Never deliver only descriptive statistics unless the user's task is purely descriptive.
- Never show charts without stating what decision each chart supports.
- Avoid decorative charts. Prefer sorted bars, trend lines, distribution plots, cohort tables, funnel tables, and well-labeled comparison matrices.
- Always include denominators for rates and percentages.
- Always distinguish raw count, rate, average, median, percentile, and share.
- For small or biased samples, say the limitation before making strong claims.
- For multi-file analysis, align schemas and explain joins/union logic.
- For external research-backed analysis, reconcile conflicting numbers instead of picking the first result.
- For final reporting, lead with whether the user's requirement is satisfied and what the user-visible result is. Technical evidence comes after.

## Output Checklist

Before claiming the report is complete:

- [ ] The original business question is answered directly.
- [ ] Data sources, row counts, date range, grain, and metric definitions are visible.
- [ ] Findings are ranked and tied to evidence.
- [ ] Charts/tables have units, denominators, labels, and readable titles.
- [ ] Recommendations are actionable and bounded by uncertainty.
- [ ] Any generated Excel formulas have been recalculated and checked for errors when applicable.
- [ ] Any HTML/PPT/report artifact has been opened or visually checked when feasible.
- [ ] Remaining gaps are stated plainly.
