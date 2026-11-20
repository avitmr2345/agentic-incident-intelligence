# Historical Incident: Cascading Order and Payment Degradation

## Summary
An external payment dependency became slow, causing payment timeouts, order failures, and increased retry traffic.

## Impact
Order creation reliability decreased and overall API latency increased.

## Investigation
The initial symptom was elevated Order API 503 responses. Traces showed Payment Service latency. Payment metrics showed provider timeouts. Retry volume then increased overall traffic.

## Root Cause
External payment provider degradation triggered timeouts. Retries increased load and amplified the impact.

## Resolution
Retry behavior was bounded and the provider recovered. Stuck workflows were reviewed after stabilization.

## Lessons Learned
Retries can amplify an outage. Incident investigation should follow the dependency chain and examine retry volume.

Related:
- `03_order_creation_503_runbook.md`
- `04_payment_timeout_runbook.md`
- `10_high_latency_incident_runbook.md`
- `05_payment_service_architecture.md`
