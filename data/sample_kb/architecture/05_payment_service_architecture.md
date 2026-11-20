# Payment Service Architecture

## Purpose

The Payment Service coordinates payment operations between the platform and an external payment provider.

## Payment Flow

```text
Order Service
     |
     v
Payment Service
     |
     +--> PostgreSQL
     |
     +--> External Payment Provider
     |
     +--> Message Broker
```

## Payment States

- `INITIATED`
- `AUTHORIZED`
- `CAPTURED`
- `FAILED`
- `CANCELLED`
- `EXPIRED`

The exact transition depends on the provider response and the requested operation.

## Reliability

Payment calls should use:

- timeouts
- bounded retries for retryable failures
- idempotency keys
- durable payment state
- correlation IDs

Retries must not accidentally create duplicate charges. Operations that can be repeated must be protected by idempotency.

## Common Failure Scenarios

### Provider timeout
The external provider does not respond within the configured timeout.

### Provider rejection
The provider returns a business or authorization failure.

### Credential/configuration failure
Provider credentials or endpoint configuration are invalid.

### Duplicate request
A client retries a payment request. Idempotency should prevent duplicate processing.

### Database failure
Payment state cannot be persisted reliably.

## Investigation Signals

Check:

- provider response codes
- provider latency
- payment state transitions
- idempotency key
- Payment Service logs
- database errors
- recent secret/configuration changes
- order/payment correlation IDs

Related documents:
- `04_order_service_architecture.md`
- `05_payment_api.md`
- `08_observability_architecture.md`
