# Meta-Skill Product Architect 🏗️

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](./VERSION)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-WorkBuddy%20%7C%20OpenClaw%20%7C%20Claude%20Code%20%7C%20CLI-orange.svg)](#platform-compatibility--跨平台兼容)
[![Bilingual](https://img.shields.io/badge/templates-EN%20%2B%20ZH-purple.svg)](./templates/)

> Drop in any product's raw materials. Get back a complete, reusable, cross-platform product introduction Skill.
>
> 丢入任意产品的原始素材，自动生成一个完整、可复用、跨平台的标准化产品介绍 Skill。

**Repository**: [github.com/ChetHwang/meta-skill-product-architect](https://github.com/ChetHwang/meta-skill-product-architect)

---

## What This Does / 这个做什么

A meta-skill that transforms raw product materials (docs, brand files, screenshots, URLs, or a 20-minute conversation) into a complete, structured product introduction Skill. The output Skill enables consistent, high-quality product introductions across any audience, format, or platform — and stays maintainable over time through versioning, TTL-tagged facts, and diff-aware updates.

---

## Key Features / 核心特性

| Feature | 特性 | Description |
|---|---|---|
| **L0-L6 Architecture** | 七层渐进式架构 | Progressive loading from elevator pitch (L0) to deep materials guide (L6) — only load what you need |
| **Multi-Audience Adaptation** | 多视角受众适配 | Auto-adjusts tone and emphasis per audience: consumers, partners, investors, media |
| **5 Input Acquisition Modes** | 五种素材获取方式 | BYO materials · Auto-Scan URLs · Structured Interview · Gap Survey · Hybrid |
| **Bilingual Output** | 中英双语模板 | `.en` and `.zh` templates — output in fluent English or native Chinese |
| **Material Reshaping** | 混合素材重塑 | PDFs, screenshots, logos → unified Markdown knowledge base |
| **8 Output Scenarios** | 八种产出场景 | One-pager, pitch deck, social media, spoken intro, infographic, and more |
| **Self-Validating** | 自验证机制 | Full checklist + content-specificity spot check (7 criteria) |
| **Lifecycle Management** | 全生命周期管理 | Versioning (MAJOR/MINOR/PATCH) · TTL-tagged facts · Diff-aware partial updates |
| **Cross-Platform** | 四平台兼容 | WorkBuddy · OpenClaw · Claude Code · Standalone CLI |
| **darwin-skill 98.0** | 自动化评分 98.0 | Evaluated by darwin-skill across 8 dimensions — the highest score in its history |

---

## Quick Start / 快速开始

### Install

```bash
git clone https://github.com/ChetHwang/meta-skill-product-architect.git
```

Then place the directory wherever your platform expects skills (see [Platform Compatibility](#platform-compatibility--跨平台兼容)).

### Use as an Agent Skill

```
1. Invoke: "/meta-skill-product-architect help me generate an intro Skill for {product name}"
2. Pick an input mode (see below)
3. Provide materials per the chosen mode
4. The agent runs L0-L6 analysis, presents a checkpoint summary, then generates a complete versioned Skill
```

### Use as a Standalone CLI

```bash
python cli/meta-skill-product-architect.py init --name "My Product" --materials ./materials/
python cli/meta-skill-product-architect.py generate
python cli/meta-skill-product-architect.py validate --skill ./introduce-my-product/
python cli/meta-skill-product-architect.py package --skill ./introduce-my-product/
```

The CLI handles scaffolding and validation. Content generation runs through an AI agent using the templates in `templates/`.

---

## Input Modes / 输入模式

| Mode | When to use | Setup |
|---|---|---|
| **Bring-Your-Own Materials** | You have docs, brand book, screenshots ready | Drop materials, the agent works through them |
| **Auto-Scan** | You have public URLs available | Give the agent 2-4 URLs (website / GitHub / App Store / RSS / social) |
| **Interview** | You have 20-25 min to talk | Agent runs a structured L0-L6 interview |
| **Gap Survey** | Some layers still missing after another mode | Agent generates a targeted survey for non-technical stakeholders |
| **Hybrid (recommended)** | Most real situations | Combine: Auto-Scan first → targeted Interview/Survey for gaps |

See [`references/interview-mode.md`](./references/interview-mode.md), [`references/auto-scan-mode.md`](./references/auto-scan-mode.md), [`references/gap-survey-guide.md`](./references/gap-survey-guide.md) for details.

---

## What You Get / 产出物

```
introduce-{product-name}/
├── SKILL.md                  # Entry point: workflow + core info + constraints
├── VERSION                   # Semver, starts at 1.0.0
├── CHANGELOG.md              # Every change, by L0-L6 layer
├── agents/
│   └── openai.yaml
├── references/               # Layered knowledge base
│   ├── product-brief.md      # Product overview (TTL-tagged facts)
│   ├── foundational-logic.md # Methodology & design principles
│   ├── output-recipes.md     # 8+ scenario templates
│   ├── brand-assets.md       # Logo system & usage rules
│   ├── visual-direction.md   # Color, typography, layout
│   └── materials-guide.md    # Asset usage & search guide
└── assets/                   # Brand assets & references
```

Every output Skill ships ready for installation on any supported platform, with lifecycle operations built in.

---

## Architecture: L0-L6 Seven-Layer Progressive Loading

```
L0 ─ Entry Layer (SKILL.md)
 │    Workflow · Info Order · Irreplaceable Facts · Output Emphasis · Boundaries
 │
 ├─ L1 ─ Product Brief
 │    Positioning · Boundaries · Structure (3-block per module) · Audience Focus
 │
 ├─ L2 ─ Foundational Logic
 │    Core Thesis · Context · Design Logic · Dual-Language Interface · Source Attribution
 │
 ├─ L3 ─ Output Recipes
 │    One-pager · Consumer · Partner · Blurb · Spoken · Poster · Social · Pitch
 │
 ├─ L4 ─ Brand Assets
 │    Logo System · Usage Principles · Style Identification · Combinations
 │
 ├─ L5 ─ Visual Direction
 │    Vibe Keywords · Motifs · Colors (incl. avoid list) · Typography · Layout
 │
 └─ L6 ─ Materials Guide
      Asset Locations · Usage Rules · Search · Boundaries
```

Load L0 first, deeper layers on demand. Full archetype specification in [`references/skill-archetype.md`](./references/skill-archetype.md).

---

## Core Design Principles / 核心设计原理

| Principle / 原则 | Description / 说明 |
|---|---|
| **Progressive Loading** / 渐进式加载 | Layered knowledge base — load entry first, deeper layers on demand |
| **Unified Information Core** / 统一信息内核 | Irreplaceable facts persist across all output variations |
| **Dual-Language Interface** / 双语言接口 | Professional terms ↔ plain language, switched by audience |
| **Material Reshaping** / 素材重塑 | PDFs, screenshots, images → unified Markdown knowledge base |
| **Verifiable Architecture** / 可验证架构 | Every Skill produced must pass the full validation checklist |
| **Long-Lived Asset** / 长寿命资产 | Versioning + TTL-tagged facts + diff-aware updates; not a one-shot |

---

## Lifecycle / 生命周期

Generated Skills are designed to outlive their initial release. They come with:

- **Semantic versioning** with explicit MAJOR / MINOR / PATCH bump rules
- **TTL-tagged facts** using `@valid_until=YYYY-Q#` markers on time-bound statements
- **Diff-aware update workflow** — when the product evolves, only affected layers regenerate

Full operations guide: [`references/lifecycle-operations.md`](./references/lifecycle-operations.md).

---

## Platform Compatibility / 跨平台兼容

| Platform / 平台 | Usage / 使用方式 | Status |
|---|---|---|
| WorkBuddy | Install to `~/.workbuddy/skills/` | ✅ |
| OpenClaw | SKILL.md + tar.gz | ✅ |
| Claude Code | Project context reference | ✅ |
| Standalone | `python cli/meta-skill-product-architect.py` | ✅ |
| OpenAI GPTs | `agents/openai.yaml` | ✅ |

Platform-specific install instructions: [`references/platform-adapters.md`](./references/platform-adapters.md).

---

## Before You Use This / 使用前准备

If you choose **Bring-Your-Own Materials** mode, gather the items below. For other modes, the agent will collect input through interview, scan, or survey.

### Required / 必需

| Category | What to provide | Why needed |
|---|---|---|
| Product identity | Name, one-line description, primary target audience | L0 entry layer |
| Core value | What it does, 2-4 key promises (action-verb-led, 1 sentence each) | L1 product brief |
| Boundaries | 3-5 "It is not X. Instead it is Y." clarifications | L1 boundaries |
| Audience types | 2-3 distinct segments, each with: persona + 3-5 priorities + 1 common misconception | L1 audience focus |
| Distribution / access points | Public URLs grouped by platform/channel (website, RSS, app stores, social handles) | Output CTAs, social footers, deck closings |

### Recommended / 推荐

| Category | What to provide | Granularity |
|---|---|---|
| Product structure (per module) | For each module: (1) positioning, (2) emphasis, (3) 2-4 verbatim brand-voice sentences | Mandatory 3-block-per-module |
| Usage patterns | How often, in what contexts, on what channels | Specific scenarios with anchors |
| Cadence / Release schedule | Day/time/frequency mapping; explicit one-time if static | "Mon at 6am" not "regularly" |
| Problem-solution pairs | 2-4 concrete problems with before/after framing | Real pain points |
| Competitive differences | 2-3 differences from top competitors | Comparative ("unlike X, we do Y") |
| Brand expressions (verbatim) | 3-5 whole sentences in the brand's actual voice | Quotable, not summarized |

### Optional / 可选

| Category | What to provide | Format |
|---|---|---|
| Design philosophy | Founder interviews, design docs | Text or links |
| Industry context | Market reports, trend analysis | Text or links |
| Methodology source | Papers/reports/frameworks; title + author + borrowed concept | Citation triple |
| Brand assets | Logo files, color hex codes, font names | PNG/SVG + values |
| Visual references | Screenshots, mockups, marketing materials | PNG/JPG |
| Content samples | Demos, feature lists, walkthroughs | Text, video, PDF |
| Serial / episodic metadata | For content products: per-episode id + date + title + keywords + thumbnail | Tabular |
| Pricing/packaging | Tier structure, price points | Table or list |
| Testimonials | User quotes, ratings, press | Text |

---

## Documentation Map

| File | Purpose |
|---|---|
| [`SKILL.md`](./SKILL.md) | Main entry — workflow, inputs, constraints, validation |
| [`references/skill-archetype.md`](./references/skill-archetype.md) | L0-L6 framework, extraction rules, validation checklist, good/bad fill examples |
| [`references/interview-mode.md`](./references/interview-mode.md) | Structured 20-25 min L0-L6 interview script |
| [`references/auto-scan-mode.md`](./references/auto-scan-mode.md) | URL-driven automatic L0-L6 draft |
| [`references/gap-survey-guide.md`](./references/gap-survey-guide.md) | Targeted gap-filling survey workflow |
| [`references/lifecycle-operations.md`](./references/lifecycle-operations.md) | Versioning, TTL, diff-aware updates |
| [`references/platform-adapters.md`](./references/platform-adapters.md) | Per-platform install and packaging |
| [`references/distribution-guidelines.md`](./references/distribution-guidelines.md) | Publishing flows and quality gates |
| [`templates/`](./templates/) | Bilingual EN/ZH templates for every output file |
| [`cli/meta-skill-product-architect.py`](./cli/meta-skill-product-architect.py) | Standalone CLI (scaffolding + validation + packaging) |

---

## Contributing / 贡献

Pull requests welcome. Before submitting:

- Ensure any change to the L0-L6 archetype includes the matching version bump and CHANGELOG entry
- Bilingual changes ship paired (EN + ZH together)
- Generated example Skills should pass the full validation checklist in [`references/skill-archetype.md`](./references/skill-archetype.md)

---

## License

MIT — see [LICENSE](./LICENSE).
