# API Versioning and Change Policy

## Current Version

Public APIs use the `/api/v1` path.

Example:

`/api/v1/orders`

## Compatibility

Changes to an existing API should preserve backward compatibility where possible.

Potentially breaking changes include:

- removing fields
- changing field types
- changing authentication requirements
- changing response semantics
- changing error behavior
- changing endpoint paths

## Deployment Considerations

API changes should be evaluated together with:

- gateway routing
- service deployment order
- client compatibility
- authentication behavior
- database migrations
- monitoring and rollback plans

## Incident Investigation After an API Change

When failures begin immediately after an API deployment:

1. identify the changed endpoint
2. compare the previous and current contract
3. inspect gateway routing
4. check request/response validation
5. inspect application logs
6. check downstream dependency behavior
7. compare error rates before and after deployment
8. consider rollback when the change is confirmed as the trigger

Related documents:
- `01_api_gateway.md`
- `09_error_response_and_status_codes.md`
- service-specific API documents
