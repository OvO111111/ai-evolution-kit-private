# PM PRD routing failure

Trigger: the user cited another conversation where the assistant admitted it failed to trigger and execute the `pm-prd` workflow for a PRD + backend prototype + grey-release decision-system task.

Failure:

- The assistant did not first locate/read the real project PRDs and mockup HTML files.
- It produced generic language before building a context packet.
- It treated installed skills as automatic quality improvement, but failed to actually route through the skill workflow.

Correction:

- For PRD, solution plan, product requirements, backend/admin prototype, grey-release system, complaint workflow, or `方案 + HTML/mockup` tasks, `pm-prd` is mandatory.
- Before writing, inspect referenced PRDs, HTML mockups, samples, interface docs, current workflows, and confirmed business boundaries.
- Build a compact context packet first.
- Do not output generic PRD/flowchart/industry wording before source inspection.

Applied:

- Updated `C:\Users\skzjc\.codex\AGENTS.md`.
- Updated `C:\Users\skzjc\.codex\skills\pm-prd\SKILL.md`.
