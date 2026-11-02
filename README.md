# Portable coding-agent skills

A curated, self-contained pack distilled from an audit of a working agent skill library. These are executable workflows in plain Markdown—not a dump of personal configuration, a tool integration, or a sandbox.

## Skills

| Skill | Use it for |
| --- | --- |
| `scoped-implementation` | Deliver a bounded change without disturbing unrelated work |
| `evidence-first-debugging` | Reproduce a failure and verify a causal fix |
| `risk-based-code-review` | Review real diffs with actionable, evidence-backed findings |
| `verified-github-delivery` | Commit, push and verify authorized GitHub changes |
| `bounded-agent-delegation` | Delegate independent work without losing accountability |
| `safe-service-operations` | Diagnose and change services with rollback and verification |
| `portable-skill-audit` | Audit and safely export reusable workflows |

Each skill has inputs, a numbered workflow, verification, an output contract and anti-patterns. No proprietary tool names, hidden archive dependencies, private deployment details or inherited standing permissions are required.

## Use with Codex or Claude Code

Requires Python 3.10+ for the optional installer and checks. No Python packages need installing.

```sh
git clone https://github.com/ai2070/skills.git
cd skills
python3 scripts/validate.py
python3 -m unittest discover -s tests -v

# Preview a project-local Codex installation. The project must already exist.
python3 scripts/install.py --target codex --project /path/to/project \
  --skill scoped-implementation --skill evidence-first-debugging

# Repeat with --apply to copy only those selected skills.
python3 scripts/install.py --target codex --project /path/to/project \
  --skill scoped-implementation --skill evidence-first-debugging --apply
```

For Claude Code, use `--target claude`. Destinations are `<project>/.agents/skills/` for Codex and `<project>/.claude/skills/` for Claude Code. Use real project paths, not symlinks. The installer refuses collisions rather than overwriting existing instructions, does not edit `AGENTS.md` or `CLAUDE.md`, and does not change global configuration. Review and remove or archive an existing copy yourself before updating it. This installer assumes a trusted local filesystem, not concurrent adversarial writers.

Start a new agent session and confirm the selected skills are listed. Invoke `$scoped-implementation` in Codex or `/scoped-implementation` in Claude Code. If discovery differs in your installed version, consult its documentation; copying files alone does not prove the agent loaded them.

For another Agent Skills-compatible agent, copy a selected `skills/<name>/` directory to its documented skill directory. For a tool without skill discovery, explicitly load the selected `SKILL.md`; do not indiscriminately inject the entire pack.

## Safety and verification

Skills never grant permission. The user's scope and the host's approval, sandbox and access controls remain authoritative. Read-only work stays read-only; publishing, deployment and destructive actions require the appropriate scope. Do not disable protections to follow a workflow.

The validator checks this pack's deliberately narrow frontmatter format, required sections, file budget, local links, archive references and a few privacy patterns. It is **not** a comprehensive secret scanner, full YAML implementation or behavioral evaluation. The installer supports only these standalone packages and rejects unreviewed support files.

See [audit findings](docs/audit.md), [provenance and scope](docs/provenance.md), and [manual behavioral checks](docs/evaluation.md). Format and installation checks do not establish end-to-end success in every coding agent.

## Sources for integration paths

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skill documentation](https://code.claude.com/docs/en/skills)

## Licensing

No blanket license has been assigned to the audited source library or to this initial publication. Public visibility is not an open-source license. Personal reuse by the repository owner is the immediate goal; third-party redistribution requires an explicit licensing decision. No upstream helper scripts or archived packages are bundled.
