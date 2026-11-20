# Historical Incident: Message Consumer Crash

## Summary
A notification consumer repeatedly crashed while processing messages, causing queue backlog.

## Impact
Notification delivery was delayed.

## Detection
Queue depth increased while consumer restart frequency increased.

## Investigation
Logs showed the same processing exception recurring for a subset of messages.

## Root Cause
A malformed message triggered an unhandled processing exception, causing the consumer to restart repeatedly.

## Resolution
The problematic message was isolated through the dead-letter mechanism and the consumer was restarted with corrected error handling.

## Validation
Consumer throughput recovered and queue depth decreased.

## Lessons Learned
Consumers should handle malformed or poison messages without repeatedly destabilizing the entire processing loop.

Related:
- `08_message_broker_incident_runbook.md`
- `06_notification_service_architecture.md`
