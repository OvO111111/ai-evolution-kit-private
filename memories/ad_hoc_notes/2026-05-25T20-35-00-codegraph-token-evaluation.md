# CodeGraph token-saving evaluation

Source:
- WeChat: https://mp.weixin.qq.com/s/fsJ0E8pebxxQzylcb1-HdA
- Project: https://github.com/colbymchenry/codegraph
- Docs: https://colbymchenry.github.io/codegraph/

Assessment:
- Useful candidate, but not a universal quality-preserving compression layer.
- CodeGraph reduces coding-agent cost by pre-indexing code structure with tree-sitter into a local SQLite graph and exposing it through MCP. It is different from caveman/caveman-compress, which reduce output or memory prose tokens.
- Official current benchmark is more conservative than the WeChat article headline: about 35% cheaper, 57% fewer tokens, 46% faster, and 71% fewer tool calls across 7 repos. The 94% figure is a best-case tool-call reduction, not guaranteed total token reduction.

Adoption decision:
- Do not install globally by default yet. Treat as candidate for codebase-understanding tasks only.
- Use when the repo is medium/large, unfamiliar, cross-file, or call-graph-heavy, especially before architecture tracing, impact analysis, or refactoring.
- Do not use for PRD, reports, WeChat/Feishu work, browser tasks, data analysis, or small repos where indexing overhead may exceed savings.

Validation plan:
- Pick one real medium/large repo and run an A/B task: normal `rg`/read workflow versus CodeGraph-assisted workflow.
- Success criteria: fewer exploratory file reads/tool calls, same or better file/path accuracy, no missed dynamic-language edge that affects the answer.
- If validation passes, add a focused codebase-intelligence skill/routing rule. If it fails or adds friction, keep as reference only.
