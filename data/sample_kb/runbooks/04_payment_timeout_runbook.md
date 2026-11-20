# Payment Timeout Runbook

## Purpose

Use this runbook when payment requests are timing out or payment latency increases significantly.

## Symptoms

Possible symptoms:

- payment requests take longer than normal
- payment requests return timeout-related errors
- orders remain in `PENDING_PAYMENT`
- payment failures increase
- external provider latency increases

## Investigation Workflow

### 1. Check Payment Service

Review:

- request latency
- timeout rate
- error rate
- application logs
- resource utilization

### 2. Check External Provider

Inspect available provider signals:

- response latency
- timeout rate
- error responses
- provider status information
- recent provider-side changes if available

### 3. Check Timeout Configuration

Verify:

- client timeout
- connection timeout
- read timeout
- retry configuration

Compare current values with the last known-good configuration.

### 4. Check Retries

Determine whether retries are:

- bounded
- occurring only for retryable failures
- increasing load on the provider
- interacting correctly with idempotency

Unbounded or excessive retries can make a provider outage worse.

### 5. Check Idempotency

For payment operations, confirm that repeated requests use the correct idempotency mechanism.

Never solve a timeout incident by blindly replaying payment requests.

## Root-Cause Patterns

### External provider degradation
Provider latency rises while application resources remain healthy.

### Incorrect timeout configuration
A deployment changes timeout values and payment failures begin immediately afterward.

### Application saturation
Payment Service itself becomes CPU/memory/thread/connection constrained.

### Retry amplification
Retries increase traffic and cause additional provider or application pressure.

## Recovery

After addressing the confirmed cause:

1. monitor payment latency
2. verify successful payment state transitions
3. verify order transitions
4. check for stuck payments
5. check for duplicate-charge risk
6. monitor retry volume

Related documents:

- `05_payment_service_architecture.md`
- `05_payment_api.md`
- `04_order_creation_503_runbook.md`
