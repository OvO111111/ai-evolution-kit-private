---
name: absorb-lessons
description: Evaluate external advice, repo conventions, prior mistakes, or user-provided "make Codex smarter" material and turn only the useful, non-duplicative parts into reusable global Codex guidance. Use when the user asks Codex to evolve, learn advanced practices, absorb a repository or article, improve global behavior, create/update durable skills, or design a self-improvement mechanism.
---

# Absorb Lessons

Use this skill to convert raw advice into durable, scoped operating guidance. The goal is adaptation, not copying.

## Workflow

1. **Define the improvement target.** State what behavior should improve, which future tasks benefit, and what should stay unchanged.
2. **Extract principles, not prose.** Read the source material for failure modes, decision rules, and verification habits. Avoid importing slogans, long examples, or tool-specific wording unless the tool is actually used.
3. **Deduplicate against existing instructions.** Keep guidance only if it adds a clearer trigger, sharper rule, reusable checklist, or missing boundary. If current Codex or project rules already cover it, mention the overlap and do not duplicate it.
4. **Localize to Codex.** Convert advice into instructions that fit Codex tools, sandbox rules, memory rules, skills, and the user's global workflow. Preserve source attribution in summaries, not in copied instruction text.
5. **Separate stable rules from observations.** Put durable behavior in a skill. Put uncertain, dated, or project-specific observations in memory only when the user explicitly asks for a memory update.
6. **Validate before claiming adoption.** Run the skill validator after edits. If the change is behavioral rather than syntactic, test with a realistic prompt or explain why forward-testing was skipped.

## Acceptance Criteria

An absorbed lesson is good only when it is:

- **Actionable:** A future Codex instance can decide when and how to use it.
- **Scoped:** It names the situations where it applies and where it should not slow work down.
- **Non-duplicative:** It improves existing behavior instead of restating broad virtues.
- **Verifiable:** It includes success checks, examples of better behavior, or review criteria.
- **Small:** It protects context space by moving details to references and keeping the main skill lean.

## Current Baseline

Read `references/principles.md` when the task asks to improve Codex behavior, critique an agent guideline, or absorb a new engineering-practice source. Use it as a baseline to decide what is already covered before adding more guidance.

## Update Rules

- Prefer editing this skill over creating many overlapping behavior skills.
- Keep `SKILL.md` focused on the absorption process.
- Put detailed adopted principles, source summaries, and examples in `references/`.
- Do not write to global memory unless the user directly asks to update memory.
- Do not claim a rule is globally active until the file exists under the global skills directory and validation passes. Tell the user that restarting Codex may be required for new skills to be discovered.
