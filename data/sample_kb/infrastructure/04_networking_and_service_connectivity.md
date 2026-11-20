# Networking and Service Connectivity

## Purpose
This document describes service-to-service connectivity considerations and the signals used to investigate network-related failures.

## Connectivity Paths
Important communication paths include:
- Client to API Gateway.
- Gateway to application services.
- Services to PostgreSQL.
- Services to Redis.
- Services to Message Broker.
- Payment Service to external payment provider.
- Notification Service to external communication providers.

## Common Connectivity Failures
Examples include:
- Connection refused.
- Connection timeout.
- DNS or endpoint resolution failure.
- TLS or certificate problems.
- Network policy or access restrictions.
- Incorrect endpoint configuration.

## Investigation
When a service cannot reach a dependency:
1. Identify the exact dependency.
2. Check whether the dependency itself is healthy.
3. Check endpoint configuration.
4. Check connection and timeout metrics.
5. Compare affected and unaffected services.
6. Check whether a deployment or configuration change preceded the failure.

## Timeouts
Network timeouts should be explicitly configured.

A network timeout can become an application timeout, which can then produce:
- HTTP 5xx responses.
- Retry amplification.
- Queue backlog.
- Increased connection usage.

## External Providers
External provider failures should be distinguished from internal service failures.

For example, a Payment Service timeout may originate from:
- Internal payment processing.
- Network connectivity.
- External provider latency.
- Provider errors.

## Correlation
Correlation IDs, traces, service logs, and dependency latency metrics should be used together to determine where the request path is failing.

## Related Knowledge
Use with Payment Timeout Runbook, High Latency Runbook, Service Dependency Map, and Retry/Timeout/Idempotency Policy.
