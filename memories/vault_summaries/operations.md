# Vault Operations Log

Append-only. Use entries like:

```markdown
## [YYYY-MM-DD HH:mm +08:00] ingest | source title
- source_id:
- source_path:
- sensitivity:
- pages_updated:
- notes:
```

## [2026-05-18 21:05 +08:00] ingest | initial memory consolidation

- source_id: memory_registry
- source_path: `%USERPROFILE%\.codex\memories\MEMORY.md`
- sensitivity: personal/work mixed
- pages_updated:
  - `wiki/topics/working-habits.md`
  - `wiki/topics/self-evolution-system.md`
  - `wiki/topics/skill-routing.md`
  - `wiki/topics/knowledge-vault-design.md`
  - `wiki/topics/html-artifacts.md`
  - `wiki/topics/wechat-work-context.md`
  - `wiki/topics/payment-product-design.md`
  - `wiki/decisions/export-boundaries.md`
  - `wiki/decisions/multi-agent-context-protocol.md`
  - `wiki/projects/project-registry.md`
  - `index/source-map.md`
  - `index/query-guide.md`
  - `config/source-registry.jsonl`
- notes: Organized high-signal memories and lookup locations. Excluded raw project code, raw work chats, account state, secrets, customer/payment data, and large task-local files.

## [2026-05-18 21:15 +08:00] index | rebuild SQLite and Chinese aliases

- source_id: compiled_vault
- pages_updated:
  - `index/aliases.md`
  - `db/vault.sqlite`
- notes: Added Chinese query aliases and rebuilt the local SQLite/FTS cache. Verified exact Chinese queries can resolve through the alias index.

## [2026-05-18 21:55 +08:00] governance | EvoSkill-inspired skill portfolio

- source_id: evoskill_article
- source_path: `https://mp.weixin.qq.com/s/h8gsYACrt0mnBUT5BchaIw?scene=334`
- pages_updated:
  - `wiki/topics/skill-routing.md`
  - `wiki/decisions/skill-governance.md`
  - `config/skill-portfolio.jsonl`
- notes: Classified 61 local visible skills into active/reference/candidate tiers. Adopted EvoSkill governance ideas without running automated mutation.

## [2026-05-19 09:10 +08:00] governance | PM PRD routing failure guard

- source_id: pm_prd_routing_failure
- pages_updated:
  - `wiki/decisions/pm-prd-routing-guard.md`
  - `index/aliases.md`
- notes: Added a hard guard that PRD/solution/prototype tasks must inspect real reference PRDs, mockups, samples, API docs, and business boundaries before drafting.

## [2026-05-19 09:20 +08:00] validation | skill trigger regression harness

- source_id: skill_trigger_test_harness
- pages_updated:
  - `wiki/topics/skill-routing.md`
  - `wiki/decisions/skill-governance.md`
  - `config/skill-trigger-tests.jsonl`
  - `scripts/check_skill_routing.py`
- notes: Added a 25-case trigger test set and checker. Verified local vault and export-bundle layouts both run with 0 failures and 9 intentional warnings.

## [2026-05-20 00:00 +08:00] governance | Open Design admin UI absorption

- source_id: open_design_repo
- source_path: `https://github.com/nexu-io/open-design`
- pages_updated:
  - `wiki/decisions/admin-ui-design-standard.md`
  - `config/skill-portfolio.jsonl`
  - `config/skill-trigger-tests.jsonl`
  - `skills/open-design-design-systems/SKILL.md`
  - `AGENTS.md`
- notes: Promoted `open-design-design-systems` to active for backend/admin UI and added a mandatory closest-reference design-system gate.

## [2026-05-21 00:00 +08:00] behavior | end-to-end execution protocol

- source_id: user_execution_criticism
- pages_updated:
  - `AGENTS.md`
  - `wiki/topics/working-habits.md`
  - `memories/extensions/ad_hoc/notes/2026-05-21T00-00-00-end-to-end-execution-protocol.md`
- notes: Added a hard rule against stopping after substeps or asking for routine next-step confirmation. Completion must map to the user's original goal, not a milestone.

## [2026-05-21 00:10 +08:00] behavior | outcome-first reporting

- source_id: user_reporting_criticism
- pages_updated:
  - `AGENTS.md`
  - `wiki/topics/working-habits.md`
  - `memories/extensions/ad_hoc/notes/2026-05-21T00-10-00-outcome-first-reporting.md`
- notes: Added a hard final-reporting rule: answer requirement status and user-visible outcome first; technical details are evidence, not the headline.

## [2026-05-22 10:20 +08:00] skill | SenseNova data analysis report absorption

- source_id: sensenova_skills_article
- source_path: `https://mp.weixin.qq.com/s/v-hUiwCqm2Bp70s4b8U6iQ?scene=334&click_id=2`
- pages_updated:
  - `skills/data-analysis-report/SKILL.md`
  - `AGENTS.md`
  - `wiki/decisions/data-analysis-report-standard.md`
  - `wiki/topics/skill-routing.md`
  - `config/skill-portfolio.jsonl`
  - `config/skill-trigger-tests.jsonl`
  - `memories/extensions/ad_hoc/notes/2026-05-22T10-20-00-sensenova-data-analysis-report-absorption.md`
- notes: Added a mandatory data-analysis-report skill so reports start from decision question, data inventory, metric definitions, evidence-backed findings, recommendations, and suitable deliverables instead of only file processing.
