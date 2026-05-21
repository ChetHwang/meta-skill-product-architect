# Platform Adapters

How to install and use `meta-skill-product-architect` across different AI platforms, and how to migrate generated Skills between platforms.

## Installing the Meta-Skill

### WorkBuddy

```bash
cp -r meta-skill-product-architect ~/.workbuddy/skills/
# Trigger: /meta-skill-product-architect
```

### OpenClaw

```bash
tar -czf meta-skill-product-architect.tar.gz meta-skill-product-architect/
# Upload via OpenClaw skill marketplace or manual install
```

### Claude Code

Add this repository as project context. In conversation: "Follow the Meta-Skill Product Architect guide to analyze my product materials."

### Standalone

```bash
python cli/meta-skill-product-architect.py --help
```

## Distributing Generated Skills

### WorkBuddy

```bash
cp -r ./introduce-{product-name} ~/.workbuddy/skills/
```

### OpenClaw

```bash
tar -czf introduce-{product-name}.tar.gz introduce-{product-name}/
```

### Claude Code

Reference the output Skill directory in project files or load via file reference.

### As Standalone Knowledge Bundle

Share the entire `introduce-{product-name}` directory. Any Markdown-capable AI agent can read it.

## Cross-Platform Compatibility

| Element | WorkBuddy | OpenClaw | Claude Code | Standalone |
|---|---|---|---|---|
| SKILL.md direct | ✅ | ✅ | Via reference | Readable |
| agents/openai.yaml | Informational | Informational | Informational | Informational |
| references/ layered | ✅ | ✅ | Manual | Readable |
| assets/ images | ✅ | ✅ | Partial | Partial |
| tar.gz packaging | Optional | ✅ | Not needed | Not needed |

**Key principle**: All critical information lives in Markdown text. Images and brand files are enhancements, not necessities. Any platform can at minimum read the text.

## Naming Convention

All generated Skills use the `introduce-{product-name}` format. Lowercase only, spaces replaced with hyphens, alphanumeric and hyphens only.
