#!/usr/bin/env python3
"""Copy selected skills into a project. Dry-run unless --apply is supplied."""
import argparse
import json
from pathlib import Path
import shutil
import sys
from validate import validate

TARGETS = {'codex': '.agents/skills', 'claude': '.claude/skills'}


def install(source, project, target, names, apply=False):
    source, project = Path(source).resolve(), Path(project).absolute()
    if not project.is_dir():
        raise ValueError('Project must be an existing directory')
    if any(p.is_symlink() for p in [project, *project.parents]):
        raise ValueError('Use a real project path, not a symlink')
    if target not in TARGETS:
        raise ValueError('Unknown target')
    result = validate(source)
    if not result['ok']:
        raise ValueError('Source validation failed: ' + '; '.join(result['errors']))
    available = {p.parent.name for p in (source / 'skills').glob('*/SKILL.md')}
    if not names or len(names) != len(set(names)) or not set(names) <= available:
        raise ValueError('Select unique existing skill names')
    base = project / TARGETS[target]
    for p in [base, *base.parents]:
        if p.is_symlink():
            raise ValueError('Destination must not contain symlinks')
        if p.exists() and not p.is_dir():
            raise ValueError('Destination ancestor is not a directory')
    destinations = [base / name for name in names]
    if any(p.exists() or p.is_symlink() for p in destinations):
        raise FileExistsError('A selected skill already exists; nothing was changed')
    if apply:
        base.mkdir(parents=True, exist_ok=True)
        created = []
        try:
            for name, dest in zip(names, destinations):
                dest.mkdir()  # Exclusive creation; never overwrite an existing skill.
                created.append(dest)
                src = source / 'skills' / name / 'SKILL.md'
                shutil.copyfile(src, dest / 'SKILL.md')
                if src.read_bytes() != (dest / 'SKILL.md').read_bytes():
                    raise OSError('Installed content differs from source')
        except Exception:
            for dest in reversed(created):
                shutil.rmtree(dest)
            raise
    return {'applied': apply, 'skills': list(names), 'destinations': [str(p) for p in destinations]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, type=Path)
    parser.add_argument('--target', choices=TARGETS, required=True)
    parser.add_argument('--skill', action='append', required=True)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parents[1], args.project, args.target, args.skill, args.apply)
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
