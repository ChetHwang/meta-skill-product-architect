#!/usr/bin/env python3
"""
Meta-Skill Product Architect — CLI Tool

Generate standardized product introduction Skills from raw product materials.
Cross-platform: WorkBuddy, OpenClaw, Claude Code, standalone.

Usage:
    python meta-skill-product-architect.py init --name "Product Name" --materials ./path/
    python meta-skill-product-architect.py generate --output ./output/
    python meta-skill-product-architect.py validate --skill ./output/
    python meta-skill-product-architect.py package --format workbuddy --skill ./output/
"""

import argparse
import json
import os
import shutil
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def cmd_init(args):
    """Initialize a new product analysis session."""
    name = args.name
    materials_path = Path(args.materials).resolve()
    output_path = Path(args.output or f"introduce-{slugify(name)}").resolve()
    
    if output_path.exists():
        print(f"⚠️  Output directory '{output_path}' already exists.")
        if not args.force:
            print("   Use --force to overwrite.")
            return
    
    print(f"🔍 Initializing analysis for: {name}")
    print(f"📁 Materials: {materials_path}")
    print(f"📦 Output: {output_path}")
    
    # Create output structure
    dirs = [
        output_path,
        output_path / "references",
        output_path / "agents",
        output_path / "assets",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    
    # Create manifest
    manifest = {
        "product_name": name,
        "product_slug": slugify(name),
        "materials_path": str(materials_path),
        "created_at": datetime.now().isoformat(),
        "status": "initialized",
        "layers": {
            "L0_skill_md": "pending",
            "L1_product_brief": "pending",
            "L2_foundational_logic": "pending",
            "L3_output_recipes": "pending",
            "L4_brand_assets": "pending",
            "L5_visual_direction": "pending",
            "L6_materials_guide": "pending",
        }
    }
    
    with open(output_path / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Session initialized at: {output_path}")
    print(f"   Next: Edit manifest.json to track progress, then run 'generate'")
    
    # Scan materials
    scan_materials(materials_path, output_path)


def cmd_scan(args):
    """Scan existing output directory and report status."""
    skill_path = Path(args.skill).resolve()
    if not skill_path.exists():
        print(f"❌ Output path '{skill_path}' not found.")
        return
    
    manifest_file = skill_path / "manifest.json"
    if manifest_file.exists():
        with open(manifest_file, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        
        status_map = {"pending": "⏳", "completed": "✅", "skipped": "⏭️"}
        print(f"\n📊 Status for: {manifest['product_name']}")
        print(f"{'='*50}")
        for layer, status in manifest["layers"].items():
            icon = status_map.get(status, "❓")
            print(f"  {icon} {layer}")
        
        completed = sum(1 for s in manifest["layers"].values() if s == "completed")
        total = len(manifest["layers"])
        print(f"\n📈 Progress: {completed}/{total}")
    else:
        print(f"⚠️  No manifest.json found. The output may be incomplete.")
    
    # Check for required files
    required = [
        "SKILL.md",
        "references/product-brief.md",
        "references/foundational-logic.md",
        "references/output-recipes.md",
        "references/materials-guide.md",
        "agents/openai.yaml",
    ]
    
    print(f"\n📁 File check:")
    for filepath in required:
        full = skill_path / filepath
        exists = full.exists()
        icon = "✅" if exists else "❌"
        print(f"  {icon} {filepath}")


def cmd_generate(args):
    """Generate the complete Skill from filled templates."""
    print("🚀 Generating Skill package...")
    
    output_path = Path(args.output or ".").resolve()
    manifest_file = output_path / "manifest.json"
    
    if not manifest_file.exists():
        print(f"❌ No manifest.json found. Run 'init' first.")
        return
    
    with open(manifest_file, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    name = manifest["product_name"]
    slug = manifest["product_slug"]
    
    print(f"📦 Generating Skill for: {name}")
    
    # Validate each generated file exists
    required_group = [
        ("SKILL.md", "L0_skill_md"),
        ("references/product-brief.md", "L1_product_brief"),
        ("references/foundational-logic.md", "L2_foundational_logic"),
        ("references/output-recipes.md", "L3_output_recipes"),
        ("references/brand-assets.md", "L4_brand_assets"),
        ("references/visual-direction.md", "L5_visual_direction"),
        ("references/materials-guide.md", "L6_materials_guide"),
        ("agents/openai.yaml", None),
    ]
    
    all_complete = True
    for filepath, layer_key in required_group:
        full = output_path / filepath
        if full.exists() and full.stat().st_size > 100:
            if layer_key:
                manifest["layers"][layer_key] = "completed"
            print(f"  ✅ {filepath}")
        else:
            all_complete = False
            if layer_key:
                manifest["layers"][layer_key] = "pending"
            print(f"  ❌ {filepath} - missing or empty")
    
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    if all_complete:
        print(f"\n🎉 All files generated! Output: {output_path}")
    else:
        print(f"\n⚠️  Some files are missing. Check and re-run.")


def cmd_validate(args):
    """Validate the generated Skill against the archetype checklist."""
    skill_path = Path(args.skill).resolve()
    if not skill_path.exists():
        print(f"❌ Path '{skill_path}' not found.")
        return
    
    print(f"\n🔍 Validating Skill at: {skill_path}")
    print(f"{'='*60}")
    
    checks = []
    
    # Structural checks
    structural_checks = [
        ("SKILL.md exists", skill_path / "SKILL.md"),
        ("agents/ directory", skill_path / "agents"),
        ("agents/openai.yaml", skill_path / "agents" / "openai.yaml"),
        ("references/ directory", skill_path / "references"),
        ("assets/ directory", skill_path / "assets"),
    ]
    
    print(f"\n📁 Structure Check:")
    for name, path in structural_checks:
        passed = path.exists()
        icon = "✅" if passed else "❌"
        print(f"  {icon} {name}")
        checks.append(passed)
    
    # Reference file checks
    ref_files = [
        "product-brief.md",
        "foundational-logic.md",
        "output-recipes.md",
        "brand-assets.md",
        "visual-direction.md",
        "materials-guide.md",
    ]
    
    print(f"\n📄 Reference Files:")
    for fname in ref_files:
        full = skill_path / "references" / fname
        passed = full.exists() and full.stat().st_size > 100
        icon = "✅" if passed else "❌"
        print(f"  {icon} references/{fname}")
        checks.append(passed)
    
    # Content checks for SKILL.md
    print(f"\n📝 SKILL.md Content:")
    skill_path_file = skill_path / "SKILL.md"
    if skill_path_file.exists():
        content = skill_path_file.read_text(encoding="utf-8")
        content_checks = [
            ("Has frontmatter (---)", "---" in content),
            ("Has name in frontmatter", "name:" in content),
            ("Has description in frontmatter", "description:" in content),
            ("Has workflow section", "工作流程" in content or "workflow" in content.lower()),
            ("Has 核心信息顺序 or core info order", "核心信息顺序" in content),
            ("Has 不可丢失的事实 or core facts", "不可丢失" in content),
            ("Has 边界与约束 or boundaries", "边界" in content or "constraint" in content.lower()),
            ("Has resources section", "## 资源" in content),
        ]
        for cname, cpassed in content_checks:
            icon = "✅" if cpassed else "❌"
            print(f"  {icon} {cname}")
            checks.append(cpassed)
    
    total = len(checks)
    passed = sum(1 for c in checks if c)
    score = (passed / total) * 100 if total > 0 else 0
    
    print(f"\n{'='*60}")
    print(f"📊 Score: {passed}/{total} ({score:.1f}%)")
    
    if score >= 90:
        print(f"🎉 Excellent! Skill is complete and ready to use.")
    elif score >= 70:
        print(f"⚠️  Good but needs improvement. Fix the failing items.")
    else:
        print(f"❌ Major gaps found. Re-run the generation process.")
    
    return score >= 90


def cmd_package(args):
    """Package the Skill for distribution."""
    skill_path = Path(args.skill).resolve()
    if not skill_path.exists():
        print(f"❌ Path '{skill_path}' not found.")
        return
    
    fmt = args.format or "all"
    name = skill_path.name
    parent = skill_path.parent
    
    if fmt in ("workbuddy", "all"):
        tar_path = parent / f"{name}.tar.gz"
        subprocess.run(["tar", "-czf", str(tar_path), "-C", str(parent), name], check=True)
        print(f"✅ WorkBuddy/OpenClaw package: {tar_path}")
    
    if fmt in ("claude", "all"):
        # Claude Code works well with just the directory structure
        print(f"✅ Claude Code: Use directory directly at {skill_path}")
        print(f"   Add to project context or reference in conversation.")
    
    print(f"\n📦 Package complete!")


def slugify(text):
    """Convert text to URL-safe slug."""
    result = text.lower().strip()
    # Replace common Chinese/Unicode characters
    result = result.replace(" ", "-").replace("《", "").replace("》", "")
    result = result.replace("（", "").replace("）", "").replace("·", "-")
    result = result.replace("「", "").replace("」", "")
    # Keep only ASCII alphanumeric, hyphens, underscores
    import re
    result = re.sub(r'[^a-z0-9\-_]', '', result)
    # Collapse multiple hyphens
    result = re.sub(r'-+', '-', result)
    # Strip leading/trailing hyphens
    result = result.strip('-')
    return result or "product"


def scan_materials(materials_path: Path, output_path: Path):
    """Scan materials directory and report found files."""
    if not materials_path.exists():
        print(f"⚠️  Materials path '{materials_path}' not found.")
        return
    
    print(f"\n📂 Materials found:")
    formats = {
        ".md": "📝",
        ".txt": "📄",
        ".pdf": "📕",
        ".docx": "📘",
        ".pptx": "📙",
        ".xlsx": "📊",
        ".csv": "📋",
        ".png": "🖼️",
        ".jpg": "🖼️",
        ".jpeg": "🖼️",
        ".svg": "🎨",
        ".webp": "🖼️",
        ".json": "📋",
        ".yaml": "🔧",
        ".yml": "🔧",
        ".html": "🌐",
        ".htm": "🌐",
    }
    
    for f in sorted(materials_path.rglob("*")):
        if f.is_file() and not f.name.startswith("."):
            ext = f.suffix.lower()
            icon = formats.get(ext, "📦")
            size_kb = f.stat().st_size / 1024
            rel = f.relative_to(materials_path)
            print(f"  {icon} {rel} ({size_kb:.0f} KB)")
    
    print(f"\n💡 Tip: Materials will be reshaped to Markdown during generation.")


def main():
    parser = argparse.ArgumentParser(
        description="Meta-Skill Product Architect — Generate standardized product introduction Skills",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # init
    p_init = subparsers.add_parser("init", help="Initialize a new product analysis session")
    p_init.add_argument("--name", "-n", required=True, help="Product name")
    p_init.add_argument("--materials", "-m", required=True, help="Path to product materials")
    p_init.add_argument("--output", "-o", help="Output directory (default: introduce-{product-name})")
    p_init.add_argument("--force", "-f", action="store_true", help="Overwrite existing output")
    
    # scan
    p_scan = subparsers.add_parser("scan", help="Scan output directory and report status")
    p_scan.add_argument("--skill", "-s", required=True, help="Path to Skill output directory")
    
    # generate
    p_gen = subparsers.add_parser("generate", help="Generate the complete Skill package")
    p_gen.add_argument("--output", "-o", help="Output directory (default: current)")
    
    # validate
    p_val = subparsers.add_parser("validate", help="Validate generated Skill against checklist")
    p_val.add_argument("--skill", "-s", required=True, help="Path to Skill output directory")
    
    # package
    p_pkg = subparsers.add_parser("package", help="Package Skill for distribution")
    p_pkg.add_argument("--skill", "-s", required=True, help="Path to Skill output directory")
    p_pkg.add_argument("--format", "-f", choices=["workbuddy", "claude", "all"], default="all", help="Target platform")
    
    args = parser.parse_args()
    
    if args.command == "init":
        cmd_init(args)
    elif args.command == "scan":
        cmd_scan(args)
    elif args.command == "generate":
        cmd_generate(args)
    elif args.command == "validate":
        cmd_validate(args)
    elif args.command == "package":
        cmd_package(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
