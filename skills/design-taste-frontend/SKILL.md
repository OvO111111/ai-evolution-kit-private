---
name: design-taste-frontend
description: Anti-template frontend direction and quality control for public landing pages, portfolios, marketing sites, editorial pages, and redesigns. Use when a public-facing web surface needs stronger typography, composition, visual hierarchy, asset direction, motion discipline, or a real design-system choice. Do not use as the main route for admin dashboards, dense internal tools, data tables, or multi-step product flows.
---

# Design Taste Frontend

This skill corrects generic frontend taste without forcing one fashionable style. Read the brief and sources before choosing a direction.

The original long-form guide is preserved in `references/full-guide.md`. Read only the relevant sections when the task needs deep motion recipes, detailed design-system install references, the block-library contract, or the exhaustive anti-pattern checklist. Do not load the full guide for a routing decision or a simple page.

## Scope

Use for:

- public landing and marketing pages;
- portfolios and editorial pages;
- visual redesigns of public sites;
- one lane in a requested multi-option visual comparison.

Do not use as the primary workflow for admin/internal tools or product-flow design. Route those through `admin-platform-execution-gate` or Product Design.

## Design Read

Before code, establish:

- page type and audience;
- brand and reference signals;
- trust, accessibility, regulatory, and content constraints;
- whether this is a targeted evolution or a full redesign;
- a design family or real design system that fits the audience.

If a missing decision materially changes the direction, ask all currently known blocking questions in one compact batch, at most three. Otherwise state the inferred direction briefly and continue.

## Direction Dials

Set three task-local values from 1-10:

- `DESIGN_VARIANCE`: symmetry and conventionality versus authored composition;
- `MOTION_INTENSITY`: static hierarchy versus cinematic interaction;
- `VISUAL_DENSITY`: gallery-like breathing room versus information density.

Infer them from the brief. Do not use one fixed default across projects, and do not ask the user to edit the skill file.

## Foundation Choice

Use an existing project system first. For a new build, choose one foundation that matches the domain:

- Fluent for Microsoft/enterprise products;
- Material for Material-native products;
- Carbon for enterprise analytics;
- Polaris for Shopify surfaces;
- Atlaskit for Atlassian-like tools;
- Primer for GitHub/developer products;
- GOV.UK or USWDS for matching public-sector work;
- Radix or shadcn for owned modern React components;
- native CSS/Tailwind for authored editorial, brutalist, kinetic, or campaign work.

Use one system per project. Verify dependencies before importing. Do not claim an aesthetic trend is an official system.

## Anti-Template Rules

Avoid defaults that are not justified by the brief:

- purple/blue glow over a dark mesh;
- centered hero plus three equal feature cards;
- repeated left-text/right-image sections;
- nested cards and decorative pills;
- giant headings that hide the actual product;
- fake dashboards, fake metrics, and invented testimonials;
- random serif emphasis inside sans headlines;
- beige/brass/espresso as an automatic premium palette;
- Inter as the automatic font for every brand;
- decorative scroll labels, version tags, and meaningless metadata strips.

Use visible product/media assets for sites and games. Keep hero content inspectable, and show a hint of the next section in the first viewport.

## Composition

- Choose a layout family from the content, not from habit.
- Keep navigation stable and one line on desktop.
- Use grid tracks and responsive constraints instead of fragile percentage math.
- Avoid repeating the same section composition more than twice in succession.
- Use cards only when boundaries or elevation communicate real hierarchy.
- Keep one radius system, one icon family, and one accent logic.
- Ensure all text fits its container at mobile and desktop widths.

## Typography And Color

- Select type for audience, language, and brand character.
- Preserve readable body measure and hierarchy.
- Use serif only when the brief is genuinely editorial, heritage, luxury, or publication-led.
- Lock one palette for the page; do not drift between warm and cool neutrals.
- Check button, form, status, and text contrast.
- Do not make every surface monochromatic or one-hue.

## Interaction And Motion

Every visible action must work or be explicitly unavailable. Include hover, focus, disabled, loading, empty, error, and reduced-motion behavior where relevant.

Motion must support hierarchy, storytelling, feedback, or state change. Avoid scroll-jacking and continuous state-driven rerenders. Read the motion sections in `references/full-guide.md` only when implementing sticky stacks, horizontal pans, or advanced reveal systems.

## Redesign Workflow

1. Capture the existing site at representative widths.
2. Identify what must be preserved: content, routes, brand assets, conversion intent, and working behavior.
3. Audit hierarchy, composition, typography, color, assets, interaction, accessibility, and performance.
4. Choose targeted evolution or full redesign explicitly.
5. Implement the smallest coherent direction, not disconnected local patches.
6. Compare before/after screenshots and verify routes and interactions.

## Multi-Option Lane

When this skill owns one option in a multi-lane comparison, state a distinct thesis and differ from other lanes in at least four dimensions: composition, typography, density, color logic, content hierarchy, motion, navigation, or asset treatment. Recoloring a shared template fails.

## Verification

Before completion:

- run build/lint/type checks that exist;
- inspect screenshots at desktop and mobile widths;
- verify text fit, overflow, navigation, CTAs, forms, and major states;
- confirm real assets render and no placeholder or broken media remains;
- check contrast, keyboard focus, reduced motion, and layout shift risks;
- compare against the selected reference or original redesign target.

If the result still reads as a generic template, revise it before delivery.
