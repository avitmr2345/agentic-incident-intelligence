# User API

## Base Path

`/api/v1/users`

## Current User

`GET /api/v1/users/me`

Returns the authenticated user's profile.

## Get User

`GET /api/v1/users/{user_id}`

Returns a user profile when the caller has the required permissions.

## Update Profile

`PATCH /api/v1/users/{user_id}`

Updates permitted profile fields.

## Common Responses

- `200` successful request
- `400` invalid payload
- `401` authentication failure
- `403` authorization failure
- `404` user not found
- `409` business conflict
- `500` internal error

## Dependencies

- API Gateway
- Authentication context
- PostgreSQL
- Redis where caching is enabled

## Investigation

For user profile failures:

1. verify authentication
2. check authorization
3. check User Service health
4. inspect database connectivity/query latency
5. inspect cache behavior where applicable
6. correlate with recent deployments

Related documents:
- `03_authentication_architecture.md`
- `07_data_storage_and_cache_architecture.md`
