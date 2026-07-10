# Portable Source Inventory

This exported reference describes source categories and verification order. Exact
server addresses, credentials, document tokens, local project paths, report IDs, and
company data remain in the private project handoff and runtime configuration.

## Required Source Categories

| Source category | Purpose | Preferred access | Update boundary |
|---|---|---|---|
| project handoff and field glossary | current names, formulas, filters, date rules, known incidents | private local project files | update with implementation changes |
| canonical editable business document | human-facing definitions and change log | authenticated Lark document route | verify read-after-write |
| audit and consistency scripts | encoded freshness, permission, filter, and report checks | private local project scripts | extend when rules change |
| live Metabase and reporting database | current schema, row counts, report metadata, and reconciliation | private configured read-only connection | never export endpoints or credentials |
| permission and operational guards | partner isolation and negative controls | private server/project configuration | changes require negative tests |
| historical exports and scripts | baseline and implementation examples | private project archive | reference only until revalidated |
| future spreadsheet imports | periodic uploaded data | user-provided files plus approved loader | inspect headers and ownership before modeling |

## Verification Order

1. Read the current private project handoff and glossary.
2. Inspect the actual audit scripts and the current data source.
3. Compare live report behavior with the defined metric and filter contract.
4. Reconcile old exports only as baseline evidence, never as automatic truth.
5. Update the canonical business document after a verified implementation change.

## Export Boundary

Do not place any of the following in this portable reference:

- server IPs, hostnames, ports, database names, usernames, or SSH-key paths;
- Lark/Feishu document URLs, document IDs, board tokens, or OAuth details;
- report/card IDs that are meaningful only in one private deployment;
- company, customer, merchant, payment, or row-level business data;
- absolute local project paths or private operational script paths.
