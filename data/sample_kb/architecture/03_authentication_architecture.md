# Authentication Architecture

## Purpose

The Authentication Service manages login, token issuance, token refresh, and authentication-related validation.

## Login Flow

```text
Client
  |
  v
API Gateway
  |
  v
Authentication Service
  |
  +--> PostgreSQL (credential/user data)
  |
  +--> JWT configuration / secrets
  |
  v
JWT access token
```

The primary login endpoint is:

`POST /api/v1/auth/login`

A successful login returns an access token used by protected APIs.

## Token Validation

For protected requests, authentication information is evaluated using the configured JWT signing key and token claims.

Important token properties include:

- signature
- expiration
- issuer
- subject/user identity
- required authorization claims

A token can be structurally valid but still be rejected if it is expired, signed with an unexpected key, or has invalid claims.

## 401 vs 403

### HTTP 401
Usually indicates that authentication failed or the request did not provide acceptable authentication credentials.

Common causes:
- missing Authorization header
- expired token
- invalid signature
- wrong issuer
- token generated with stale configuration

### HTTP 403
Usually indicates that authentication succeeded but the authenticated identity is not allowed to perform the requested operation.

## Dependencies

- PostgreSQL
- Redis where session/rate-limit functionality is enabled
- JWT signing configuration
- secret/configuration management
- API Gateway

## Common Status Codes

- `400` invalid login request
- `401` authentication failure
- `403` authorization failure
- `429` rate limit
- `500` unexpected application error
- `503` unavailable dependency or service

## Incident Investigation

If users report that login succeeds but protected endpoints return 401:

1. Verify the login response and token issuance.
2. Check whether failures began after a deployment or configuration change.
3. Inspect JWT signing/verification configuration.
4. Compare the token issuer and expected issuer.
5. Check token expiry.
6. Check API Gateway authentication forwarding.
7. Review authentication and gateway logs using the correlation ID.

Related documents:
- `01_system_architecture_overview.md`
- `02_service_dependency_map.md`
- `01_api_gateway.md`
- `02_authentication_api.md`
- `09_error_response_and_status_codes.md`
