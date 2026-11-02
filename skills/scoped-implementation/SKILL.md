---
name: scoped-implementation
description: "Implement a bounded change while preserving existing work and verifying acceptance."
---
# Scoped Implementation

## When to use
- Adding or changing behavior in an existing codebase.
- Delivering a small, testable slice of a larger feature.

## Inputs
- Desired behavior and observable acceptance criteria.
- Allowed files, interfaces, environments, and side effects.
- Repository instructions and available validation commands.
- Known constraints, exclusions, and approval requirements.

## Workflow
1. Establish scope before editing.
   - Translate the request into observable success and failure cases.
   - Resolve ambiguity that changes permissions, data handling, or architecture.
   - User and harness approval requirements prevail over this procedure.
2. Inspect the project and preserve its starting state.
   - Identify the actual project root, entry points, and relevant tests.
   - Record staged, unstaged, and untracked work without exposing secrets.
   - Preserve a diff or content baseline for files you may touch.
3. Trace the smallest complete implementation path.
   - Follow inputs through validation, processing, persistence, and output.
   - Note compatibility requirements and likely failure boundaries.
   - Avoid unrelated cleanup and speculative infrastructure.
4. Establish validation before changing behavior.
   - Run relevant baseline checks where safe; record existing failures.
   - Add a focused acceptance or regression test when practical.
   - Inspect test configuration before allowing database or network access.
5. Implement only the agreed slice.
   - Reuse project conventions and keep public contracts explicit.
   - Stop for approval if new dependencies or wider permissions are needed.
   - Preserve concurrent edits; investigate unexpected changes before proceeding.
6. Exercise the change and inspect the final delta.
   - Run focused checks, then affected integration checks as warranted.
   - Exercise the real entry point when acceptance requires runtime behavior.
   - Compare against the starting baseline, not only the latest commit.

## Verification
- Match each acceptance criterion to observed evidence or a stated blocker.
- Confirm unrelated work remains intact and no secrets entered the change.
- Separate compilation, unit tests, integration tests, and runtime evidence.
- Use an independent review for material correctness or security risks.
- Treat unavailable checks as unverified, not implicitly successful.

## Output
- Changed behavior and exact files affected.
- Commands or probes run, their results, and remaining limitations.
- Any scope decisions or approvals still needed.

## Avoid
- Broad formatting, dependency upgrades, or redesign outside the request.
- Blanket staging, resetting, restoring, or deleting unrelated work.
- Disabling guards or escaping isolation to make a check pass.
- Treating local implementation as permission to publish, merge, or deploy.
