# Order Service Architecture

## Purpose

The Order Service owns order creation, state transitions, and coordination with product validation and payment processing.

## Order Lifecycle

```text
CART
  |
  v
PENDING_PAYMENT
  |
  +--> PAYMENT_FAILED
  |
  v
PAID
  |
  v
PROCESSING
  |
  v
COMPLETED
```

An order may also transition to `CANCELLED` when cancellation rules permit it.

## Order Creation Flow

```text
Client
  |
  v
API Gateway
  |
  v
Order Service
  |
  +--> Product Catalog Service
  |
  +--> PostgreSQL
  |
  +--> Payment Service
  |
  +--> Message Broker
```

Typical processing:

1. Authenticate the request.
2. Validate the order payload.
3. Validate product availability/details.
4. Create the order in `PENDING_PAYMENT`.
5. Initiate payment.
6. Transition the order based on payment result.
7. Publish the appropriate event.
8. Allow downstream notification processing.

## Dependencies

- PostgreSQL
- Product Catalog Service
- Payment Service
- Redis where applicable
- Message Broker
- API Gateway

## Common Failure Scenarios

### Product validation failure
The requested product is unavailable or invalid.

### Payment timeout
Payment processing exceeds the configured timeout.

### Payment service unavailable
The order cannot complete payment processing because the dependency is unavailable.

### Database failure
Order creation or state transitions fail.

### Broker failure
The order may complete synchronously while downstream event processing is delayed.

## Investigation Signals

For order failures, inspect:

- order endpoint response codes
- Order Service logs
- database connectivity/errors
- Product Catalog response latency
- Payment Service response/error rate
- message broker queue depth
- recent deployment/configuration changes
- correlation ID across services

A 500 from the order endpoint does not by itself identify the root cause. The dependency path must be traced.

Related documents:
- `02_service_dependency_map.md`
- `04_order_api.md`
- `03_product_catalog_api.md`
- `05_payment_api.md`
- `08_observability_architecture.md`
