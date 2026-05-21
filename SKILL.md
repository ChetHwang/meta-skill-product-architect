---
name: meta-skill-product-architect
description: Generate a complete, reusable product introduction Skill from any product's raw materials. Handles mixed-format inputs (docs, images, brand assets), reshapes them into a standardized L0-L6 layered knowledge base, and outputs a cross-platform Skill package ready for WorkBuddy, OpenClaw, or Claude Code.
agent_created: true
---

# Meta-Skill Product Architect

## Overview

A meta-skill that transforms raw product materials into a complete, structured product introduction Skill. The output Skill enables consistent, high-quality product introductions across any audience, format, or platform.

**What it produces**: A full Skill package named `introduce-{product-name}` following a standardized 7-layer progressive-loading architecture (L0-L6).

**Cross-platform**: The output Skill works on WorkBuddy, OpenClaw, Claude Code, or as a standalone knowledge bundle.

## Before You Start — Required Inputs

To generate a quality Skill, gather these materials before invoking this meta-skill. More detail produces a better Skill; sparse input produces a thin one.

### Required (minimum viable input)

| Category | What to provide | Granularity | Why needed |
|---|---|---|---|
| Product identity | Product name, one-sentence description, primary target audience | 1 product name + 1-line description + 1-3 line audience persona | L0 entry layer |
| Core value | What the product does + its 2-4 key promises | Each promise = 1 sentence, action-verb-led | L1 product brief |
| What it is NOT | 3-5 clarifications (common misconceptions, competitor differences) | Each clarification = "It is not X. Instead, it is Y." | L1 boundaries |
| Audience segmentation | 2-3 distinct audience types, each with: (a) 1-line persona, (b) 3-5 things this audience cares about, (c) 1 common misconception they hold | Mandatory tri-part per audience — do not collapse | L1 audience focus + output emphasis |
| **Distribution / access points** | **All public URLs where audiences can find, subscribe to, or use the product, grouped by platform/channel (e.g., website, RSS, App Store, podcast platforms, social handles)** | **Group by platform; one URL per product/module/sub-brand within each group** | **Output materials' CTAs, social copy footers, infographic bottoms, pitch deck closing slides** |

### Recommended (produces a much better Skill)

| Category | What to provide | Granularity |
|---|---|---|
| Product structure (per module) | For each module/feature/sub-brand provide **three blocks**: (1) Positioning — what slot it occupies; (2) Emphasis — what to stress when describing it; (3) Verbatim expressions — 2-4 ready-to-reuse sentences in the brand's voice | Mandatory 3-block-per-module; collapsing into a single paragraph loses depth |
| Usage patterns | How often, in what real-life contexts, on what devices (commute, dinner, before bed, on web, on mobile) | Specific scenarios with time/place anchors, not abstract |
| **Cadence / Release schedule** | **Update frequency, day-of-week mapping (e.g., Mon = module A, Tue-Thu = module B), seasonality, versioning rhythm** | **Concrete enough to write "every Monday at 6am" or "monthly major + weekly minor"** |
| Problem-solution pairs | 2-4 specific problems the product solves, with before/after framing | Concrete pain points — "users have X but lack Y" |
| Competitive differentiation | 2-3 specific differences from the top 3 alternatives | Comparative, not superlative ("unlike X, we do Y" not "we are the best") |
| Brand expressions (verbatim) | 3-5 ready-to-paste sentences in the brand's actual voice: slogans, taglines, recurring full sentences from marketing copy | Whole-sentence verbatim; not concept summaries |

### Optional (adds depth and visual polish)

| Category | What to provide | Format |
|---|---|---|
| Design philosophy | Founder interviews, design docs, "why we built this" narratives | Text or links |
| Industry context | Market reports, trend analysis, timing rationale | Text or links |
| **Methodology source attribution** | **Academic papers, white papers, research reports, frameworks the product is built on. Provide title + author + 1-line of what is borrowed** | **Citation triple: title / author / borrowed concept** |
| Brand assets | Logo files (primary + sub-brand if any), brand color hex codes, font names | PNG/SVG + values |
| Visual references | Screenshots, mockups, existing marketing materials | PNG/JPG |
| Content samples | Product demos, feature walkthroughs, sales-pitch scripts | Text, video links, PDF |
| **Serial / episodic content metadata** | **For content products (podcasts, courses, show series): per-episode title + date + topic keywords + thumbnail. Enables search and case-citation in generated materials.** | **Tabular: id, date, title, keywords, thumbnail path** |
| Pricing/packaging | Tier structure, price points, feature matrices | Table or list |
| Testimonials/reviews | User quotes, ratings, notable press mentions | Text |

### Material Reshaping Rules

All input formats will be reshaped during processing:

| Input format | Reshaped to | Action |
|---|---|---|
| PDF / .docx / .pptx | Markdown | Extract text, preserve structure |
| Screenshots / images | Structured text description | Describe colors, layout, elements, mood |
| Excel / CSV | Markdown table | Convert to readable tabular format |
| Web links | Link + summary | Scrape key content, archive |
| Audio / video | Text summary | Extract key content and value propositions |
| Logo / brand files | Preserved as-is | Archive to `assets/` |

**Core principle**: The final knowledge base must be plain-text readable Markdown with referencable image assets. All critical information must be obtainable from text alone.

---

## Workflow

> **Two modes, one source of truth.** This Skill is designed to be driven by an AI agent in conversation (the primary mode). A companion CLI in `cli/meta-skill-product-architect.py` mirrors the same lifecycle (`init` → `scan` → `generate` → `validate` → `package`) for users who want a scriptable interface, but the agent-driven workflow below is canonical — the CLI does no content generation on its own; it only scaffolds directories, checks file existence, and packages output. When agent and CLI disagree, the agent flow wins.

### Step 0 — Pre-Flight (do this before collecting anything)

Confirm three things with the user before any material collection or analysis:

1. **Primary language of the output Skill** — Chinese (zh), English (en), or other. This selects template variants in Step 4 and shapes how Step 3 extracts brand voice. Default = the language of the bulk of provided materials; if ambiguous, ask.
2. **Product type at a glance** — content product (podcast/show/course), SaaS, physical good, service, community, etc. This calibrates which output recipes apply (e.g., a B2B SaaS rarely needs "spoken intro").
3. **Output Skill name target** — confirm `introduce-{product-name}` slug; flag if the directory already exists.

Do not proceed past Pre-Flight without these three confirmations.

### Step 1: Load the Analysis Framework

Read `references/skill-archetype.md` fully before proceeding. This defines the L0-L6 seven-layer analysis framework. Understand the goals, required materials, extraction rules, and validation standards for each layer.

### Step 1.5: Choose Input Acquisition Mode

The user does NOT have to come pre-loaded with materials. Pick the lowest-friction path that fits:

| Mode | When to use | Reference |
|---|---|---|
| **Bring-Your-Own Materials** (default) | User has gathered docs, brand book, screenshots, content samples | This file's "Before You Start — Required Inputs" |
| **Auto-Scan Mode** | User can give 2-4 public URLs (website, GitHub, App Store, RSS, social profile) | `references/auto-scan-mode.md` |
| **Interview Mode** | Product owner has 20-25 min for a structured conversation; materials are scattered or non-existent | `references/interview-mode.md` |
| **Gap Survey** | Used AFTER another mode to fill 1-3 missing layers with a short questionnaire to non-technical stakeholders | `references/gap-survey-guide.md` + `templates/gap-survey.md.template.{en,zh}` |
| **Hybrid** | Most realistic; e.g., Auto-Scan first → Interview the founder on the gaps → Survey marketing for verbatim expressions | Combine references above |

Tell the user the options. Recommend a default based on what they've already mentioned (URLs available? Interview time available? Materials already in hand?). Get explicit choice before proceeding.

### Step 2: Collect and Reshape Materials

Apply the chosen mode from Step 1.5. Whatever the input source, normalize the output to plain-text Markdown with organized assets.

**Checkpoint — Confirm materials before analysis**

After reshaping, present a summary to the user:

- List of materials found and what was extracted from each
- Flag any missing categories from the Required list
- For each missing category, name a likely source (see map below) — do not just say "missing"

**Missing category → likely source map** (use this to suggest where the user can find what's missing):

| Missing input | Likely source(s) |
|---|---|
| Product identity / core value | Official website "About" page, product one-pager, founder's pitch |
| What it is NOT | Sales playbook, FAQ, competitor-comparison page |
| Audience segmentation | Marketing personas, CRM segments, customer support tags |
| Distribution / access points | Footer of product website, app-store listings, RSS feed registry, social bio |
| Product structure (per-module 3-block) | PRD, internal product wiki, onboarding deck |
| Usage patterns | Analytics dashboard (session times, retention), user interviews |
| Cadence / release schedule | Editorial calendar, release notes, content production tracker |
| Problem-solution pairs | Customer interview notes, sales objection logs, support ticket themes |
| Competitive differentiation | Sales battle cards, win/loss analysis |
| Brand expressions | Marketing copy archive, recurring social posts, brand book |
| Methodology source | Founder interview, design memo, internal R&D docs |
| Brand assets | Brand book, design-system repo, marketing asset library |
| Visual references | Marketing site, recent campaigns, social posts |
| Content samples | Product demos, episode lists, feature walkthroughs |
| Serial/episodic metadata | CMS export, content production tracker, RSS feed |

Then ask: "These materials cover X of Y required categories. Missing: [list]. Likely sources for the missing items: [refer to map]. Proceed with analysis, or supplement first?"

Do NOT proceed to Step 3 until the user confirms or explicitly says "proceed with what you have."

### Step 3: Analyze Layer by Layer (L0 → L6)

Extract information using the analysis framework defined in `skill-archetype.md`:

1. **L0 — Entry Layer**: Product name, positioning, audience, core promises, output scenarios, constraints
2. **L1 — Product Brief**: Full product persona—what it is, what it's not, structure, audience focuses, high-level expressions
3. **L2 — Foundational Logic**: Design principles, methodology, differentiation barriers, dual-language interface (professional ↔ consumer)
4. **L3 — Output Recipes**: Standard output scenarios matched to product type, each with structure + writing tips
5. **L4 — Brand Assets**: Brand hierarchy, logo usage rules, style identification, combination guidelines
6. **L5 — Visual Direction**: Visual vibe keywords, core motifs, color palette, typography, layout structures
7. **L6 — Materials Guide**: Asset inventory, usage principles, search suggestions, boundaries

**Analysis constraints**:
- Filter out noise and redundancy when materials are abundant
- Make reasonable inferences when materials are sparse, but mark them as `[inferred]` for user confirmation
- Defer to authoritative sources when materials conflict (Brand Docs > Screenshots > Verbal Descriptions)

**Checkpoint — Confirm analysis before generating files**

After completing all 7 layers, present an extraction summary table:

```
| Layer | Status | Key extraction | Missing |
|-------|--------|----------------|---------|
| L0    | ✅     | {summary}      |         |
| L1    | ✅     | {summary}      |         |
| L2    | ⚠️ inferred | {summary} | Design philosophy docs |
| ...   |        |                |         |
```

Ask: "Analysis complete. {N} layers confirmed from materials, {M} layers contain inferences. Generate files with this analysis, or adjust any layer?"

Do NOT proceed to Step 4 until the user confirms.

### Step 4: Generate Output Files

Use templates from `templates/` to populate all output files. Select the language variant matching the product's primary language:

| Template | Language | Output |
|---|---|---|
| `templates/SKILL.md.template.en` | English | `SKILL.md` |
| `templates/SKILL.md.template.zh` | Chinese | `SKILL.md` |
| `templates/references/product-brief.md.template.en` | English | `references/product-brief.md` |
| `templates/references/product-brief.md.template.zh` | Chinese | `references/product-brief.md` |
| *(same pattern for all 6 reference templates)* | | |
| `templates/agents/openai.yaml.template.en` | English | `agents/openai.yaml` |
| `templates/agents/openai.yaml.template.zh` | Chinese | `agents/openai.yaml` |
| `templates/VERSION.template` | Language-neutral | `VERSION` (seeded at `1.0.0`) |
| `templates/CHANGELOG.md.template.en` | English | `CHANGELOG.md` |
| `templates/CHANGELOG.md.template.zh` | Chinese | `CHANGELOG.md` |

Copy provided brand assets (logos, visual references) to `assets/`.

### Step 5: Run Validation

Execute every item in the full validation checklist at the bottom of `references/skill-archetype.md`. Verify the output Skill meets all structural requirements.

**Fix all failing items. Do not skip any.**

### Step 6: Package and Deliver

Produce the final Skill with this directory structure:

```
introduce-{product-name}/
├── SKILL.md
├── VERSION                  ← starts at 1.0.0
├── CHANGELOG.md             ← initial release entry
├── agents/
│   └── openai.yaml
├── references/
│   ├── product-brief.md
│   ├── foundational-logic.md
│   ├── output-recipes.md
│   ├── brand-assets.md
│   ├── visual-direction.md
│   └── materials-guide.md
└── assets/
    └── (brand and reference files)
```

Use templates `templates/VERSION.template` and `templates/CHANGELOG.md.template.{en,zh}` to seed the two lifecycle files.

### Step 7: Operate the Skill Over Time

A generated Skill is not a one-shot deliverable; it is a long-lived asset. Once handed off, future evolution follows the rules in `references/lifecycle-operations.md`:

- **Versioning discipline** — every change ships with a VERSION bump and a CHANGELOG line (MAJOR / MINOR / PATCH)
- **TTL-tagged facts** — data-bearing statements carry `@valid_until=YYYY-Q#` markers; expired facts trigger refresh
- **Diff-aware updates** — when the product changes, regenerate only affected layers, do not re-run the full meta-skill

Deliver the Skill with a one-paragraph handoff note pointing the new owner to `lifecycle-operations.md`.

---

## Quality Reference — What Good Looks Like

Use this as a mental model when generating each file. Every generated Skill should hit these quality targets.

### SKILL.md quality checklist (beyond structural validation)

- [ ] The "Overview" paragraph makes it immediately clear what the Skill does and who it's for—without reading any references
- [ ] The workflow references are progressive: Step 1 reads the brief, later steps load deeper references only when needed
- [ ] Irreplaceable facts are genuinely irreplaceable—not filler that repeats what's in the overview
- [ ] Output emphasis is audience-specific, not generic ("for consumers: emphasize ease of use" not "for consumers: emphasize value")
- [ ] Style requirements are actionable (e.g., "short sentences, 3-paragraph max for consumer copy") not abstract ("be friendly")

### Reference files quality checklist

- [ ] **product-brief.md**: Includes both "what it is" AND "what it is not." The "not" items are specific and competitive, not generic ("it's not a CRM" not "it's not bad")
- [ ] **foundational-logic.md**: The dual-language interface includes concrete translation pairs (e.g., "asynchronous collaboration → 'work on your own time'")
- [ ] **output-recipes.md**: Each recipe includes a recommended structure AND writing tips AND a tone example. Not just an outline.
- [ ] **brand-assets.md**: Includes usage boundaries—when NOT to use the logo—not just when to use it
- [ ] **visual-direction.md**: Includes colors to AVOID, not just the palette. Visual boundaries are as important as visual choices.
- [ ] **materials-guide.md**: Search suggestions are concrete (`rg 'keyword' assets/scripts`) not abstract ("search for relevant content")

### Layer completeness check

Before delivering, verify that no layer is fully empty. Every layer must have at minimum:

| Layer | Minimum content |
|---|---|
| L0 (SKILL.md) | All frontmatter fields + 6-item info order + ≥5 irreplaceable facts |
| L1 (product-brief) | Core positioning + ≥3 "not" items + ≥2 audience types |
| L2 (foundational-logic) | Core thesis + dual-language interface |
| L3 (output-recipes) | ≥4 output scenarios with structure + tips |
| L4 (brand-assets) | ≥1 logo reference + usage principles |
| L5 (visual-direction) | ≥3 vibe keywords + color palette |
| L6 (materials-guide) | Asset inventory + usage principles |

### Dry-run validation (simulate before delivering)

Before final delivery, mentally simulate a typical user prompt against the generated Skill:

1. Pick a random output scenario from the recipes (e.g., "one-pager")
2. Trace through the workflow: does the Skill guide the agent to read the right references in the right order?
3. Check: would the agent's output contain all 6 items from the core information order?
4. Check: would the output adapt correctly for the specified audience?
5. Check: does the output have a concrete CTA destination (from Distribution / access points)?

If any of these dry-run checks reveals a gap, fix the Skill before delivering.

### Content-specificity spot check (catch shallow fills)

Validation by count alone (≥3, ≥4, etc.) can be passed by one-liner placeholder fills. Add a specificity pass:

- [ ] Each "audience focus" block has ≥80 characters of substantive content (not just "audience cares about quality")
- [ ] Each module description has the mandatory 3-block structure (positioning / emphasis / verbatim) and ≥120 characters in the verbatim block
- [ ] Each output recipe has a writing-tips block of ≥3 bullets, not just an empty structure outline
- [ ] Brand expressions are whole sentences in the brand's voice, not concept summaries (e.g., "We connect textbook knowledge with the real world" — not "connects knowledge with reality")
- [ ] Visual direction's "avoid" list is non-empty (boundaries matter as much as choices)
- [ ] Distribution / access points lists actual URLs, not "see website"
- [ ] Cadence section is concrete (e.g., "Mon at 6am") not generic ("regularly updated")

Fail this pass = regenerate the failing section, do not ship.

---

## Core Information Order

When generating each file, organize content in this order:

1. What it is
2. What it contains
3. Why it matters today
4. What problem it solves
5. What value it creates for the audience
6. How it differs from alternatives

---

## Non-Negotiable Design Principles

These principles must be preserved in every output Skill:

- **Progressive loading**: Layered knowledge base—read the entry point first, load deeper layers on demand
- **Unified information core**: A stable list of irreplaceable facts that appear consistently across all outputs
- **Dual-language interface**: Professional terminology for internal/professional contexts; plain-language expressions for consumer-facing outputs
- **Material reshaping**: Mixed-format inputs → unified Markdown knowledge base
- **Verifiable architecture**: Output Skill must pass the complete validation checklist

---

## Trigger Scenarios

Invoke this meta-skill when the user says any of:

### Creation
- "Generate a product introduction Skill for {product name}"
- "Create an intro Skill like {similar product}"
- "Turn these materials into a standard product introduction Skill"
- "Analyze this product and output a Skill of the same type"
- "Build a new product intro Skill: {product name}"
- "Package {product name} materials into a complete Skill"
- `/meta-skill-product-architect`

### Input acquisition (alternative starting points)
- "Interview me about my product to generate an intro Skill" → Interview Mode
- "Here are 3 URLs — auto-generate a draft intro Skill" → Auto-Scan Mode
- "Send a survey to {person} to fill in {layers}" → Gap Survey

### Lifecycle (maintenance of an existing generated Skill)
- "We just shipped a new module — update the intro Skill" → diff-aware update
- "Check which facts in this Skill are stale" → TTL check
- "Bump version and refresh the changelog" → versioning

---

## Constraints

Observe these constraints when generating a Skill:

### Content Integrity
- Do not fabricate product information. Mark inferences as `[inferred]` and request user confirmation when materials are insufficient.
- Do not copy-paste long original text into Skill files. Distill and rewrite.
- Cross-validate across multiple material sources. Do not rely on a single source.
- Do not reference source products, example products, or origin materials in the output Skill.

### Scope and Quality
- Generate only output scenarios that match the product type. Do not invent inapplicable scenarios.
- Ensure the output Skill has no fewer than 7 information layers (L0-L6).
- Match the output Skill language to the input material language.
- Name the output Skill consistently as `introduce-{product-name}`.

### Material Sparseness
- If fewer than 2 of the 4 Required categories are provided, **pause and request more materials**. Do not proceed with analysis on insufficient data.
- If 2-3 Required categories are provided but no Recommended materials, proceed with caution. Generate `[inferred]` content only for layers that can be reasonably extrapolated. Leave fully empty layers for which no inference is possible.
- If all 4 Required categories are provided, proceed normally. Fill `[inferred]` only for Optional-layer gaps.

### File and Path Conflicts
- If the output directory `introduce-{product-name}/` already exists, ask: "Output directory already exists. Overwrite, merge, or choose a different name?"
- If a template file is missing or unreadable, pause and report which template is unavailable. Do not generate incomplete files with missing sections.
- If the `references/skill-archetype.md` framework file cannot be read, stop immediately—this is a blocking dependency.

## Troubleshooting

| Situation | Action |
|---|---|
| User provides no materials at all | Ask for at minimum: product name, one-line description, target audience, and 2 core promises. Do not proceed without these. |
| Output directory already exists | Ask to overwrite, merge, or rename. Default to rename with `-v2` suffix if user doesn't specify. |
| Template file missing | Report the missing template name. Offer to generate a minimal version from the archetype specification. |
| Validation fails on some layers | Report failing layers with specific missing items. Ask user to provide missing info or accept `[inferred]` for those layers. |
| Material language is ambiguous | Ask the user to confirm the primary language before template selection. |

---

## Resources

- [references/skill-archetype.md](references/skill-archetype.md): L0-L6 complete analysis framework (required reading)
- [references/lifecycle-operations.md](references/lifecycle-operations.md): Versioning, TTL, diff-aware updates for generated Skills
- [references/interview-mode.md](references/interview-mode.md): Structured 20-25 min interview script (input acquisition)
- [references/auto-scan-mode.md](references/auto-scan-mode.md): URL-driven automatic L0-L6 draft (input acquisition)
- [references/gap-survey-guide.md](references/gap-survey-guide.md): Targeted survey workflow for filling gaps
- [references/platform-adapters.md](references/platform-adapters.md): Multi-platform adaptation guide
- [references/distribution-guidelines.md](references/distribution-guidelines.md): Public distribution guidelines
- [templates/](templates/): Bilingual output templates (EN + ZH) including VERSION, CHANGELOG, and gap-survey
- [cli/meta-skill-product-architect.py](cli/meta-skill-product-architect.py): Standalone CLI tool

---

## Self-Validation

This meta-skill (meta-skill-product-architect) passes its own validation:

- [x] Clear "what it is" definition
- [x] Clear boundaries ("what it's not")
- [x] Documented workflow
- [x] Core information order
- [x] Non-negotiable design principles
- [x] Trigger scenario list
- [x] Constraints and boundaries
- [x] Resource index
- [x] Progressive-loading knowledge structure (read SKILL.md first, then skill-archetype.md, then others on demand)
- [x] Verifiable output (full validation checklist)
- [x] Cross-platform (WorkBuddy / OpenClaw / Claude Code / standalone CLI)
