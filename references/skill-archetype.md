# Skill Archetype — L0-L6 Framework

## Overview

Analyze any product's raw materials and map them to this 7-layer structure. Applies to content products, physical goods, SaaS, apps, services, or any offering needing consistent introduction materials.

## Core Principles

1. **Progressive loading**: Load L0 first, deeper layers on demand. Do not load all context at once.
2. **Unified core**: A stable set of irreplaceable facts persists across all output variations.
3. **Dual-language interface**: Professional terms for internal use; plain language for consumers.
4. **Material reshaping**: Mixed inputs → unified Markdown knowledge base.
5. **Verifiable output**: Every generated Skill must pass the full validation checklist.

---

## L0 — Entry Layer (SKILL.md)

### Extraction Targets

| Field | Source | Example |
|---|---|---|
| Product name | Brand/project name | "Slack" |
| One-line positioning | Slogan, core value | "Team communication for the modern workplace" |
| Audience | Personas, docs | "Teams of 10-500 in tech companies" |
| Core promises | Value props / selling points | "Searchable history, integrations, channels" |
| Output scenarios | Use cases | One-pager, pitch deck, landing page, social |

### Generation Rules

Frontmatter:
```yaml
---
name: introduce-{product-name}
description: Generate introduction materials for {product name} across scenarios and audiences.
agent_created: true
---
```

Workflow structure (fixed):
1. Read `references/product-brief.md` first
2. Load other references based on output type
3. Follow Core Information Order
4. Adjust density and tone per scenario

Core Information Order (fixed):
1. What it is
2. What it contains
3. Why it matters today
4. What problem it solves
5. What value it creates
6. How it differs from alternatives

Must include: Irreplaceable facts, audience-specific emphasis, boundaries, style rules, resource index.

---

## L1 — Product Brief

### Extraction Priority
1. Official website / product page
2. Brand positioning docs
3. PRD / specs
4. User feedback
5. Media coverage

### Required Sections
- Core positioning (1 sentence + promise list)
- Boundaries — what it is NOT (≥3 clarifications)
- Why it matters today (context + timing)
- Problem-solution pairs (2-4, contrast framing)
- Long-term outcomes (3-5)
- **Product structure — per-module three-block format (mandatory):**
  - **Positioning** — what slot this module occupies / what scenario or capability it serves
  - **Emphasis** — what to stress when describing this module externally
  - **Verbatim expressions** — 2-4 ready-to-paste full sentences in the brand's voice
  - Do not collapse multiple modules into one paragraph; one ### subsection per module
- **Release cadence** (concrete: e.g., "Mon at 6am", "monthly major + weekly minor", or "single release, no recurrence")
- Usage patterns (frequency, context, channel)
- Recommended scenarios
- Common brand expressions (3-5 whole sentences, brand voice — not concept summaries)
- Audience focus (≥2 types, each with: 1-line persona + 3-5 emphasis points + 1 common misconception)
- Talking points / high-level messaging (2-3)
- **Distribution / access points** (clickable URLs grouped by platform, one per module/sub-brand; or explicit "Internal product — not publicly distributed")

---

## L2 — Foundational Logic

### Extraction Sources
- Founder statements / design docs → core philosophy
- Industry reports → context and timing
- Competitive analysis → differentiation barriers
- User research → real pain points
- Academic references → theoretical backing

### Required Sections
- Core thesis (≤3 sentences)
- Context/era analysis: why now
- Module methodology: for each module, explain what it solves, its mechanism, why it works
- Value translation: N summary statements
- Dual-language interface: professional terms ↔ consumer expressions (with mapping)
- Usage boundaries: when NOT to use this framing
- **Source attribution**: cite any external papers/reports/frameworks borrowed, OR explicitly state "Methodology drawn from internal product team thinking; no external sources." Empty is not acceptable.

---

## L3 — Output Recipes

### Scenario Matching

| Scenario | Product types | Structure |
|---|---|---|
| One-pager | All | Positioning → Structure → Value → Differentiation |
| Consumer intro | B2C | Warm, accessible, value-forward |
| Partner/pitch | B2B | Positioning → Structure → Differentiation → Potential |
| Professional | Expert/industry | Methodology, depth, domain value |
| Profile blurb | All | One-line + one-line differentiation |
| Spoken/audio | Voice/video | Natural flow, rhythm, invitation |
| Infographic | Visual | Short labels, parallel, scannable |
| Social media | Brand | Hook + value + CTA |
| Pitch/deck | Fundraising | Market → Product → Value → Extensibility |

Each scenario requires: recommended structure + writing tips + tone guidance.

---

## L4 — Brand Assets

### Extraction
- Primary logo → archive to assets/, record path
- Sub-brand logos → record, describe relationship
- Brand colors → extract hex values
- Fonts → record names and usage
- Brand elements → describe visually

### Required Sections
- Asset inventory (≥1 logo)
- Usage principles (primary + sub-brand)
- Brand mark relationships
- Style identification per mark
- Combination guidelines
- Usage boundaries

---

## L5 — Visual Direction

### Extraction from: logos, screenshots, covers, design files
- Vibe keywords (3-5 adjectives)
- Core visual motifs (element + description + use)
- Color palette (primary hex + secondary hex + avoid tones)
- Typography (headings + body + hierarchy rules)
- Layout templates (top/middle/bottom or modular)

### Reshaping
- Only logo → reverse-engineer colors and keywords
- Multiple images → inductively find patterns
- No visuals → infer from positioning, mark as [suggested]

### Required Sections
- Vibe keywords
- Core motifs
- Color direction
- Typography guidelines
- Layout structures
- Visual boundaries (styles to avoid, copy limits, temperature)

---

## L6 — Materials Guide

### Asset Organization

| Type | Action | Location |
|---|---|---|
| Screenshots | Keep as reference | assets/screenshots/ |
| Logos | Keep original | assets/ |
| PDF/Word | Convert to Markdown | references/ or assets/docs/ |
| Content lists | Standardize | assets/scripts/ or assets/content/ |
| Video/audio | Describe + link | assets/ (index) |
| Web links | Archive as Markdown | assets/links/ |

### Reshaping Table

| Input | Output | Method |
|---|---|---|
| PDF | Markdown | Extract text, preserve structure |
| .docx | Markdown | Convert, keep structure |
| .pptx | Markdown | Text + image descriptions |
| Image | Text description | Visual features + mood |
| Excel/CSV | Markdown table | Readable table |
| Link | Link + summary | Key content scrape |
| Audio/video | Text summary | Key content + value points |

### Required Sections
- Asset location inventory
- Usage principles (do + don't)
- Search suggestions
- Recommended usage in output materials
- Boundaries and scope limits

---

## Full Validation Checklist

### Structural Completeness
- [ ] Directory: SKILL.md + references/ + agents/ + assets/
- [ ] All reference files exist and are non-empty
- [ ] agents/openai.yaml exists
- [ ] SKILL.md frontmatter complete with agent_created: true
- [ ] `VERSION` file exists at root (semver: MAJOR.MINOR.PATCH)
- [ ] `CHANGELOG.md` exists at root with at least the initial 1.0.0 release entry
- [ ] TTL markers on any data-bearing facts in references (`@valid_until=YYYY-Q#` or `@valid_until=YYYY-MM`); evergreen statements do not require markers

### L0 Checks
- [ ] Clear "what it is" definition
- [ ] Clear "what it's not" boundaries
- [ ] Progressive-loading workflow documented
- [ ] Core information order (6 steps)
- [ ] Irreplaceable facts list
- [ ] Audience-specific output emphasis
- [ ] Boundary and constraint rules
- [ ] Style requirements
- [ ] Resource index pointing to references/

### L1 Checks
- [ ] Core positioning (1 sentence)
- [ ] "What it's not" / Boundaries (≥3)
- [ ] Real-world value context
- [ ] Problem-solution pairs
- [ ] Module/feature descriptions in mandatory three-block format (positioning / emphasis / verbatim) per module
- [ ] Release cadence is concrete (specific day/time/frequency or explicit "single release")
- [ ] Usage patterns
- [ ] Recommended scenarios
- [ ] Brand expressions are whole sentences in brand voice (not concept summaries)
- [ ] Audience focus (≥2 types, each with persona + emphasis points + 1 common misconception)
- [ ] Talking points (2-3)
- [ ] Distribution / access points lists actual URLs grouped by platform (or explicit internal-only statement)

### L2 Checks
- [ ] Core thesis (≤3 sentences)
- [ ] Context/era analysis
- [ ] Module methodology
- [ ] High-level summary
- [ ] Dual-language interface (with explicit term-to-consumer-expression mapping pairs)
- [ ] Usage boundaries
- [ ] Source attribution (external citations or explicit internal-only statement)

### L3 Checks
- [ ] ≥4 output scenarios
- [ ] Each with structure + writing tips
- [ ] Scenario-product type match

### L4 Checks
- [ ] Asset inventory (≥1 logo)
- [ ] Usage principles
- [ ] Style identification
- [ ] Combination guidelines
- [ ] Boundaries

### L5 Checks
- [ ] Vibe keywords (3-5)
- [ ] Core visual motifs
- [ ] Color direction
- [ ] Typography guidance
- [ ] Layout structure
- [ ] Visual boundaries

### L6 Checks
- [ ] Asset inventory
- [ ] Usage principles
- [ ] Search suggestions
- [ ] Recommended usage patterns
- [ ] Boundaries

### Deliverability
- [ ] Output Skill loadable in WorkBuddy
- [ ] Output Skill loadable in OpenClaw
- [ ] Output Skill loadable in Claude Code
- [ ] Output Skill packageable as tar.gz
- [ ] Output Skill directly readable by AI agents

### Content Specificity (catches shallow fills that pass count-based checks)
- [ ] Each audience focus block has ≥80 chars of substantive content
- [ ] Each module's verbatim-expressions block has ≥120 chars (2-4 full sentences)
- [ ] Each output recipe has ≥3 writing-tips bullets, not just structure outline
- [ ] Brand expressions are whole sentences in brand voice (specificity test: would a copywriter recognize this as brand-correct?)
- [ ] Visual direction's "avoid" list is non-empty
- [ ] Distribution / access points contains actual URLs (or explicit internal-only statement)
- [ ] Release cadence is concrete (day/time/frequency or explicit one-time)
- [ ] Source attribution is filled (external citations or explicit internal-only)
- [ ] No `{{PLACEHOLDER}}` or `[inferred]` tags remain unaddressed in the final output

---

## Appendix — Good Fill vs. Bad Fill (Generic Examples)

Use a known generic product (e.g., Notion, Slack, Spotify) as a sanity-check anchor when reviewing each layer's fills. The examples below are NOT to be copied into the output — they are calibration tools only.

### L0 — Entry Layer

**Good fill (Notion)**
```
description: Generate introduction materials for Notion across scenarios — one-pagers, sales decks, onboarding copy, social posts — for individuals, teams, and enterprises evaluating an all-in-one workspace.
```

**Bad fill (vague)**
```
description: Generate introduction materials for Notion.
```

Why bad: no scenario coverage, no audience signal, doesn't tell the agent when to invoke.

### L1 — Product Brief

**Good fill (Slack, structure block)**
```
### Channels
Positioning: The default surface where teams have ongoing topic-scoped conversations.
Emphasis: Async-first; persistent; searchable; organized by topic not by sender.
Verbatim expressions:
- "Where work happens — organized by topic, searchable forever."
- "Move conversations out of inboxes and into channels everyone can find later."
```

**Bad fill**
```
### Channels
Channels are where teams talk. They are organized and persistent.
```

Why bad: no slot/scenario coverage; no quotable sentences; tells agent nothing about emphasis.

### L2 — Foundational Logic

**Good fill (dual-language interface, Spotify)**
```
Professional ↔ Consumer mapping:
- "Collaborative filtering" → "Recommendations from listeners like you"
- "Audio fingerprinting" → "Find a song by humming it"
- "Personalized algorithmic playlists" → "Made just for you"
```

**Bad fill**
```
Professional ↔ Consumer mapping:
- Use technical terms internally; use plain language for users.
```

Why bad: principle without mapping; agent cannot apply it.

### L3 — Output Recipes

**Good fill (one-pager writing tips)**
```
Writing tips:
- Lead with the 1-sentence positioning, not with the company history
- Use parallel structure for the module list (3 modules = 3 cards of equal length)
- Close with a single concrete CTA — link to product, not "learn more"
- Avoid: superlatives without backing ("the best", "leading"), feature dumps, jargon
```

**Bad fill**
```
Writing tips:
- Be clear and concise.
- Use a friendly tone.
```

Why bad: not actionable; applies to any document; doesn't shape this recipe's output.

### L4 — Brand Assets

**Good fill (usage boundaries)**
```
- Do not place the secondary logo on backgrounds containing red (clash with primary brand)
- Minimum clear space around the logo: equal to the height of the "S" glyph
- The icon-only mark is for app icons and favicons; never use it in body copy
- When primary and secondary marks appear together, the primary is always larger and always to the left
```

**Bad fill**
```
- Use the logo correctly.
- Maintain brand consistency.
```

Why bad: no operational constraint; nothing an agent can check.

### L5 — Visual Direction

**Good fill (colors to avoid)**
```
Avoid:
- Saturated reds and oranges (clash with primary teal)
- Pure black backgrounds (use #1a1a2e instead — softer, on-brand)
- Pastel palettes (signal "kids product" — wrong audience)
```

**Bad fill**
```
Avoid:
- Off-brand colors.
```

Why bad: tautological; specifies nothing.

### L6 — Materials Guide

**Good fill (search suggestions)**
```
Search suggestions:
- Episode topic: `rg 'museum|history' assets/scripts/`
- Date lookup: `rg '^date: 26010[5-9]' assets/scripts/`
- Speaker quotes: `rg '^speaker:' assets/scripts/`
```

**Bad fill**
```
Search suggestions:
- Search for keywords in the materials.
```

Why bad: not executable; gives the agent zero advantage over no instruction.
