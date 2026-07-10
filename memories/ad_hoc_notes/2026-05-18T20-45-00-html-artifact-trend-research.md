# HTML artifact trend research

Trigger: the user challenged a surface-level treatment of HTML and asked why HTML is currently hot in Silicon Valley / AI developer circles.

Findings from live research:

- The current wave is tied to Claude Code / Anthropic ecosystem discussion around "The Unreasonable Effectiveness of HTML", amplified by Simon Willison and example galleries of single-file HTML artifacts.
- The core argument is not "HTML is prettier than Markdown"; it is that HTML lets agents output artifact-shaped work: spatial comparison, annotated diffs, diagrams, dashboards, timelines, prototypes, sliders, forms, and custom editors.
- HTML is acting as a browser-native runtime for human review and iteration: no backend, no build step, directly openable, shareable, and interactive.
- Markdown remains better for durable source truth, diffs, long-term rules, specs, and text knowledge that humans need to co-edit.
- HTML has costs: noisy diffs, hidden complexity, security surface via JavaScript/external resources, possible false confidence from polished design, and heavier generation/review cost.

Adoption:

- Treat HTML as a first-class compiled artifact format and interaction runtime, not just a raw webpage snapshot.
- Keep raw truth in source files/Markdown/JSONL; use HTML as a human-facing view/tool with visible citations and adjacent data exports.
- Add three HTML roles to the private knowledge vault schema: `source_html`, `compiled_html`, and `interactive_html`.
