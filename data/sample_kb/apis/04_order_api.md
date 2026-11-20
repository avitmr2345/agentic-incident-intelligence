# Order API

## Base Path

`/api/v1/orders`

## Create Order

`POST /api/v1/orders`

The request contains the selected products, quantities, and order information.

Typical flow:

Gateway -> Order Service -> Product Catalog -> Payment Service -> Order database -> event publication

Common responses:
- `201` order created
- `400` invalid order
- `401` unauthenticated
- `403` unauthorized
- `404` referenced resource not found
- `409` state or business conflict
- `500` internal error
- `503` dependency unavailable

## Get Order

`GET /api/v1/orders/{order_id}`

Possible responses:
- `200`
- `401`
- `403`
- `404`
- `500`

## Cancel Order

`POST /api/v1/orders/{order_id}/cancel`

Cancellation depends on the current order state and business rules.

A cancellation request may return `409` when the order has already moved to a state where cancellation is not allowed.

## Investigation

For order creation failures, trace the complete dependency path rather than assuming the Order Service is the root cause.

Check:

- product validation
- database
- payment availability
- payment latency
- broker status
- recent deployments
- correlation ID

Related documents:
- `04_order_service_architecture.md`
- `03_product_catalog_api.md`
- `05_payment_api.md`
