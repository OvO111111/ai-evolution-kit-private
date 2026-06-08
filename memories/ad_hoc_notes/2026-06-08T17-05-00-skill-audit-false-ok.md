# Skill audit false OK correction

User challenged prior claims that all skills were installed, recognized, and working. The prior conclusion was invalid.

Root cause:
- The check conflated several different states: repository/project discussed, local skill installed, plugin cache present, current session skill metadata injected, callable tool exposed, trigger selected, and `SKILL.md` actually opened.
- A skill cannot be considered "working" from file/cache presence alone.
- `huashu-design` had been discussed as a candidate/reference, but was not installed as a local Codex skill until 2026-06-08, so earlier claims that all mentioned design skills were OK were wrong.

Current audit snapshot:
- Audit file: `C:\Users\skzjc\.codex\skill-mentioned-audit-2026-06-08.csv`
- Mentioned items checked: 53
- Local skill exists: 25
- Local plus plugin skill exists: 8
- Plugin skill exists only: 8
- Not installed as a skill: 12
- Not installed list: `hermes-self-evolution`, `hermes-agent`, `proactive-agent`, `self-improving-agent`, `summarize`, `tavily`, `clawhub`, `self-improving-agent-next`, `autonomous-ai-agents`, `gbrain`, `genericagent`, `agent-skills`.

Durable rule:
- Do not answer "all skills are OK" unless the evidence separates: installed on disk, visible in current session, trigger metadata match, actual `SKILL.md` loaded, and smoke test outcome.
- For user-named skills, if the skill is absent, say absent; if only a repo/project was evaluated, call it reference-only, not installed.
- If a script used for audit emits errors, the audit is not valid until the script is fixed and rerun cleanly.
