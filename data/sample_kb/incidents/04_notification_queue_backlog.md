# Historical Incident: Notification Queue Backlog

## Summary
Notification delivery became delayed because the notification consumer processed messages slower than they were produced.

## Impact
Order and payment notifications were delayed.

## Detection
Message broker queue depth increased continuously while consumer throughput decreased.

## Investigation
The consumer process was running, but provider requests were taking longer than normal. Email provider latency was elevated.

## Root Cause
The downstream email provider experienced latency, reducing consumer throughput and creating a queue backlog.

## Resolution
Provider latency recovered. Consumers gradually drained the backlog.

## Validation
Queue depth returned toward baseline and notification delivery latency normalized.

## Lessons Learned
A healthy consumer process does not guarantee healthy throughput. Downstream provider latency must be checked.

Related:
- `05_notification_delay_runbook.md`
- `06_notification_service_architecture.md`
- `08_message_broker_incident_runbook.md`
