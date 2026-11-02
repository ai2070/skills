---
name: bounded-agent-delegation
description: "Delegate a narrow work package with explicit authority and independently checked results."
---
# Bounded Agent Delegation

## When to use
- A coding or investigation task benefits from a separate worker.
- Independent review is warranted by a material risk.

## Inputs
- One concrete deliverable with observable acceptance criteria.
- Allowed files, tools, environments, and external side effects.
- Starting revision or preserved dirty-tree baseline.
- Time, attempt, cost, and escalation limits appropriate to the task.

## Workflow
1. Decide whether delegation is useful.
   - Keep trivial work direct when handoff overhead exceeds the benefit.
   - Start with one implementer rather than a hierarchy of coordinators.
   - Add parallel workers only for independent, non-overlapping work.
2. Prepare a bounded work packet.
   - State the goal, exclusions, relevant files, and existing evidence.
   - Specify acceptance tests and the required output format.
   - Include known failures and local edits that must be preserved.
3. Define authority explicitly.
   - State whether the worker may edit, execute tests, install, or use network.
   - Deny implicit permission to publish, merge, deploy, or alter shared services.
   - User and harness approvals prevail; prose is not a sandbox or access control.
   - Use available isolation and least-privilege access; do not bypass restrictions.
4. Prevent conflicting ownership.
   - Assign disjoint files or an authorized isolated checkout per implementer.
   - Reserve shared integration points for one owner.
   - Do not overwrite concurrent work when collecting results.
5. Monitor with bounded checkpoints.
   - Request concise progress, blockers, changed paths, and test evidence.
   - Stop scope growth, repeated unsupported guesses, or excessive retries.
   - Escalate with preserved evidence rather than restarting investigation blindly.
6. Independently inspect the returned artifact.
   - Treat the worker summary as a lead, not a trusted acceptance result.
   - Compare actual changes with scope and the preserved baseline.
   - Re-run decisive checks and inspect exact targets of external changes.
7. Integrate only verified work.
   - Resolve conflicts explicitly and test the combined result.
   - Use a focused independent reviewer when risk justifies it.
   - Add specialists only for distinct risks not covered by the first review.
   - Keep unverified or blocked criteria open in the final status.

## Verification
- Confirm actual changed paths, behavior, and permissions match the packet.
- Verify test commands and results rather than repeating claimed test counts.
- Validate the integrated revision, not only isolated worker branches.
- Check unrelated work and shared state for unintended modifications.
- Distinguish implementation, review, integration, and runtime acceptance.

## Output
- Accepted deliverable, changed paths, and independently observed evidence.
- Rejected or incomplete work with the specific unmet criterion.
- Remaining risks, approvals, and known resource usage when available.

## Avoid
- Nested delegation without a concrete need and explicit authority.
- Giving every worker full credentials or broad write access.
- Treating a model label, confident summary, or green checklist as evidence.
- Claiming cost savings without comparable end-to-end usage data.
