# Interview Mode

An alternative to material collection: instead of asking the user to gather a stack of documents, the agent runs a structured **20-25 minute interview** with the product owner. The interview output IS the material—the agent extracts L0-L6 directly from the conversation.

Use Interview Mode when:

- The product owner is non-technical or doesn't have neatly organized docs
- Materials are scattered across multiple people / tools and gathering them blocks progress
- The product is so new that formal documentation does not yet exist
- The product owner prefers to talk over assemble

Do NOT use Interview Mode when:

- The user has already prepared comprehensive materials (use those first; interview only fills gaps)
- The product is technical and requires precise specs (use Auto-Scan Mode or direct PRD ingestion)
- The interviewee is not the product owner (proxies miss too much)

---

## Pre-Interview Checklist

Before starting, confirm with the user:

1. **Time budget**: 20-25 minutes uninterrupted. If they have <15 min, decline and reschedule.
2. **Recording / note method**: explicit consent. If recording is not possible, the agent takes structured notes.
3. **Output language**: Chinese or English. This shapes question phrasing and follow-up choices.
4. **Permission to follow up**: if a key area is sparse, agent will revisit it. Confirm this is OK.

---

## Interview Script — 7 Sections, ~3 Minutes Each

The script maps 1:1 onto L0-L6. Each section has a **primary question**, **probe questions** for when answers are thin, and **stop conditions** to keep timing.

### Section 1 — Identity (L0) [~3 min]

**Primary**: "If you had 30 seconds in an elevator to tell someone what your product is, who it's for, and why it matters — what would you say?"

**Probes if thin**:
- "Who's the single most representative user? Walk me through one of them by name (or pseudonym)."
- "What's the most accurate one-sentence description of what you do?"

**Capture**:
- Product name (verbatim)
- One-sentence description (record literally, don't paraphrase)
- Primary target audience (with a real persona name if possible)

**Stop when**: agent has all three above.

---

### Section 2 — Boundaries (L1, partial) [~2 min]

**Primary**: "When people first hear about your product, what do they mistakenly think it is — but it actually isn't?"

**Probes**:
- "What's the closest competitor people compare you to, and what's the actual difference?"
- "What kind of customer or use case do you turn away, or that you intentionally don't serve?"

**Capture**: 3-5 "It's not X. It's actually Y." statements.

**Stop when**: ≥3 distinct misconceptions captured.

---

### Section 3 — Why Now (L1 + L2) [~3 min]

**Primary**: "Why is this product needed today specifically? What changed in the world (or your industry) that makes it land now?"

**Probes**:
- "What happens in your customer's life that makes them say 'I need this'?"
- "Five years ago, would this product have worked? Why or why not?"

**Capture**:
- Why-now context (1-2 paragraphs of substance)
- 2-4 problem-solution pairs (concrete before/after)

**Stop when**: at least one specific era-shift named + 2 problem-solution pairs.

---

### Section 4 — Product Structure (L1, deepest section) [~5 min]

This section needs the most time. The three-block format is mandatory.

**Primary**: "Walk me through the product piece by piece. For each module / feature / sub-brand, three questions: (a) what slot does it occupy, (b) what should we emphasize when describing it, (c) what's a real sentence you'd say about it to a customer."

**Probes per module**:
- "If you had to pick one phrase from your marketing for this module, what would it be?"
- "Why does this module exist as a separate thing rather than being part of another module?"

**Capture per module**:
- Positioning (1-2 sentences)
- Emphasis (2-4 things to stress)
- 2-4 verbatim expressions

**Stop when**: every module covered with three blocks each.

---

### Section 5 — Audience Focus (L1) [~3 min]

**Primary**: "Tell me about your 2-3 most distinct customer types. For each one: who they are, what they care most about, and what they often misunderstand."

**Probes**:
- "How does the way you describe the product change between [Audience A] and [Audience B]?"
- "What's a misconception specific to this audience type?"

**Capture per audience**:
- Persona (1-2 sentences)
- 3-5 priorities
- 1 common misconception

**Stop when**: ≥2 audiences captured with all three sub-items.

---

### Section 6 — Brand Expressions & Cadence (L1) [~2 min]

**Primary**: "Quote me 3-5 sentences you'd actually use in a marketing post, an investor email, or a sales call. Word-for-word, not summarized."

**Then**: "How often do you ship / publish / update? Walk me through your rhythm."

**Capture**:
- 3-5 verbatim brand sentences
- Cadence specifics (day, time, frequency, or "one-time release")

**Stop when**: both above filled with concrete content.

---

### Section 7 — Distribution & Methodology Source (L1 + L2) [~3 min]

**Primary distribution**: "Where can someone find or buy or subscribe to this product? Give me every URL, by platform."

**Capture distribution**: a list of grouped clickable URLs.

**Primary methodology**: "Is there a framework, a research paper, a school of thought, or someone else's idea that influenced how you designed this? Be specific — title and author, if any."

**Capture methodology**: source citation triple OR explicit "internal thinking only."

**Stop when**: distribution links collected + source attribution answered (either citation or explicit "none").

---

### Section 8 (Optional) — Visual & Asset Pointers (L4 + L5) [~2 min]

Skip if user is non-design and has nothing visual to say.

**Primary**: "If I asked your designer for three words describing your visual style, what would they be? And what's a color you'd never use?"

**Capture**:
- 3-5 vibe keywords
- 1-3 colors to avoid (the boundary is often more useful than the palette)
- Pointer to logo file location (URL or file path)

---

## Post-Interview Reshaping

Immediately after the interview:

1. **Transcribe verbatim quotes** — anything the user said in quoted form goes straight to L1 `verbatim_expressions`. Do not paraphrase.
2. **Map answers to layers** — for each captured item, mark which L0-L6 layer it populates.
3. **Identify gaps** — any layer with fewer captures than the minimum required (per `skill-archetype.md`). For each gap, decide: re-interview (if blocking) or proceed with `[inferred]` (if low-stakes).
4. **Confirm with user** — present the extracted L0-L6 summary back to the user in <500 words. Get sign-off before generating files.

---

## Common Interview Failure Modes & Fixes

| Failure | Symptom | Fix |
|---|---|---|
| User over-pitches | All answers sound like marketing copy with no specificity | Ask: "Tell me what you'd say if a friend asked, not what's on the website." |
| User vague-paraphrases | "We help people do better things." | Ask: "Give me a specific example. A real customer. Last week." |
| User forgets boundaries | Can list features but not "what it's NOT" | Try: "What's the worst customer you've ever had — the one you should have turned away?" |
| Over time | Section 4 alone eats 15 minutes | Set a 5-minute timer audibly; move on when it rings |
| User mentions one module then describes the whole product | Module bleeding | Force return: "Stop — that's the next module. Let's finish this one first." |
| User goes too high-level on methodology | "We believe in empowering users" | Ask: "Whose work shaped that belief? Anyone you'd cite?" |

---

## Multi-Speaker Mode (Optional Extension)

If the product has multiple owners (e.g., a founder + a head of marketing + a creative director), running parallel interviews and merging is better than averaging in a single session. Run Section 4 (product structure) with the product lead, Section 6 (brand expressions) with marketing, and Section 8 (visual) with design. Merge during post-interview reshaping.
