# Historical Incident: SMS Provider Failure With Email Unaffected

## Summary
SMS notifications failed while email notifications continued normally.

## Impact
Users who selected SMS notifications experienced delivery failures.

## Investigation
Notification queue and consumer health were normal. SMS provider responses showed elevated failures, while email provider metrics remained normal.

## Root Cause
The external SMS provider experienced an outage.

## Resolution
The provider recovered and queued retryable messages were processed.

## Lessons Learned
An incident affecting one notification channel does not necessarily indicate a failure of the Notification Service itself.

Related:
- `06_notification_service_architecture.md`
- `05_notification_delay_runbook.md`
