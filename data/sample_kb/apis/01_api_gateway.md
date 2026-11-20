# API Gateway

## Purpose

The API Gateway is the main HTTP entry point for client requests. It routes requests to backend services and provides cross-cutting controls.

## Responsibilities

- request routing
- authentication forwarding/validation integration
- request validation
- rate limiting
- correlation ID handling
- access logging
- response propagation
- API version routing

## Request Headers

Common headers include:

- `Authorization`
- `Content-Type`
- `X-Correlation-ID`

If a client does not provide a correlation ID, the gateway should generate one where configured.

## Route Mapping

Examples:

- `/api/v1/auth/*` -> Authentication Service
- `/api/v1/users/*` -> User Service
- `/api/v1/products/*` -> Product Catalog Service
- `/api/v1/orders/*` -> Order Service
- `/api/v1/payments/*` -> Payment Service
- `/api/v1/notifications/*` -> Notification Service

## Common Failures

### 401
Authentication information is missing or invalid.

### 403
The request is authenticated but not authorized.

### 404
The route does not exist or is not mapped.

### 429
Rate limit exceeded.

### 502/503
The gateway cannot successfully communicate with the target service or the target service is unavailable.

## Investigation

For gateway failures, check:

1. route configuration
2. gateway logs
3. target service health
4. authentication behavior
5. rate limiting
6. correlation ID
7. recent gateway/configuration deployments

Related documents:
- `02_authentication_api.md`
- `08_health_and_readiness_endpoints.md`
- `09_error_response_and_status_codes.md`
