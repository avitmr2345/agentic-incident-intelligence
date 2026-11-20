# Authentication API

## Base Path

`/api/v1/auth`

## Login

`POST /api/v1/auth/login`

Purpose: authenticate a user and issue an access token.

Typical request:

```json
{
  "email": "user@example.com",
  "password": "********"
}
```

Typical successful response contains an access token and token metadata.

Common failures:
- `400` invalid request
- `401` invalid credentials
- `429` rate limit
- `500` internal failure
- `503` dependency unavailable

## Refresh Token

`POST /api/v1/auth/refresh`

Purpose: obtain a new access token using a valid refresh mechanism.

Common investigation points:
- refresh token validity
- token expiry
- signing configuration
- authentication database
- recent configuration changes

## Current User

`GET /api/v1/auth/me`

Requires a valid access token.

Typical failures:
- `401` missing/invalid/expired token
- `403` insufficient permission
- `500` internal error

## Incident Investigation

If login succeeds but `/me` or another protected API returns 401:

1. capture the correlation ID
2. verify the token was issued successfully
3. inspect token issuer and expiry
4. inspect gateway authentication handling
5. compare token signing/verification configuration
6. check whether the issue started after deployment/configuration change

Related documents:
- `03_authentication_architecture.md`
- `01_api_gateway.md`
- `09_error_response_and_status_codes.md`
