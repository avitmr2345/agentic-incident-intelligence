# Retry, Timeout, and Idempotency Policy

## Purpose
This policy establishes safe behavior for distributed calls where network failures, dependency latency, and transient errors can occur.

## Timeouts
Every synchronous dependency call should have an explicit timeout.

Timeouts prevent one slow dependency from indefinitely consuming application resources.

Timeout selection should consider:
- Expected dependency latency.
- User-facing latency requirements.
- Downstream timeout behavior.
- Retry budget.
- Overall request deadline.

## Retry Rules
Retries should be bounded and used only when the failure is likely to be transient.

Suitable candidates may include:
- Temporary network failures.
- Selected 5xx responses.
- Connection failures.
- Explicitly retryable dependency errors.

Retries should generally not be used blindly for:
- Validation errors.
- Authentication failures.
- Authorization failures.
- Permanent not-found conditions.
- Requests that can create duplicate side effects without idempotency protection.

## Backoff
Retries should use controlled backoff rather than immediate repeated requests.

Unbounded or aggressive retries can create retry amplification and turn a dependency degradation into a cascading incident.

## Idempotency
Operations with externally visible side effects should support idempotency where duplicate requests are possible.

Payment creation is a key example:
- A client may retry after a timeout.
- The Payment Service should use an idempotency key.
- A repeated request with the same key should not create a second charge.

## Retry Budget
Retry counts should be bounded. The system should avoid repeatedly retrying a failing dependency when the dependency is already overloaded.

## Incident Investigation
When investigating a timeout:
1. Identify the dependency.
2. Compare dependency latency with configured timeout.
3. Check retry count and backoff behavior.
4. Determine whether retries amplified traffic.
5. Check whether the operation is idempotent.
6. Verify whether partial side effects occurred.

## Related Knowledge
This policy is directly relevant to payment timeouts, cascading order incidents, high-latency incidents, and payment duplicate-request prevention.
