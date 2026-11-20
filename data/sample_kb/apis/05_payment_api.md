# Payment API

## Base Path

`/api/v1/payments`

## Create Payment

`POST /api/v1/payments`

Creates or initiates payment processing for an order.

Important request information may include:

- order ID
- amount
- currency
- idempotency key

Common responses:
- `201` payment initiated
- `400` invalid request
- `401` unauthenticated
- `409` duplicate/conflicting operation
- `500` internal error
- `502/503` provider or service availability issue

## Get Payment

`GET /api/v1/payments/{payment_id}`

Returns the current payment state.

## Idempotency

Payment creation should support an idempotency mechanism so repeated client requests do not unintentionally create duplicate charges.

## Investigation

For payment failures:

1. identify payment and order IDs
2. inspect payment state transition
3. inspect provider response
4. check provider latency/timeouts
5. verify idempotency behavior
6. inspect Payment Service logs
7. check recent credential/configuration changes

Related documents:
- `05_payment_service_architecture.md`
- `04_order_api.md`
- `09_error_response_and_status_codes.md`
