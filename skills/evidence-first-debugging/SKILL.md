---
name: evidence-first-debugging
description: "Investigate failures from preserved evidence and verify a causal repair."
---
# Evidence-First Debugging

## When to use
- A reproducible defect, intermittent failure, or unexplained regression.
- A recovery action succeeds but the original cause remains uncertain.

## Inputs
- Expected behavior, observed behavior, and affected entry point.
- Error evidence, relevant versions, and recent changes.
- Authorized environments, diagnostic access, and impact limits.
- Existing local changes and available regression tests.

## Workflow
1. Set the investigation boundary.
   - Identify the exact service, repository, record, or request affected.
   - Confirm which probes and state changes are permitted.
   - User and harness approvals prevail; diagnostics do not expand access.
2. Preserve evidence before recovery.
   - Capture redacted errors, timing, request identifiers, and state transitions.
   - Record relevant configuration names without copying secret values.
   - Preserve local edits before changing instrumentation or source.
3. Reproduce safely with the smallest representative case.
   - Record inputs, environment, expected result, and actual result.
   - Prefer isolated fixtures over production writes.
   - If intermittent, bound attempts and record both failures and successes.
4. Locate the first failing boundary.
   - Trace input, validation, transport, processing, storage, and response.
   - Compare a successful case with a failing case at that boundary.
   - Distinguish observed facts from candidate explanations.
5. Test one causal hypothesis at a time.
   - State what observation would support or disprove it.
   - Prefer a narrow probe over broad resets or dependency changes.
   - Add minimal redacted diagnostics only where evidence is missing.
6. Repair the supported cause.
   - Add a regression that fails for the original condition where possible.
   - Apply the smallest correction without weakening safety controls.
   - Remove unnecessary diagnostic changes and preserve useful safe logging.
7. Re-run the failing path and adjacent checks.
   - Verify the repaired condition, a normal case, and a relevant negative case.
   - Exercise the actual entry point if runtime access is authorized.
   - Stop and report a precise evidence gap when the cause remains unknown.

## Verification
- Confirm the regression detects the defect, not merely the new implementation.
- Inspect the final diff against the preserved baseline.
- Distinguish restored availability from demonstrated root-cause resolution.
- Distinguish mocked tests from real transport, storage, or runtime evidence.
- Check that logs and test artifacts contain no credentials or private payloads.

## Output
- Observed failure, supported cause, and correction made.
- Reproduction and verification results, with environmental limitations.
- Recovery status and unresolved recurrence risk stated separately.

## Avoid
- Restarting, clearing caches, or resetting credentials before preserving evidence.
- Calling a successful retry proof that an intermittent defect is fixed.
- Disabling authentication, validation, isolation, or permission checks.
- Presenting a plausible hypothesis as a confirmed diagnosis.
