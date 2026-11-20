# Observability Architecture

## Purpose

Observability allows engineers to determine what happened, where it happened, and how failures propagated across the platform.

## Three Core Signals

### Logs
Structured application and infrastructure events.

Useful fields include:

- timestamp
- service
- environment
- log level
- endpoint
- status code
- error type
- correlation ID
- request ID

### Metrics
Quantitative signals such as:

- request rate
- error rate
- latency
- database connection usage
- queue depth
- cache hit rate
- provider latency
- retry count

### Traces
Distributed traces connect a request across multiple services.

For example:

```text
Gateway -> Order Service -> Product Catalog
                         -> Payment Service -> Provider
```

## Correlation IDs

The same correlation ID should be propagated through a request path whenever possible.

This allows an engineer to connect:

- gateway logs
- service logs
- downstream calls
- database-related application logs
- asynchronous processing records

## Health vs Readiness

Liveness answers whether a process is running.

Readiness answers whether the service is prepared to accept traffic and its required dependencies are sufficiently available.

## Investigation Sequence

A practical sequence is:

1. Reproduce or clearly define the symptom.
2. Identify affected endpoint/workflow.
3. Check error rate and latency.
4. Search logs using correlation ID.
5. Inspect traces for slow/failing dependencies.
6. Check dependency health.
7. Compare the timing with deployments/configuration changes.
8. Determine whether the failure is local or cascading.
9. Confirm the suspected root cause with multiple signals.

## Incident Evidence

Strong evidence should connect the symptom to an observable technical cause.

Example:

`Order creation returns 503` + `Payment Service timeout in trace` + `provider latency spike` is stronger evidence than the 503 alone.

Related documents:
- `01_system_architecture_overview.md`
- `02_service_dependency_map.md`
- `08_health_and_readiness_endpoints.md`
- `09_error_response_and_status_codes.md`
