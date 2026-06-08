# App factory skill for company 声之境-style H5/admin projects

User need: company/work projects such as "每周穿搭" should reuse the 声之境 project pattern and existing unified admin platform instead of starting from blank PRD/prototype work.

Adopted strategy: created `app-factory-h5-admin` as a scoped company/work project-factory skill. It must inspect 声之境 PRDs/mockups and unified admin sources first, produce a context packet, then deliver the requested 750px H5 HTML prototype, unified admin HTML prototype, PRD, module/data map, and verification in the gated sequence.

Reason: existing horizontal skills (`pm-prd`, `admin-platform-execution-gate`, `open-design-design-systems`) are necessary but not enough for this company project family. The repeatable workflow is "new company/self-operated H5 app under the same backend", so the missing capability is project-pattern adaptation.

Boundary: this is not a global H5, PRD, frontend, or admin default. Use it only when the task references 声之境, 每周穿搭, 多应用管理平台, 统一后台, `D:\xiaochengxu\shengzhijing`, or explicitly asks to reuse that company pattern. Do not use it for personal projects, open-source projects, external client projects, generic H5 pages, generic landing pages, or unrelated admin dashboards. In-scope inheritance is limited to structure, module responsibilities, fixed prototype dimensions, and admin shell patterns. Do not copy old content, merchant/AppID/env/payment data, or secrets. React source files with mojibake are structural references only.

Primary source paths:
- `D:\xiaochengxu\shengzhijing\声之境素材\方案\PRD-声之境微信小程序.md`
- `D:\xiaochengxu\shengzhijing\声之境素材\方案\PRD-多应用管理平台.md`
- `D:\xiaochengxu\shengzhijing\声之境素材\方案\mockup-声之境小程序.html`
- `D:\xiaochengxu\shengzhijing\声之境素材\方案\mockup-多应用管理平台.html`
- `D:\xiaochengxu\shengzhijing\h5-web`
- `D:\xiaochengxu\shengzhijing\admin-web`

Output locations:
- `C:\Users\skzjc\.codex\skills\app-factory-h5-admin`
- `C:\Users\skzjc\Documents\Codex\exports\codex-evolution-export-20260518-165156\skills\app-factory-h5-admin`
