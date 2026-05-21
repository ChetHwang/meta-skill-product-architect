# Gap Survey Guide

The Survey is the **lightest-weight input mode**. Use it after Auto-Scan to fill the 1-3 layers Auto-Scan couldn't reach, with a non-technical stakeholder who doesn't have time for a full interview.

A good survey:
- Takes the respondent ≤10 minutes
- Asks ≤10 questions
- Is targeted (only the gaps, not a re-collection of everything)
- Returns directly usable content (not raw "thoughts")

---

## When to Use Survey vs. Interview vs. Auto-Scan

| Situation | Mode |
|---|---|
| Have public assets + an hour with the founder | Auto-Scan → Interview (best combination) |
| Have public assets + founder is unavailable | Auto-Scan → Gap Survey to founder's deputy / marketing lead |
| No public assets, founder available | Interview Mode only |
| No public assets, founder unavailable | Survey to 2-3 people who collectively know the product |
| Need to refresh an existing Skill | Survey targeting just the TTL-expired fields |

Surveys are also good for **lifecycle refresh**: when TTL'd facts expire, send a 2-question survey to the marked `@owner` rather than re-interviewing.

---

## Generating a Targeted Survey

The agent should NOT send the full 7-section template. Instead:

1. **Identify the gap layers** — from Auto-Scan output or skill-archetype audit
2. **Pick the relevant question modules** from the template (each module = 1-3 questions tied to a layer)
3. **Customize question phrasing** to the actual product (replace `{{PRODUCT_NAME}}`, weave in any known facts to anchor the respondent)
4. **Specify a deadline** (3-5 business days; longer kills response rate)
5. **Send to the right person** — see "Who to send each module to" table below

---

## Who to Send Each Module to

| Layer to fill | Best respondent | Backup respondent |
|---|---|---|
| L0 identity | Founder / product lead | Marketing lead |
| L1 boundaries ("not what") | Product lead | Sales lead (knows misconceptions intimately) |
| L1 audience priorities | Customer success / marketing | Sales lead |
| L1 brand expressions | Marketing / brand manager | Copywriter / content lead |
| L1 cadence / distribution | Product lead / operations | Marketing lead |
| L2 methodology source | Founder | Head of product / R&D |
| L4 brand assets | Design lead | Marketing lead |
| L5 visual direction (avoid colors etc.) | Design lead | Brand manager |

If the same person owns multiple layers, batch their questions into one survey.

---

## Survey Response Quality Control

When responses come back:

- **Reject vague answers** — "We help users do better" / "Our customers love us" — politely re-ask: "Can you give me a specific phrase you'd use, word for word?"
- **Reject summarized verbatims** — for brand expressions, if the answer is "we focus on simplicity" instead of an actual sentence, follow up
- **Cross-check against Auto-Scan** — if survey responses contradict public materials, flag the conflict for the original requester
- **Catch boilerplate** — if multiple respondents give very similar answers (often because they read the same internal doc), don't double-count

Aim for response signal that's specific enough to drop directly into a `{{VERBATIM_EXPRESSIONS}}` block. If responses aren't there yet, do one follow-up round before degrading to `[inferred]`.

---

## Survey Templates

Two bilingual templates ship with this Skill:

- `templates/gap-survey.md.template.en` — English survey
- `templates/gap-survey.md.template.zh` — Chinese survey

Each contains modules for: identity, boundaries, audience, brand expressions, cadence, methodology, visual direction. Pick only the modules relevant to your gaps.

---

## Anti-Patterns

- **Sending the full survey to everyone** — Recipients get fatigued and answer poorly. Always target.
- **Long-form text-box-only questions** — Give example formats inside each question to anchor expectations
- **Sending without context** — If respondents don't know why they're being asked, answers degrade. Always include a 1-paragraph context: "We're building a structured intro Skill for {{PRODUCT_NAME}}. Your answers will be used verbatim in marketing materials. Reply with specifics, not summaries."
- **Letting it sit** — Set a deadline. Follow up at 50% of deadline. Stop trying at 150% of deadline.
