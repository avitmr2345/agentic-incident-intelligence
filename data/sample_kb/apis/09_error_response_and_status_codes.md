# Error Responses and Status Codes

## Purpose

HTTP status codes provide symptoms, not complete root causes. Incident investigation should combine the status code with logs, traces, metrics, and dependency behavior.

## Common Codes

### 400 Bad Request
The request is invalid.

### 401 Unauthorized
Authentication credentials are missing, invalid, expired, or rejected.

### 403 Forbidden
Authentication succeeded but the caller is not permitted to perform the operation.

### 404 Not Found
The route or requested resource does not exist.

### 409 Conflict
The requested operation conflicts with current state or business rules.

### 429 Too Many Requests
The request has exceeded a configured rate limit.

### 500 Internal Server Error
Unexpected application-side failure.

### 502 Bad Gateway
A gateway or proxy could not obtain a valid response from an upstream service.

### 503 Service Unavailable
The target service or a required dependency is unavailable.

## Investigation Rule

Do not conclude that the component returning the status code is necessarily the root cause.

Example:

`Order API -> 503`

may be caused by:

`Order Service -> Payment Service timeout -> external provider latency`

rather than an Order Service application defect.

## Evidence

Use:

- correlation ID
- endpoint
- timestamp
- service logs
- dependency traces
- metrics
- deployment/configuration history

Related documents:
- `01_api_gateway.md`
- `04_order_api.md`
- `08_observability_architecture.md`
