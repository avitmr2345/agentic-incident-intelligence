# Incident Postmortem and Learning Policy

## Purpose
This policy defines how significant incidents should be documented so that the organization can learn from failures and improve system reliability.

## When to Create a Postmortem
A postmortem is appropriate for:
- High-severity incidents.
- Repeated incidents.
- Significant customer impact.
- Data integrity problems.
- Cascading failures.
- Incidents that reveal an important architectural weakness.

## Required Sections
A postmortem should contain:

### Summary
A concise description of what happened and the impact.

### Timeline
Important events should be recorded in chronological order:
- First observed symptom.
- Detection.
- Investigation milestones.
- Mitigation.
- Recovery.
- Follow-up actions.

### Impact
Document:
- Affected functionality.
- Approximate scope.
- Duration.
- Customer or operational impact.

### Root Cause
Describe the technical condition that caused the incident.

Avoid stopping at the first visible symptom.

For example, an Order API 503 may be a symptom while the deeper cause is a payment dependency timeout.

### Contributing Factors
Record conditions that increased the likelihood or impact, such as:
- Missing timeout controls.
- Excessive retries.
- Poor dependency isolation.
- Configuration drift.
- Insufficient monitoring.
- Backward-incompatible changes.

### Detection
Document which signals detected the incident:
- Metrics.
- Logs.
- Traces.
- Health checks.
- Customer reports.

### Resolution
Record the actions that restored service.

### Corrective Actions
Actions should be specific and measurable.

Examples:
- Add dependency timeout.
- Add alert for queue growth.
- Improve readiness validation.
- Add idempotency protection.
- Correct deployment compatibility checks.

## Evidence
Postmortems should reference the relevant:
- Services.
- APIs.
- Runbooks.
- Logs.
- Metrics.
- Traces.
- Historical incidents.

This creates reusable operational knowledge.

## Reuse of Historical Knowledge
Before concluding an incident investigation, engineers should check whether a similar historical incident exists.

Historical incidents can provide:
- Known root causes.
- Previously successful mitigations.
- Important investigation signals.
- Known failure patterns.

## Learning Loop
Postmortems should lead to improvements in:
- Architecture.
- Monitoring.
- Runbooks.
- Deployment practices.
- API contracts.
- Reliability controls.

The goal is learning and system improvement, not assigning blame.

## Related Knowledge
This policy connects the historical incident reports with runbooks, architecture documentation, operational policies, and future incident investigations.
