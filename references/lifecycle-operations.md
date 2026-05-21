# Lifecycle Operations

A generated `introduce-{product-name}` Skill is not a one-shot document; it is a long-lived asset that must evolve with the product it represents. This file defines the three operational disciplines: **versioning**, **TTL-tagged facts**, and **diff-aware updates**.

---

## 1. Versioning Discipline

Every generated Skill ships with two files at the root:

- `VERSION` — single line, semver (`MAJOR.MINOR.PATCH`)
- `CHANGELOG.md` — every change, one line, references affected layer(s)

### When to bump

| Bump | Trigger |
|---|---|
| MAJOR | Core positioning changes; "what it's NOT" boundary shifts; rebrand; target audience change |
| MINOR | New module added; new output recipe added; new audience segment; new sub-brand |
| PATCH | Wording tweaks; refreshed TTL'd facts; new verbatim expressions; clarifications; typo fixes |

### Bump procedure

1. Identify the highest-severity change in the update.
2. Bump that level (and reset lower-level digits).
3. Add CHANGELOG entry referencing affected layer(s): e.g., `## [1.2.0] — 2026-06-01 / Added — L1: new sub-brand "Curiosity Treehole"`.
4. Mark `[BREAKING]` for any change that invalidates already-distributed output materials.

---

## 2. TTL-Tagged Facts

Many "facts" in a product Skill are time-bound: user counts, press mentions, partnerships, pricing tiers, release dates. Tagging them with a Time-To-Live prevents stale data from leaking into outputs months later.

### Syntax

Use HTML-style comments embedded next to the fact:

```markdown
- Our community has 50,000 weekly active listeners. <!-- @valid_until=2026-Q4 @owner=marketing -->
- Featured in TechCrunch's "Top 10 Family Podcasts" list, May 2025. <!-- @valid_until=2027-05 -->
- Pricing: Pro tier is $29/month. <!-- @valid_until=2026-12 @owner=finance -->
```

### Where to apply

- `references/product-brief.md` — Core Positioning / Recommended Scenarios / Brand Expressions / Distribution sections
- `references/foundational-logic.md` — Source Attribution (re-cite if the source becomes outdated)
- `references/brand-assets.md` — Asset Inventory (if a logo retires, mark the old entry)

### What NOT to tag

Do NOT tag:
- Methodology / why-it-matters statements — these should be evergreen by design
- Boundary statements ("it is not X") — if these change, the skill needs a MAJOR bump, not a TTL refresh

### Refresh workflow

1. Run the spot-check: search the Skill for `@valid_until=` markers. (Tip: `rg '@valid_until' references/`)
2. For each marker, if today ≥ `@valid_until`, ask the marked `@owner` to confirm or update.
3. Updates trigger a PATCH bump and a CHANGELOG line: `Refreshed — L1: weekly active listener count → 75,000 @valid_until=2027-Q4`.

---

## 3. Diff-Aware Updates (Not Full Regeneration)

When a product evolves, do NOT re-run the meta-skill from scratch. That wastes effort and risks losing carefully refined wording. Instead, do a targeted update.

### Decision table

| What changed about the product | Which layers regenerate | Bump |
|---|---|---|
| Core positioning shifted (different problem, different audience) | L0 + L1 + L2 + L3 (output emphasis only) | MAJOR |
| New module / sub-brand added | L1 (insert one new module block) + L4 (add logo) + L5 (extend visual motifs) + L6 (extend search suggestions) | MINOR |
| Existing module repositioned | L1 (rewrite that module's 3 blocks) + L3 (audit recipes referencing it) | MINOR |
| Pricing / packaging changed | L1 (Pricing section if present) + refresh related TTL'd facts | PATCH |
| Press / partnership added | L1 (relevant Recommended Scenarios / Testimonials section) + new TTL'd fact | PATCH |
| Visual rebrand (color/font/logo) | L4 + L5 fully regenerate; L0-L3 unchanged | MINOR or MAJOR depending on scope |
| New output channel needed (e.g., podcast → also doing newsletter) | L3 (add one new recipe) + L6 (add asset class if applicable) | MINOR |
| Brand voice tightening | L0 (style requirements) + L1 (verbatim expressions revised) + L3 (writing tips per recipe) | MINOR |
| Methodology source updated (new paper / framework cited) | L2 (Source Attribution) + L2 (Methodology if mechanism changed) | PATCH or MINOR |

### Targeted update workflow

1. **Identify the change** — name what specifically about the product changed (be concrete: "added the 'Saturday Bonus Episode' format" not "we updated the product").
2. **Map to layers** using the decision table above.
3. **For each affected layer**, regenerate ONLY that file. Other files stay untouched.
4. **Re-run validation** focused on changed layers — full validation is optional, layer-specific validation is required.
5. **Update VERSION** per bump rules.
6. **Add CHANGELOG entry** with layer references.
7. **Dry-run check**: pick one output recipe that exercises the changed layer; mentally simulate generating it; confirm output reflects the change without breaking anything else.

### When to do a full regeneration anyway

- MAJOR-level rebrand (≥3 layers affected)
- Skill has accumulated >20 PATCH-level updates without a MINOR consolidation
- The product structure changed enough that ≥3 modules need rewriting
- The Skill failed the validation checklist after multiple targeted updates (sign of accumulated drift)

---

## 4. CLI Support

The companion CLI (`cli/meta-skill-product-architect.py`) currently implements:

```bash
python cli/meta-skill-product-architect.py validate --skill ./introduce-my-product/
# Runs structural + content checks against the archetype validation checklist

python cli/meta-skill-product-architect.py scan --skill ./introduce-my-product/
# Reports completion status for each L0-L6 layer

python cli/meta-skill-product-architect.py package --skill ./introduce-my-product/
# Produces a distributable tar.gz
```

**Planned (not yet implemented)** — for now, follow the manual workflow in sections 1-3:

- `bump --level {major|minor|patch}` — bump VERSION and open CHANGELOG for editing
- `ttl-check` — list all `@valid_until` markers and flag expired ones
- `diff-plan --change "{description}"` — print the decision-table mapping for a described change

Everything in sections 1-3 above can be done manually without the CLI.

---

## 5. Lifecycle Anti-Patterns

Watch for these — they indicate the skill is decaying:

- **Stale brag** — older skill claims that contradict the current product (e.g., "now serving 50k users" when it's actually 200k, or 10k)
- **Recipe drift** — output recipes that reference modules no longer in L1
- **Verbatim divergence** — `verbatim_expressions` no longer match what marketing actually says today
- **Boundary creep** — "what it's NOT" list silently stops being enforced; outputs start using forbidden superlatives
- **TTL fatigue** — `@valid_until` markers all past their date, nobody refreshing

Any one of these = pause and do a maintenance pass.
