# Historical Incident: Order Creation 503 Caused by Payment Timeout

## Summary
Order creation began returning HTTP 503. Initial investigation focused on the Order Service, but distributed traces showed that requests were spending most of their time waiting for Payment Service responses.

## Impact
Customers were unable to complete some orders.

## Detection
Order API 503 rate and latency increased simultaneously.

## Investigation
Engineers checked:
1. Order Service health
2. database connectivity
3. Product Catalog latency
4. Payment Service latency
5. external payment provider responses

Order Service itself was healthy. Payment traces showed repeated timeout events.

## Root Cause
The external payment provider experienced elevated latency. Payment Service requests exceeded the configured timeout, causing Order Service requests to fail.

## Resolution
Provider connectivity recovered and payment latency returned to normal. Stuck order/payment states were reviewed after recovery.

## Validation
Successful order creation was confirmed and Payment Service timeout metrics returned to baseline.

## Lessons Learned
A 503 from Order API does not prove that Order Service is the root cause. Dependency traces are essential.

Related:
- `03_order_creation_503_runbook.md`
- `05_payment_service_architecture.md`
- `05_payment_api.md`
