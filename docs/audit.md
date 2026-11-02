# Skill-library audit

## Scope and evidence

The structural scan enumerated **139 non-hidden installed `SKILL.md` files** in the default-profile library. The three content-review partitions covered 21 coding/agent packages, 88 other packages and 30 productivity/knowledge/business/operations packages. Installed does not mean enabled. Hidden archives, plugin-provided skills and other profiles are excluded from the baseline inventory. Support files were sampled or statically scanned, not comprehensively executed. Reviewers inspected some archive existence to distinguish missing exports from lost local files.

A YAML-aware local scan checked all enumerated frontmatter. The export's lightweight validator is separate and accepts only this pack's minimal format. None of the original workflows was certified against every live external service.

## Structural screening results

These are overlapping triage categories, not independent confirmed vulnerabilities. Counts describe the **pre-edit source baseline**, not the rewritten pack.

| Screening category | Skill bodies flagged |
| --- | ---: |
| `archive_dependency` | 12 |
| `machine_paths` | 18 |
| `name_directory_mismatch` | 1 |
| `nonportable_metadata` | 90 |
| `outline_instead_of_workflow` | 12 |
| `over_500_lines` | 9 |
| `personal_context` | 36 |
| `unresolved_support_path_mentions` | 25 |

`unresolved_support_path_mentions` includes historical inventories and example paths; it is not a definitive broken-link count. Nested Hermes metadata may be valid in Hermes while not matching the portable standard's string-to-string metadata map. Personal-context and machine-path flags require review; examples are not automatically disclosures.

## Prioritized findings and treatment

| Priority | Finding | Treatment |
| --- | --- | --- |
| Critical | Some computer-use guidance suggested splitting blocked commands; sandbox failure guidance recommended unsandboxed retries | Removed the bypass recommendation from two installed computer-use skills and one installed Codex skill after backing up their entry points. Portable workflows preserve refusals. Other specialized packages still need review. |
| High | Personal, clinical, contact and deployment context exists in bodies and support files | Excluded raw packages and support material. Export consists of newly worded, manually reviewed procedures. No private evidence is included here. |
| High | Consolidated umbrellas list old headings and depend on hidden archives | Replaced selected coding workflows with complete standalone instructions; no archive dependency in this pack. Broader source packaging remains open. |
| High | Some read-only workflows recommend syncs, edits or persistent writes | Portable procedures distinguish observation from authorized mutation. Original testing/measurement skills remain open remediation work. |
| High | Blanket staging/restoration can capture or destroy pre-existing work | Require preserved baselines, explicit scoped changes, reviewed staging and rollback of only task-owned changes. |
| High | Browser recovery can forward sensitive URLs; webhook examples lack explicit trust boundaries | Do not export these helpers. They require targeted code/security remediation before future inclusion. |
| Medium | Repeated mandatory reviewers and contradictory delegation rules increase cost and weaken evidence | Use bounded independent tasks, risk-scaled review and controller verification of decisive artifacts. |
| Medium | Stale tool APIs and machine-specific paths are embedded in reusable procedures | Use capability discovery and project-derived commands rather than assumed harness tool names. |
| Medium | Syntax checks, worker assertions and retries are presented as stronger evidence than they establish | Separate structural tests, actual behavioral tests, remote persistence and live user-visible acceptance. |

## Publication boundary

This release contains seven curated skills plus a validator, no-overwrite project installer, tests and documentation. It is **not a full-library migration or a claim that all findings are fixed**. Local backup and detailed path-level inventory stay outside public Git history. Personal knowledge-base authority conflicts, unsafe specialized defaults, missing shared references and original script defects remain follow-up work.

## Remaining verification limits

- Automated tests validate this export's format and installer, not model compliance.
- No actual Codex/Claude task execution is claimed; discovery paths are documentation-grounded.
- Privacy screening is heuristic plus content review, not a guarantee or comprehensive secret-scanner result.
- No third-party helper scripts or source archives are included. License selection remains explicit rather than inheriting inconsistent source metadata.
