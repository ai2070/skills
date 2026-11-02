---
name: safe-service-operations
description: "Inspect and change services within explicit scope with recovery planning and live verification."
---
# Safe Service Operations

## When to use
- Diagnosing service health, configuration, connectivity, or startup failures.
- Performing an authorized restart, configuration change, or deployment.

## Inputs
- Exact environment, service identity, owner, and desired outcome.
- Allowed operations, maintenance constraints, and impact tolerance.
- Current version, configuration source, and service supervisor if applicable.
- Health criteria, recovery options, and access approval requirements.

## Workflow
1. Establish identity and permissions before operating.
   - Confirm the host or account, environment, service, and data dependencies.
   - Separate read-only diagnosis from permission to restart or change state.
   - User and harness approvals prevail; never work around denied access.
2. Gather read-only evidence first.
   - Inspect health, supervisor state, bounded logs, and relevant configuration.
   - Check the actual listener and process identity rather than guessing from names.
   - Redact secrets and private request content from collected evidence.
3. Preserve the current state and define recovery.
   - Record deployed version, relevant configuration, and observed failure.
   - Preserve local edits and avoid capturing secret values in reports.
   - For approved mutations, identify a recovery target and rollback trigger.
   - Verify backup and restore feasibility before data-changing operations.
4. Choose the smallest authorized intervention.
   - Prefer scoped configuration or service actions over host-wide changes.
   - Validate syntax and dependencies without activating changes when possible.
   - Obtain approval for wider impact, privileged access, or new installations.
   - Treat irreversible migrations as separate decisions, not ordinary rollback.
5. Apply one bounded change.
   - Use the existing supervisor or deployment mechanism where appropriate.
   - Do not create persistent jobs or expose listeners beyond approved scope.
   - Bound retries and waits; stop on unexpected impact or data risk.
6. Verify the exact live target independently.
   - Read back active version or configuration through an appropriate safe view.
   - Check health, authenticated access, and a representative user path.
   - Verify expected denial behavior and dependent storage or network boundaries.
   - After an approved restart, confirm the intended supervisor owns the process.
7. Recover or escalate when verification fails.
   - Use the agreed rollback only when authorized and safe for current data.
   - Verify the restored target; a rollback command alone proves nothing.
   - Preserve failure evidence and state precisely what remains unavailable.

## Verification
- Separate process existence, listener availability, health, and usable behavior.
- Confirm the service identity and revision match the intended environment.
- Use a bounded follow-up check to detect immediate exits or restart loops.
- Distinguish successful builds and tests from live service acceptance.
- Confirm no unrelated services, permissions, or network exposure changed.

## Output
- Exact target, action taken, and observed before-and-after state.
- Live checks performed, recovery status, and unresolved risks.
- Any missing permissions or evidence preventing completion.

## Avoid
- Mutating a service during a read-only audit or health question.
- Broad process kills, unrestricted firewall changes, or unsandboxed fallbacks.
- Deleting logs, caches, or data before preserving diagnostic evidence.
- Calling a temporary launch durable service operation or guaranteed uptime.
