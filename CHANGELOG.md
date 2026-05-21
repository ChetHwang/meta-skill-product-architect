# Changelog — meta-skill-product-architect

All notable changes to this project follow [Semantic Versioning](https://semver.org/).

This Changelog tracks the **meta-skill itself**. Each generated `introduce-{product}` Skill maintains its own separate CHANGELOG using `templates/CHANGELOG.md.template.{en,zh}`.

## Versioning Rules

| Bump | When |
|---|---|
| MAJOR | Breaking change to the L0-L6 archetype; output Skill structure changes; templates incompatible with prior generated Skills |
| MINOR | New input mode; new reference; new template; new optional layer |
| PATCH | Wording polish; bug fixes; doc clarifications; new examples in archetype |

---

## [1.0.0] — Initial Release

### Core
- L0-L6 seven-layer progressive-loading framework (`references/skill-archetype.md`)
- Bilingual templates (EN + ZH) for SKILL.md, all 6 references, CHANGELOG, gap-survey, openai agent config
- CLI tool with init / scan / generate / validate / package commands

### Input Acquisition Modes
- **Bring-Your-Own Materials** — three-tier Required / Recommended / Optional input table with granularity guidance
- **Auto-Scan Mode** — URL-driven L0-L6 draft generation
- **Interview Mode** — structured 20-25 min L0-L6 interview script with timing and stop conditions
- **Gap Survey** — modular questionnaire for filling specific gaps with non-technical stakeholders

### Lifecycle Operations
- Versioning discipline (semver MAJOR/MINOR/PATCH bump rules)
- TTL-tagged facts with `@valid_until=YYYY-Q#` syntax
- Diff-aware update workflow with decision table mapping product changes to affected layers

### Quality Framework
- Complete validation checklist across structural / L0-L6 / deliverability / content specificity dimensions
- Good Fill vs. Bad Fill examples per layer (using generic anchors like Notion / Slack / Spotify)
- Dry-run validation step before delivery

### Cross-Platform Support
- WorkBuddy / OpenClaw / Claude Code / standalone CLI / OpenAI GPTs
