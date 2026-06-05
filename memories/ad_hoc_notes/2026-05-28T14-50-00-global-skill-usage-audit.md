# Global skill usage audit and routing correction

Trigger:
- User challenged that the design failure was not a single Taste Skill issue and asked for a global check of skill usage, including zero-use skills.

Audit performed:
- Added `tools/audit_skill_usage.py` to the evolution export.
- Scanned `C:\Users\skzjc\.codex\sessions`: 16 JSONL session files, 26,785 records before the current audit cutoff.
- Counting rule: strongest evidence is a historical tool argument opening or referencing a concrete `SKILL.md`; assistant/user mentions are secondary and may only mean discussion.

Initial findings:
- 66 discovered skills.
- 32 active skills.
- 10 active skills had zero strong/assistant evidence.
- Duplicate active `agent-reach` entry existed in the portfolio.
- `admin-platform-execution-gate` existed locally and had usage evidence but was missing from the export portfolio and tests.

Corrections made:
- Installed/exported `admin-platform-execution-gate` and made it mandatory with `open-design-design-systems` for backend/admin/internal-tool UI.
- Added a global rule: mandatory skills must leave evidence by opening `SKILL.md` or using their concrete tool/script; installed/remembered/named is not enough.
- Added the audit script to the export toolset.
- Deduped `agent-reach` in the portfolio and fixed the audit script to dedupe mirrored skills by logical name.
- Demoted cold/zero-evidence Lark skills from active to reference/on-demand while keeping routing tests that require them on matching Feishu/Lark tasks.
- Re-ran validators.

Final result:
- `check_skill_routing.py`: `portfolio_items=65`, `test_cases=30`, `active_count=22`, `failures=0`.
- `audit_skill_usage.py`: 65 logical skills, 22 active, active-zero = 0.
- Remaining warnings are intentional reference/candidate/on-demand warnings, not fake active skills.

Adopted rule:
- This failure class is global skill governance. When a skill is skipped despite being mandatory, fix the routing system, usage audit, and portfolio tiering rather than patching only the visible failed skill.
