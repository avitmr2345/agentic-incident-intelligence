# Authentication 401 Incident Runbook

## Purpose

Use this runbook when users can log in or previously authenticated successfully but protected APIs begin returning HTTP 401.

## Typical Symptom

Example:

```text
POST /api/v1/auth/login -> 200
GET /api/v1/users/me -> 401
GET /api/v1/orders -> 401
```

This pattern suggests that credential authentication and subsequent token validation may be behaving differently.

## Investigation Workflow

### 1. Confirm the Pattern

Determine:

- whether login itself succeeds
- which protected endpoints return 401
- whether the issue affects all users or a subset
- when the failures started

### 2. Inspect the Token

Check relevant properties:

- expiration
- issuer
- subject
- required claims
- signing algorithm where applicable

Do not expose sensitive token contents in logs or incident reports.

### 3. Check Signing Configuration

Compare the configuration used when tokens are issued with the configuration used for verification.

Look for:

- changed signing key
- incorrect secret/configuration
- mismatched issuer
- changed algorithm configuration
- stale environment configuration

### 4. Check API Gateway Behavior

Verify:

- Authorization header forwarding
- gateway authentication configuration
- route configuration
- recent gateway deployment

### 5. Check Timing

If the issue began immediately after a deployment or configuration change, compare the changed authentication configuration with the incident start time.

### 6. Correlate Logs

Use the correlation ID across:

```text
Client
 -> API Gateway
 -> Authentication/verification layer
 -> Target Service
```

## Common Root-Cause Patterns

- token signing/verification configuration mismatch
- expired tokens
- gateway dropping Authorization headers
- incorrect issuer configuration
- authentication configuration changed during deployment

## Recovery Considerations

If a configuration mismatch is confirmed:

1. restore the known-good configuration or deploy the corrected configuration
2. verify token issuance
3. verify a protected endpoint
4. monitor 401 rate
5. confirm that existing and newly issued tokens behave as expected

Do not invalidate all sessions unless the incident requires it.

Related documents:

- `03_authentication_architecture.md`
- `02_authentication_api.md`
- `01_api_gateway.md`
