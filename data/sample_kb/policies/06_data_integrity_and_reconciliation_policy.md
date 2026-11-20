# Data Integrity and Reconciliation Policy

## Purpose
This policy defines practices for protecting data consistency across services and for investigating situations where asynchronous or distributed processing may leave partial state.

## Service Data Ownership
Each service should have clear ownership of its domain data.

Examples:
- Authentication owns authentication-related state.
- Order Service owns order lifecycle state.
- Payment Service owns payment state.
- Notification Service owns notification delivery state.

Services should avoid directly modifying another service's domain database.

## Distributed Operations
A business workflow may involve multiple services and asynchronous events.

For example:
1. Order is created.
2. Payment is requested.
3. Payment is authorized.
4. Order state is updated.
5. Notification event is produced.

Failure at any stage can produce temporary partial state.

## Idempotent Processing
Consumers processing events should be able to safely handle duplicate delivery where possible.

The system should use:
- Stable event identifiers.
- Idempotency keys where appropriate.
- State-transition validation.
- Safe duplicate handling.

## Reconciliation
Reconciliation should be considered when:
- An order remains in an unexpected state.
- Payment state and order state disagree.
- Events were delayed or lost.
- A consumer recovered after a backlog.
- External payment state differs from internal records.

A reconciliation process should compare authoritative records and identify mismatches without blindly overwriting state.

## Payment Reconciliation
Payment-related reconciliation should verify:
- Internal payment status.
- External provider result where available.
- Order payment state.
- Idempotency information.
- Relevant timestamps and correlation identifiers.

## Data Integrity During Incidents
Recovery actions should avoid destructive changes unless the impact and intended state are understood.

Engineers should preserve:
- Original identifiers.
- Relevant event records.
- Error information.
- Timestamps.
- Evidence used to determine the corrective action.

## Related Knowledge
Use this policy with Payment Service Architecture, Order Service Architecture, Message Broker Runbook, Payment Timeout Runbook, and Payment Duplicate Request Incident.
