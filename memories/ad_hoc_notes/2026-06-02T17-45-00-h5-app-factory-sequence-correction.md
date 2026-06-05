# H5 app factory sequence correction

User correction: the H5 app-factory workflow must not jump straight to HTML or PRD. Correct sequence is:

1. inspect source/reference materials;
2. analyze and decompose the product;
3. ask the necessary blocking questions;
4. confirm the core H5 experience, admin experience, page/function boundaries, and payment/data/admin scope;
5. build the 750px H5 HTML and unified-admin HTML prototypes;
6. wait for user confirmation of page/function direction;
7. write the PRD against the confirmed prototype.

Applied changes:

- Updated `C:\Users\skzjc\.codex\skills\app-factory-h5-admin\SKILL.md` with an explicit Analysis And Question Gate before HTML.
- Updated `C:\Users\skzjc\.codex\skills\pm-prd\SKILL.md` so PRD generation does not preempt the app-factory prototype-confirmation flow.
- Updated `app-factory-h5-admin/agents/openai.yaml`.
- Synced the modified skill files into `C:\Users\skzjc\Documents\Codex\exports\codex-evolution-export-20260518-165156\skills`.
