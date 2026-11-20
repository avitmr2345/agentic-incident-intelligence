# Health and Readiness Endpoints

## Purpose

Health endpoints provide a quick way to determine whether a service process is alive and whether it should receive traffic.

## Liveness

`GET /health`

A successful liveness response indicates that the service process is running.

Liveness checks should remain lightweight.

## Readiness

`GET /ready`

A readiness response indicates whether the service is prepared to accept traffic based on required startup/dependency checks.

A service can be alive but not ready.

## Incident Interpretation

### Health succeeds, readiness fails
The process is running but a required dependency or startup condition may be unavailable.

### Health and readiness both fail
The service process or its hosting environment may be unhealthy.

### Health succeeds but API requests fail
The application can be alive while a specific endpoint, dependency, configuration path, or business operation is failing.

## Investigation

Check:

- service logs
- database connectivity
- dependency health
- configuration
- recent deployment
- resource utilization

Related documents:
- `01_api_gateway.md`
- `09_error_response_and_status_codes.md`
- `08_observability_architecture.md`
