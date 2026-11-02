---
name: verified-github-delivery
description: "Deliver authorized Git changes and verify the exact remote revision and pull request state."
---
# Verified GitHub Delivery

## When to use
- An authorized request to commit, push, or open a GitHub pull request.
- Verifying whether a specific revision reached the intended remote branch.

## Inputs
- Repository identity, remote owner and name, source branch, and target branch.
- Approved files or hunks and requested delivery stage.
- Acceptance checks, required CI checks, and review requirements.
- Available authentication without exposing credentials.

## Workflow
1. Confirm destination and authority.
   - Inspect the repository root, remote URLs, current branch, and status.
   - Distinguish permission to edit, commit, push, create a PR, and merge.
   - User and harness approvals prevail; stop at the authorized stage.
2. Preserve the starting work state.
   - Inspect staged, unstaged, and untracked changes before staging anything.
   - Record which changes belong to this task and which predate it.
   - If unrelated staged work cannot be safely separated, stop for guidance.
3. Validate the intended patch.
   - Inspect the task delta for secrets, generated noise, and accidental deletions.
   - Run relevant checks and record the exact revision or dirty-tree context.
   - Do not claim runtime acceptance from compilation or unit tests alone.
4. Stage and commit only authorized content.
   - Use explicit paths or selected hunks, never blanket staging.
   - Inspect the staged diff and file list immediately before committing.
   - Verify the resulting commit contents and record its full SHA.
5. Push to the explicit authorized destination.
   - Confirm remote and branch again before a state-changing command.
   - Use a normal push; handle divergence without rewriting others' history.
   - Read the remote branch ref back and compare it with the intended SHA.
6. Create or update a pull request only when requested.
   - Verify repository, head branch, base branch, title, and body.
   - Include a concise change summary and actual validation evidence.
   - Read back the exact PR and confirm its head SHA and destination.
7. Inspect checks and stop at the agreed boundary.
   - Read applicable required checks for the current PR head revision.
   - Treat pending, missing, skipped, stale, and failing results distinctly.
   - If requirements cannot be discovered, report that verification gap.
   - Merge, auto-merge, releases, and deployments require separate scope.

## Verification
- Confirm local commit SHA equals the intended remote branch SHA after push.
- Confirm the PR head SHA matches the delivered revision, if a PR is involved.
- Report required checks individually when they block acceptance.
- Recheck local status to ensure unrelated work remains intact.
- A successful push does not prove CI completion, approval, merge, or deployment.

## Output
- Commit SHA, destination branch, and PR URL when applicable.
- Verified check state and the delivery stage actually reached.
- Remaining blockers or actions requiring approval.

## Avoid
- Blanket add, restore, reset, cleanup, or force-push operations.
- Silently changing remotes, branch protections, or required checks.
- Publishing secrets or private material in diffs, commit messages, or PR text.
- Reporting delivery from a command exit status without remote readback.
