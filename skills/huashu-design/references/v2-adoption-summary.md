# Huashu Design v2.0 Local Adoption Summary

Source: `https://github.com/alchaincyf/huashu-design`, tag `v2.0`, commit `8a8d87d83b8dec767f37c05077732edb3ce5f903`.

## Adopted

- Keep the local `SKILL.md` short; use upstream references and assets through progressive disclosure.
- Fact-check concrete products, releases, versions, specs, and events before designing around them.
- If the user gives no visual source and asks for something vague like "make it look good", do not guess a final page. Produce three distinct design directions first.
- Treat core assets as first-class: logo, product imagery, UI screenshots, real data shape, and current product state are more important than abstract brand-color talk.
- Match the role to the artifact: slide designer for decks, motion designer for animation, UX/prototype designer for app flows, reviewer for critique.
- For app/iOS prototypes, prefer real imagery from reliable sources, wrap screens in device frames when appropriate, and run click-path checks before claiming success.
- Use Tweaks/variants when visual alternatives or live tuning are the point of the task.
- For HTML animation deliverables, video/GIF/audio export can matter; for static UI or admin screens, do not force MP4/GIF/BGM.
- Expert review uses concrete criteria: philosophy fit, hierarchy, detail execution, functionality, innovation, plus fix list.

## Rejected / constrained

- Do not copy the upstream 57KB `SKILL.md` as the active entrypoint; it is too large for normal routing and will hurt context hygiene.
- Do not make Huashu the default for production web apps, backend logic, SEO sites, or ordinary admin CRUD implementation.
- Do not import large demo media into the portable GitHub evolution export; keep those local and export only the compressed skill, references, and lightweight assets.
- Do not add Huashu watermarks except when the user explicitly wants animation/video distribution behavior.

## Update check

Future weekly checks must include manually adapted external skills with `upstream` metadata. For Huashu, run:

```powershell
git ls-remote --tags https://github.com/alchaincyf/huashu-design.git
```

Compare the highest stable tag with `upstream_ref` and report whether local resources were synced and whether local adaptation changed.
