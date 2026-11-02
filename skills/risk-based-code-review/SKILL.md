---
name: risk-based-code-review
description: "Review a precise change with evidence and effort proportional to its risks."
---
# Risk-Based Code Review

## When to use
- Assessing a patch, pull request, or proposed implementation before acceptance.
- Checking correctness, security, compatibility, or operational impact.

## Inputs
- Exact revision or preserved working-tree baseline and proposed delta.
- Requirements, acceptance criteria, and relevant project conventions.
- Test evidence, known failures, and deployment context.
- Review permissions and whether fixes are explicitly authorized.

## Workflow
1. Fix the review target.
   - Identify the base, head, changed files, and any uncommitted changes.
   - Check that supplied test evidence refers to this revision.
   - Read-only review stays read-only unless editing is separately authorized.
2. Estimate risk from consequences, not patch size alone.
   - Examine authentication, data loss, concurrency, migrations, and public APIs.
   - Include sensitive data exposure and rollback difficulty.
   - Use one focused reviewer by default; add expertise for distinct high risks.
3. Read the change in context.
   - Inspect callers, data contracts, configuration, and error paths.
   - Compare implemented behavior with explicit acceptance criteria.
   - Trace important values across boundaries instead of reviewing lines alone.
4. Investigate concrete failure scenarios.
   - Check malformed inputs, partial failures, retries, and concurrent actions.
   - Look for authorization gaps, secret leakage, and unsafe defaults.
   - Prioritize reachable defects over speculative style preferences.
5. Evaluate evidence without trusting summaries alone.
   - Inspect actual tests and identify assertions that could miss the defect.
   - Run safe focused checks if permitted; inspect their side effects first.
   - User and harness approvals prevail over suggested review commands.
6. Report actionable findings.
   - Give each finding a location, triggering condition, impact, and rationale.
   - Label severity by consequence and likelihood; state uncertainty explicitly.
   - Separate blocking defects from optional improvements and questions.
7. Reassess repairs against the updated target.
   - Check the corrective delta and rerun affected checks when authorized.
   - Confirm earlier evidence still applies; stale evidence is not acceptance.
   - Do not silently fix, commit, merge, or deploy during a review-only task.

## Verification
- Confirm the reviewed revision and record any files not inspected.
- Ensure claimed defects have a credible path or reproducible evidence.
- Identify missing runtime checks separately from passing static tests.
- Confirm review commands did not alter tracked or unrelated local work.
- Report no findings as a bounded result, not proof of defect-free software.

## Output
- Findings ordered by severity, with precise locations and suggested remedies.
- Requirement coverage, checks performed, and unverified risk areas.
- A recommendation tied to this revision and the applicable acceptance gates.

## Avoid
- Mandatory multi-reviewer hierarchies for every small change.
- Inflating formatting preferences into correctness blockers.
- Accepting implementer or subagent self-reports as independent proof.
- Generating files, installing packages, or changing state without scope.
