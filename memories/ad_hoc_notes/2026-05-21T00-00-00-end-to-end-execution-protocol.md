# End-To-End Execution Protocol

Date: 2026-05-21

User criticism: another conversation stopped after each substep, asked for routine next-step confirmation, or claimed completion after only one part of the user's larger request was done.

Adopted rule:

- Keep the user's original request as the completion target.
- Do not stop after completing only a substep.
- Report milestones as progress, not completion.
- Continue safe obvious next steps without asking.
- Ask only when continuing would materially change cost, risk, privacy exposure, account action, data loss, production state, or product direction.
- If blocked, state the exact blocker, what was tried, what input/authorization is needed, and what will happen next after it is provided.

Applied:

- Updated `%USERPROFILE%\.codex\AGENTS.md`.
- Updated `%USERPROFILE%\.codex\private\knowledge-vault\wiki\topics\working-habits.md`.
- Synced the change to the portable export bundle.

Validation:

- Verified the new global rule is present in `AGENTS.md`.
- Verified the working-habits vault page contains the end-to-end execution section.
