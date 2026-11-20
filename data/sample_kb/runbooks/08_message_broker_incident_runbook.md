# Message Broker Incident Runbook

## Purpose

Use this runbook when asynchronous processing is delayed, event consumers are failing, or message queues begin accumulating backlog.

## Symptoms

Common symptoms:

- queue depth increases
- event processing latency increases
- consumers restart repeatedly
- messages enter a dead-letter path
- downstream notifications are delayed
- asynchronous order/payment workflows remain incomplete

## Investigation Workflow

### 1. Identify the Affected Queue

Determine:

- queue/topic
- producer
- consumer
- message type
- approximate backlog start time

### 2. Check Queue Depth

Compare current queue depth with the normal baseline.

A growing queue indicates that message production is exceeding successful consumption.

### 3. Check Consumer Health

Inspect:

- consumer availability
- processing rate
- error rate
- restart count
- processing latency

### 4. Check Producer Behavior

Determine whether an upstream service suddenly increased event production.

A producer problem can create a backlog even when consumers are healthy.

### 5. Inspect Failed Messages

Look for:

- repeated processing errors
- malformed payloads
- unavailable dependencies
- poison messages
- dead-letter messages

### 6. Check Downstream Dependencies

A healthy consumer can still become slow if it depends on an unhealthy external service.

Example:

```text
Payment Event
    ↓
Notification Consumer
    ↓
Email Provider timeout
    ↓
Consumer throughput decreases
    ↓
Queue backlog increases
```

## Root-Cause Patterns

### Consumer outage
Messages accumulate because no consumers are processing them.

### Consumer slowdown
Consumers are running but process fewer messages than normal.

### Producer spike
Event volume increases sharply.

### Dependency failure
Consumer processing is slowed by a downstream dependency.

### Poison message
A specific message repeatedly fails and requires dead-letter handling.

## Recovery

After resolving the cause:

1. verify consumers are processing messages
2. monitor queue depth
3. verify processing latency
4. inspect dead-letter messages
5. verify downstream state
6. confirm idempotency where messages may be replayed

Do not simply delete a backlog without understanding whether those messages represent business-critical operations.

Related documents:

- `06_notification_service_architecture.md`
- `06_notification_delay_runbook.md`
- `04_order_service_architecture.md`
- `08_observability_architecture.md`
