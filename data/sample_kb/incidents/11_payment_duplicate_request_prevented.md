# Historical Incident: Payment Retry and Idempotency Protection

## Summary
A client retried a payment request after experiencing a timeout. The same idempotency key was reused.

## Impact
The customer experienced a delayed response but no duplicate charge was created.

## Investigation
Payment records showed multiple requests associated with the same idempotency key.

## Root Cause
The initial provider response was delayed, causing the client to retry. The Payment Service correctly recognized the repeated idempotency key.

## Resolution
No corrective production action was required. The payment state was reconciled with the provider response.

## Lessons Learned
Timeouts do not necessarily mean that an external payment operation did not occur. Idempotency and state reconciliation are essential.

Related:
- `05_payment_service_architecture.md`
- `05_payment_api.md`
- `04_payment_timeout_runbook.md`
