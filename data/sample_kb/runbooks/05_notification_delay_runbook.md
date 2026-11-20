# Notification Delay Runbook

## Purpose

Use this runbook when users report delayed or missing email, SMS, or push notifications.

## Typical Symptoms

- notifications remain in `QUEUED`
- queue depth increases
- notification latency increases
- retry count increases
- notifications appear after a significant delay
- some notifications enter the dead-letter path

## Processing Path

```text
Order/Payment Event
       |
       v
Message Broker
       |
       v
Notification Consumer
       |
       +--> Email Provider
       +--> SMS Provider
       +--> Push Provider
```

## Investigation Workflow

### 1. Check Queue Depth

A growing queue indicates that incoming work is exceeding consumer processing capacity or that consumers are unavailable.

### 2. Check Consumer Health

Verify:

- consumer process is running
- readiness status
- processing rate
- error rate
- restart frequency

### 3. Check Provider Behavior

Determine whether the affected channel's external provider is:

- timing out
- rejecting requests
- rate limiting
- returning elevated errors

### 4. Check Retries

Inspect:

- retry count
- retry delay
- repeated failures
- dead-letter messages

### 5. Check Event Production

If notifications are missing entirely, verify that the upstream service actually published the expected event.

For example:

```text
Payment completed
    |
    v
PaymentAuthorized event
    |
    v
Notification consumer
```

If the event was never published, the problem may be upstream rather than in the Notification Service.

## Root-Cause Patterns

### Consumer outage
Queue depth increases while provider health is normal.

### Provider degradation
Consumer is processing messages but provider calls fail or slow down.

### Upstream event failure
The expected event was not published.

### Poison message
A specific message repeatedly fails processing and moves to a dead-letter path.

## Recovery

After fixing the confirmed cause:

1. verify consumer processing
2. monitor queue depth until it returns toward normal
3. verify successful deliveries
4. inspect dead-letter messages
5. confirm no duplicate notifications were produced

Related documents:

- `06_notification_service_architecture.md`
- `06_notification_api.md`
- `08_observability_architecture.md`
