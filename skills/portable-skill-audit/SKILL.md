---
name: portable-skill-audit
description: "Audit and package reusable agent skills. Use when reviewing instruction libraries, fixing stale procedures, or sharing workflows across coding agents."
---
# Portable skill audit

## When to use
Audit an instruction library or prepare a curated cross-agent release. This is not permission to publish private source material or install tools.

## Inputs
Source roots, intended audience, target agents, publication visibility, and authorized edit scope. Discover repository ownership and existing destinations before creating another repository.

## Workflow
1. Enumerate installed packages in code. Distinguish installed, enabled, archived, plugin-provided and other-profile skills. Record coverage and exclusions; do not call a sampled review exhaustive.
2. Read complete selected bodies and their referenced files. Separate executable procedures from historical headings, task logs, personal context and runtime adapters. Inventory dependencies before deleting or consolidating a package.
3. Check frontmatter against the target format, duplicate names, broken links, missing scripts, oversized bodies, contradictory rules and assumptions about tool availability. A syntax pass is not behavioral validation.
4. Review safety boundaries: read-only claims versus actual writes, bypass instructions, network egress, secrets, destructive cleanup, and approval scope. Reproduce suspected script defects only in an isolated fixture without real credentials or external writes.
5. Preserve a recoverable baseline before installed edits. Prefer targeted corrections over replacing the library. Keep personal deployment configuration and historical permissions outside portable procedures.
6. Build a small self-contained export. Write concrete inputs, numbered actions, verification, output and failure boundaries. Bundle every required dependency, or remove the dependency by distilling the procedure. Do not require hidden local archives.
7. Inspect the entire export for private data, including support files, generated artifacts and Git history. An automated pattern scan assists review but does not prove confidentiality. Preserve applicable third-party notices and do not invent provenance or licensing authority.
8. Validate structure and run safe helper tests. Exercise a target-agent pilot when available; otherwise label compatibility as format/documentation-based, not end-to-end tested.
9. Publish only the reviewed allowlist to the authorized destination and visibility. Read back the remote branch commit and file inventory. Preserve the local audit and rollback artifact outside public history.

## Verification
Compare enumerated versus reviewed counts programmatically. Check link closure and unique names. Verify helper behavior, no-overwrite installation and unchanged excluded files. Distinguish published fixes from findings still open in the original library.

## Output
Report scope, prioritized findings, applied changes, tests actually run, compatibility limits, destination URL and exact revision. Include the private rollback location only in the private handoff.

## Avoid
Bulk-exporting a home directory; treating name redaction as privacy review; claiming Markdown enforces a sandbox; blanket license reassignment; running arbitrary source scripts during lint; claiming all skills were repaired when only a curated subset was rewritten.
