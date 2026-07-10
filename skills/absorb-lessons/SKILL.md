---
name: absorb-lessons
description: Evaluate external advice, repo conventions, prior mistakes, or user-provided "make Codex smarter" material and turn only the useful, non-duplicative parts into reusable global Codex guidance. Use when the user asks Codex to evolve, learn advanced practices, absorb a repository or article, improve global behavior, create/update durable skills, or design a self-improvement mechanism.
---

# Absorb Lessons

Use this skill to convert raw advice into durable, scoped operating guidance. The goal is adaptation, not copying.

## Workflow

1. **Define the improvement target.** State what behavior should improve, which future tasks benefit, and what should stay unchanged.
2. **Acquire the real source.** When the input is a URL or repository, use `web-access` and the source-owning tool such as `github:github`. Record what was actually read; do not evaluate from a title or promotional summary.
3. **Extract principles, not prose.** Read the source material for failure modes, decision rules, and verification habits. Avoid importing slogans, long examples, or tool-specific wording unless the tool is actually used.
4. **Build an impact map.** Identify every affected skill family, router, automation, memory boundary, export rule, and test. Do not fix only the named example when the same root cause affects sibling capabilities.
5. **Deduplicate against existing instructions.** Keep guidance only if it adds a clearer trigger, sharper rule, reusable checklist, or missing boundary. If current Codex or project rules already cover it, mention the overlap and do not duplicate it.
6. **Localize to Codex.** Convert advice into instructions that fit Codex tools, sandbox rules, memory rules, skills, and the user's global workflow. Preserve source attribution in summaries, not in copied instruction text.
7. **Separate stable rules from observations.** Put durable behavior in a skill. Put uncertain, dated, or project-specific observations in memory only when the user explicitly asks for a memory update.
8. **Red-team consequential adoption.** Before changing global defaults, broad routing, memory boundaries, or repeated workflows, use `adversarial-review` to test whether the diagnosed problem is real, whether a smaller fix exists, what context or compatibility cost the rule adds, and which minimum experiment could disprove it.
9. **Create a blind before/after test.** Record the baseline, make the smallest coherent change, then run a fresh-session route or artifact test. The evaluator receives the natural user request and acceptance rubric, not the intended answer, suspected defect, changed files, or author reasoning. A validator or route-selection pass alone is not behavioral proof.
10. **Produce a change manifest.** Before completion, list every skill, rule, automation, test, or tool changed; what changed; why; test result; and anything deliberately left unchanged.

## Acceptance Criteria

An absorbed lesson is good only when it is:

- **Actionable:** A future Codex instance can decide when and how to use it.
- **Scoped:** It names the situations where it applies and where it should not slow work down.
- **Non-duplicative:** It improves existing behavior instead of restating broad virtues.
- **Verifiable:** It includes success checks, examples of better behavior, or review criteria.
- **Adversarially checked:** High-impact changes survived a falsification attempt, and artifact claims survived a blind behavioral test.
- **Small:** It protects context space by moving details to references and keeping the main skill lean.
- **Complete:** It covers sibling skills and shared mechanisms affected by the same root cause, or explicitly explains why they are out of scope.

## Current Baseline

Read `references/principles.md` when the task asks to improve Codex behavior, critique an agent guideline, or absorb a new engineering-practice source. Use it as a baseline to decide what is already covered before adding more guidance.

## Update Rules

- Prefer editing this skill over creating many overlapping behavior skills.
- Keep `SKILL.md` focused on the absorption process.
- Put detailed adopted principles, source summaries, and examples in `references/`.
- Do not write to global memory unless the user directly asks to update memory.
- Do not claim a rule is globally active until the file exists under the global skills directory and validation passes. Tell the user that restarting Codex may be required for new skills to be discovered.
- Keep route selection, static contract validation, artifact quality, and live behavior as separate evidence tiers. Never report a route test as proof that the resulting work is good.
- A system-wide evolution request is incomplete without an exact changed-skill list,
  an evolution-mechanism list, fresh behavioral tests, and a residual-risk list.
