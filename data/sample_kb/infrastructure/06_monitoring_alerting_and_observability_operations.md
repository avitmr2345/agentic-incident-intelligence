# Monitoring, Alerting, and Observability Operations

## Purpose
This document defines the operational observability signals used to detect and investigate incidents.

## Three Primary Signals

### Logs
Logs provide event-level diagnostic information.

Useful fields include:
- Timestamp.
- Service.
- Correlation ID.
- Operation.
- Status.
- Error information.

### Metrics
Metrics show aggregate system behavior.

Important metrics include:
- Request rate.
- Error rate.
- p95 latency.
- p99 latency.
- CPU and memory.
- Database connection usage.
- Cache behavior.
- Queue depth.
- Consumer health.

### Traces
Distributed traces show the path of a request through multiple services and dependencies.

Traces are especially useful for:
- High latency.
- Dependency timeouts.
- Cascading failures.
- Unexpected downstream calls.

## Alerting
Alerts should focus on actionable conditions.

Examples:
- Sustained high 5xx rate.
- Significant authentication failure increase.
- High p95/p99 latency.
- Growing message backlog.
- Database connection exhaustion.
- Service readiness failures.

## Alert Investigation
An alert should be treated as an indicator, not automatically as the root cause.

Investigation should establish:
1. What changed?
2. Which component is failing?
3. Which users or operations are affected?
4. Which dependency is involved?
5. Whether the failure is isolated or cascading.

## Alert Quality
Alerts should avoid excessive noise.

A useful alert should have:
- Clear condition.
- Meaningful threshold.
- Relevant service context.
- A documented investigation path.

## Related Knowledge
Use with Observability Architecture, Logging and Correlation ID Policy, Incident Severity Policy, and all incident runbooks.
