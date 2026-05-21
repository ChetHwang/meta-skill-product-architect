# Distribution Guidelines

How to publish `meta-skill-product-architect` publicly and promote generated Skills.

## Publishing the Meta-Skill

### GitHub (Recommended)

Repository structure matches the project structure. Key elements for a strong README:

- Badges at top (version, license, platform support)
- 30-second quick start
- L0-L6 architecture diagram
- Cross-platform usage instructions
- Contribution guide

### Launch Checklist

- [ ] README complete and readable
- [ ] At least one generated Skill example available
- [ ] Cross-platform usage instructions included
- [ ] Validation checklist referenced in SKILL.md
- [ ] LICENSE file present
- [ ] .gitignore present
- [ ] No sensitive information in docs or code

## Publishing Generated Skills

### Minimum Viable Skill

A generated `introduce-{product-name}` Skill is ready to publish when:
- [ ] Passes full validation checklist (all items ✅)
- [ ] Tested on at least one platform (recommend WorkBuddy)
- [ ] SKILL.md frontmatter complete with `agent_created: true`
- [ ] All reference files present and non-empty

### Recommended Flow

1. Generate Skill using the meta-skill
2. Run validation checklist
3. Load and test on WorkBuddy
4. Fix any issues found
5. Package as tar.gz
6. Distribute

## Promotional Messaging

### One-Liner

> Drop in product materials. Get back a polished, reusable product introduction Skill.

### Use Cases

- Product managers building reusable intro knowledge bases
- Operations teams standardizing brand output
- Startup teams formalizing product documentation
- Content/education products engineering their intro materials

### Differentiators

- **Not a template — a framework**: More than fill-in-the-blanks. Mines your materials for methodology, differentiation, and visual direction
- **Not one-off — a reusable asset**: Generated Skills can be reused indefinitely with consistent output
- **Not single-platform**: WorkBuddy, OpenClaw, Claude Code, standalone CLI — all covered
- **Self-validating**: Output is automatically checked against a complete quality checklist
