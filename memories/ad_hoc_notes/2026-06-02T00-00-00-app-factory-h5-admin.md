# App factory skill for company 声之境-style H5/admin projects

User need: company/work projects such as "每周穿搭" should reuse the 声之境 project pattern and existing unified admin platform instead of starting from blank PRD/prototype work.

Adopted strategy: created `app-factory-h5-admin` as a scoped company/work project-factory skill. It must inspect 声之境 PRDs/mockups and unified admin sources first, produce a context packet, then deliver the requested 750px H5 HTML prototype, unified admin HTML prototype, PRD, module/data map, and verification in the gated sequence.

Reason: existing horizontal skills (`pm-prd`, `admin-platform-execution-gate`, `open-design-design-systems`) are necessary but not enough for this company project family. The repeatable workflow is "new company/self-operated H5 app under the same backend", so the missing capability is project-pattern adaptation.

Boundary: this is not a global H5, PRD, frontend, or admin default. Use it only when the task references the matching company project family, runs inside a private registered company workspace, or explicitly asks to reuse that company pattern. Do not use it for personal projects, open-source projects, external client projects, generic H5 pages, generic landing pages, or unrelated admin dashboards. In-scope inheritance is limited to structure, module responsibilities, fixed prototype dimensions, and admin shell patterns. Do not copy old content, merchant/AppID/env/payment data, or secrets.

Primary source paths and output locations remain in the private project registry and
must not be exported. The portable skill records only source types and scope rules.
