# Notification API

## Base Path

`/api/v1/notifications`

## Send Notification

`POST /api/v1/notifications`

Used when an authorized caller needs to request a notification.

Typical fields include:

- recipient
- channel
- template
- payload

Supported channels may include email, SMS, and push.

## Get Notification

`GET /api/v1/notifications/{notification_id}`

Returns processing state and relevant metadata.

Possible states include:

- `QUEUED`
- `PROCESSING`
- `SENT`
- `FAILED`

## Common Failures

- `400` invalid notification request
- `401` unauthenticated
- `403` unauthorized
- `404` notification not found
- `429` rate limit
- `500` internal error
- `503` dependency unavailable

## Investigation

For delayed notifications, check:

1. message broker queue depth
2. consumer health
3. processing latency
4. retry count
5. dead-letter messages
6. provider response codes
7. notification service logs

Related documents:
- `06_notification_service_architecture.md`
- `08_health_and_readiness_endpoints.md`
