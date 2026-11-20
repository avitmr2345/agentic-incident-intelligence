# Historical Incident: External Payment Provider Latency

## Summary
Payment processing latency increased significantly because the external payment provider was responding slowly.

## Impact
Payment requests took longer than normal and some orders remained in `PENDING_PAYMENT`.

## Detection
Payment Service latency and timeout metrics crossed their normal baseline.

## Investigation
Application CPU and memory remained normal. Database performance was also normal. Provider response latency was significantly elevated.

## Root Cause
External provider degradation caused payment requests to exceed application timeout thresholds.

## Resolution
The provider recovered. Payment processing was monitored until pending workflows returned to normal.

## Lessons Learned
External dependencies must be included in incident investigation even when the internal service appears healthy.

Related:
- `04_payment_timeout_runbook.md`
- `05_payment_service_architecture.md`
