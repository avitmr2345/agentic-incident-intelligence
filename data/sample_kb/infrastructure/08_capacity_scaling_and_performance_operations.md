# Capacity, Scaling, and Performance Operations

## Purpose
This document describes how capacity and performance should be evaluated across application services and shared dependencies.

## Key Capacity Signals
Monitor:
- Request volume.
- CPU utilization.
- Memory utilization.
- Request latency.
- Error rate.
- Database connections.
- Database query latency.
- Redis utilization.
- Message queue depth.
- Consumer throughput.
- External provider latency.

## Scaling Application Services
Application services can generally be scaled when:
- Request volume increases.
- CPU or memory becomes a bottleneck.
- Concurrent request demand exceeds current capacity.

However, scaling application instances may increase pressure on shared dependencies.

For example:
- More Order Service instances can increase database connections.
- More consumers can increase downstream provider traffic.
- More application instances can increase Redis or broker usage.

## Database Capacity
Database bottlenecks may appear as:
- Increased query latency.
- Connection pool exhaustion.
- High resource utilization.
- Slow transactions.

Adding application instances should not be used as a substitute for resolving a database bottleneck.

## Cache Capacity
Redis should be monitored for:
- Memory pressure.
- Eviction behavior.
- Latency.
- Availability.

Cache failures can shift traffic to PostgreSQL and create secondary incidents.

## Queue Capacity
For asynchronous workloads, monitor:
- Queue depth.
- Message age.
- Consumer throughput.
- Consumer errors.
- Retry volume.

A growing queue may indicate insufficient consumers, slow downstream providers, or a producer spike.

## Performance Investigation
When latency increases:
1. Check whether traffic increased.
2. Check service resource utilization.
3. Inspect traces for slow dependencies.
4. Check database and cache latency.
5. Check queue or external provider behavior.
6. Compare p95 and p99 rather than only averages.

## Capacity Planning
Capacity planning should consider normal traffic, expected peaks, dependency limits, and failure scenarios.

## Related Knowledge
Use with High Latency Runbook, Database Incident Runbook, Redis Incident Runbook, Message Broker Runbook, and Compute/Runtime documentation.
