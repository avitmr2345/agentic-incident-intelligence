# Incident Severity and Priority Policy

## Purpose
This policy defines how production incidents are classified, prioritized, communicated, and escalated. Severity should reflect customer and business impact rather than the technical component that failed.

## Severity Levels

### SEV-1 — Critical
A widespread or business-critical failure that prevents a major platform capability from functioning.

Examples:
- Authentication is unavailable for most users.
- Orders cannot be created across the platform.
- A major payment failure affects a large portion of transactions.
- A cascading failure is causing rapid customer impact.

Expected response:
- Immediate incident declaration.
- Incident commander assigned.
- Engineering responders from affected services engaged.
- Continuous monitoring and communication until recovery.
- Recovery takes priority over non-critical engineering work.

### SEV-2 — Major
A significant degradation affecting an important capability or a substantial subset of users, but with a viable workaround or limited scope.

Examples:
- Elevated order failures in one region or traffic segment.
- Significant payment latency with some successful transactions.
- Notification delivery delays affecting a meaningful subset of customers.
- Repeated API 5xx responses from one service.

### SEV-3 — Moderate
A limited production issue with relatively small customer impact or a temporary degradation.

Examples:
- Elevated latency on a non-critical endpoint.
- Intermittent failures affecting a small percentage of requests.
- Delayed notifications with no loss of events.

### SEV-4 — Minor
A low-impact issue that does not materially affect normal customer operations.

Examples:
- Non-critical observability gaps.
- Minor configuration inconsistencies.
- Documentation or operational issues discovered during normal work.

## Priority Rules
Severity is determined using:
1. Customer impact.
2. Scope of affected functionality.
3. Duration and rate of failure.
4. Data integrity or security implications.
5. Likelihood of cascading failure.
6. Availability of workarounds.

A technically complex failure is not automatically high severity.

## Escalation
Escalate when:
- Impact expands beyond the original scope.
- Recovery attempts are ineffective.
- A dependency is causing cascading failures.
- Data integrity or security risk is discovered.
- The root cause remains uncertain while impact continues.

## Incident Closure
An incident should be closed only after:
- Customer-facing impact has recovered.
- Relevant health and error metrics have returned to expected levels.
- No continuing backlog or dependency failure remains.
- A follow-up investigation is recorded when appropriate.

## Related Knowledge
This policy should be used with the incident runbooks, historical incident reports, observability architecture, and deployment/change-management policy.
