#!/usr/bin/env python3
"""Validate this pack's intentionally small Agent Skills frontmatter subset.

This is a structural and heuristic privacy check, not a secret scanner or
behavioral certification. It never runs skill commands or fetches links.
"""
import argparse
import json
from pathlib import Path
import re
import sys

SECTIONS = ('When to use', 'Inputs', 'Workflow', 'Verification', 'Output', 'Avoid')
PRIVATE = re.compile(r'/Users/[^/\s]+|/home/[^/\s]+|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|\bsk-[A-Za-z0-9]{24,}')
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')


def validate(root):
    root = Path(root).resolve()
    errors = []
    paths = sorted((root / 'skills').glob('*/SKILL.md'))
    if not paths:
        errors.append('No skills found')
    for p in paths:
        label = str(p.relative_to(root))
        if p.is_symlink() or p.parent.is_symlink():
            errors.append(f'{label}: symlinks are not distributable')
            continue
        text = p.read_text(encoding='utf-8')
        match = re.match(r'\A---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: (.+)\n---\n', text)
        if not match:
            errors.append(f'{label}: expected name and JSON-quoted description frontmatter')
            continue
        name, raw = match.groups()
        try:
            description = json.loads(raw)
        except ValueError:
            description = None
        if name != p.parent.name or len(name) > 64:
            errors.append(f'{label}: invalid or mismatched name')
        if not isinstance(description, str) or not 1 <= len(description) <= 1024:
            errors.append(f'{label}: invalid description')
        if len(text.splitlines()) > 120:
            errors.append(f'{label}: exceeds pack budget of 120 lines')
        for section in SECTIONS:
            if f'## {section}\n' not in text:
                errors.append(f'{label}: missing {section}')
        if PRIVATE.search(text):
            errors.append(f'{label}: potential private data; inspect locally')
        if '.archive/' in text:
            errors.append(f'{label}: archive dependency')
        for target in LINK.findall(text):
            target = target.split('#', 1)[0]
            if not target or re.match(r'https?://', target):
                continue
            resolved = (p.parent / target).resolve()
            if not resolved.is_relative_to(p.parent.resolve()) or not resolved.is_file():
                errors.append(f'{label}: missing or out-of-package link')
    for p in (root / 'skills').rglob('*'):
        if p.is_symlink():
            errors.append(f'{p.relative_to(root)}: symlink')
        elif p.is_file() and p.name != 'SKILL.md':
            errors.append(f'{p.relative_to(root)}: unreviewed support file')
    return {'skills': len(paths), 'errors': errors, 'ok': not errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate(args.root)
    print(json.dumps(result, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
