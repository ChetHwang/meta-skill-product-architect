# Auto-Scan Mode

The lowest-friction input mode. The user provides 2-4 URLs; the agent scrapes, reads, and produces a draft L0-L6 fill. The user reviews and corrects rather than starting from blank.

Use Auto-Scan when:

- The product has a public website with non-trivial content
- The product has a public-facing artifact (GitHub repo, App Store listing, podcast feed, marketing landing page, brand book)
- The user wants "give me a starting point fast"
- Combined with Interview Mode for sections Auto-Scan can't reach (founder intent, internal methodology)

Do NOT use Auto-Scan as the sole input when:

- The product is pre-launch / has no public footprint
- The website is mostly a sign-up gate with no real content
- The product is internal-only

---

## Inputs Auto-Scan Accepts

| Input | What it feeds | Typical layer |
|---|---|---|
| Product website URL | Hero copy, feature lists, audience hints, brand voice | L0, L1, L3 |
| GitHub repo URL | README, technical positioning, feature roadmap, contributors | L0, L1, L2 |
| App Store / Play Store URL | Description, screenshots, ratings, user reviews | L0, L1, L4 (screenshots), L3 (review themes) |
| Podcast / show feed (RSS) | Episode list, descriptions, cover images, schedule | L1 (structure, cadence), L6 (episode metadata) |
| Social media profile (Twitter/LinkedIn/IG handle) | Bio, recent posts, recurring phrasings, audience replies | L1 (brand expressions), L4-L5 (visual references), audience signals |
| Brand book PDF | Logo files, color palette, typography, voice guide | L4, L5 |
| Press page / "About" page | Methodology, milestones, leadership story, source materials | L1, L2 |

Minimum viable: website + one of {GitHub, App Store listing, podcast feed}. Bonus: social handle.

---

## Auto-Scan Procedure

### Step A — URL Triage

For each provided URL, classify into one of the categories above. Reject URLs that don't fit (private docs behind auth, broken links, paywalled content). Tell the user explicitly when one URL is being skipped and why.

### Step B — Layered Extraction

Process URLs in parallel where possible. For each:

| URL type | What to extract |
|---|---|
| Website | (a) hero/h1 copy → L0 positioning candidate; (b) feature list → L1 modules; (c) testimonials → audience clues; (d) footer links → distribution channels; (e) blog/about → L2 candidates |
| GitHub README | (a) project description → L0; (b) "why this exists" → L2 candidate; (c) feature matrix → L1; (d) contributors / license → metadata only |
| App Store | (a) short description → L0; (b) long description → L1; (c) screenshots → L4 visual refs; (d) review themes → audience pain points |
| RSS feed | (a) channel description → L1; (b) episode count + dates → cadence (L1); (c) episode titles → serial metadata (L6); (d) cover images → L4/L5 |
| Social profile | (a) bio → L0 distillation; (b) pinned post → most-current positioning; (c) recurring phrases across last 20 posts → verbatim expressions (L1); (d) reply patterns → audience signals |

### Step C — Cross-Reference Conflict Resolution

Inevitably the website and the App Store description disagree, or the GitHub README contradicts the website. Apply this priority for conflicts:

| Priority | Source |
|---|---|
| Highest | Brand book / Style guide PDF (if provided) |
| 2 | Product website "About" or "Brand" page |
| 3 | Most recent dated content (blog post, recent tweet) |
| 4 | Product website hero |
| 5 | GitHub README / App Store description |
| Lowest | Inferred from user reviews or social replies |

When conflicts are surfaced, flag them for the user rather than silently picking — these often reveal real positioning ambiguity that should be resolved before generation.

### Step D — Gap Identification

After scraping, compare what Auto-Scan filled vs. what `skill-archetype.md` requires. Typical gaps:

| Frequently auto-fillable | Frequently NOT auto-fillable (need Interview/Survey) |
|---|---|
| Product name, one-line description (L0) | Detailed audience priorities + misconceptions (L1) |
| Module/feature names (L1) | Module-level "what to emphasize" (L1, 3-block) |
| Public distribution links (L1) | Methodology source attribution (L2) |
| Visual references — logo, colors (L4/L5) | Internal boundaries / "what NOT to say" (L0/L1) |
| Cadence for content products (L1) | Founder intent / why-now (L2) |
| Brand expressions from recent posts (L1) | Visual boundaries — colors to avoid (L5) |

For each gap, decide:
- **Run partial Interview Mode** on just the gap sections (recommended for ≥3 gaps)
- **Send Gap Survey** to a non-technical stakeholder (recommended for 1-2 gaps)
- **Proceed with `[inferred]`** (only for low-stakes Optional fields)

### Step E — Material Reshaping

All scraped content goes through the standard Reshaping Rules from `SKILL.md`:
- HTML/web copy → Markdown
- Images / screenshots → text description + archive to `assets/`
- PDF brand books → Markdown extraction + asset preservation
- Audio/video samples → transcript + value-point summary

### Step F — Review with User Before Generation

Present back to the user:

```
Auto-Scan Summary
─────────────────
Sources scanned: {N}
URLs that worked: {list}
URLs skipped: {list with reason}

Layers filled:
- L0: ✅ filled from {source}
- L1: ⚠️ partial — missing audience misconceptions, module emphasis
- L2: ❌ needs methodology source — recommend Interview
- L3: ✅ inferred from product type (content product → 8 standard recipes)
- L4: ✅ filled from brand book
- L5: ✅ filled from website screenshots
- L6: ✅ filled from RSS feed

Conflicts found:
- Website says "for parents and educators"; App Store says "for kids ages 4-12 and their families" → please confirm which is canonical

Recommended next step:
[a] Run partial Interview on L2 (~5 min)
[b] Send Gap Survey for audience misconceptions (~10 min for non-technical stakeholder)
[c] Proceed with [inferred] tags on the gaps
```

Wait for explicit confirmation before generation.

---

## Anti-Patterns

- **Trust the marketing site too much** — Most websites are aspirational, not descriptive. Cross-check with reviews and social to find the *real* product positioning.
- **Skip the review step** — Auto-Scan output ALWAYS needs human review. The user knows things the website doesn't say.
- **Inferring boundaries from absence** — Auto-Scan can find what the product IS, very rarely what it ISN'T. The "boundaries" layer almost always needs Interview or Survey input.
- **Scraping behind auth** — If a URL needs login, stop and ask the user to either share content directly or skip that source.

---

## Output of Auto-Scan

The output of Auto-Scan Mode is NOT a finished Skill — it is a populated draft of L0-L6 with:

- Filled cells where the scrape was confident
- `[inferred from website hero]` tags where confidence is moderate
- `[GAP — needs interview/survey]` tags where confidence is low
- A conflict log
- A recommended next-step path

The user then proceeds to either generate (if gaps are acceptable) or run a partial Interview / Survey to close them.
