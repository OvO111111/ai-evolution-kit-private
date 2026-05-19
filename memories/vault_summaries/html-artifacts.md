---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-18"
sensitivity: personal
source_ids: ["html_first_class_note", "html_artifact_trend_research"]
confidence: high
status: active
---

# HTML Artifacts

## Current Assessment

HTML is not just a prettier replacement for Markdown. The current AI-agent interest comes from HTML acting as a browser-native artifact runtime: layout, diagrams, tables, controls, timelines, dashboards, and local interactivity in a portable file.

## Use HTML When

- information is spatial, comparative, visual, or interactive
- a reviewer needs to inspect a system instead of reading a wall of text
- a report benefits from filters, tabs, charts, timelines, or collapsible evidence
- an AI-generated tool should be opened directly in a browser
- a work product needs to be shared as a self-contained artifact

## Use Markdown When

- the content is a durable text source of truth
- humans need clean diffs and co-editing
- the file is a rule, runbook, spec, decision, or long-term source summary
- the output should be easy to review in git

## Knowledge Vault Roles

- `source_html`: original captured HTML with metadata and hash.
- `compiled_html`: generated report/view derived from raw/wiki/data; not ground truth.
- `interactive_html`: task-specific browser workspace; must export state to JSONL or Markdown.

## Risks

HTML can hide complexity, create false confidence through polished design, produce noisy diffs, load external resources, or run JavaScript. Generated HTML must remain local, cited, and inspectable.
