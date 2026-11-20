# Compute, Container, and Service Runtime

## Purpose
This document describes the runtime expectations for the platform's stateless application services.

## Service Runtime
Application services should be designed to run as independently managed runtime instances.

The primary application services are:
- API Gateway
- Authentication Service
- User Service
- Product Catalog Service
- Order Service
- Payment Service
- Notification Service

Services should avoid storing critical session state only in local process memory when requests may be handled by multiple instances.

## Stateless Design
Shared state should be stored in appropriate systems such as:
- PostgreSQL for durable domain data.
- Redis for short-lived cache or coordination use cases.
- Message Broker for asynchronous events.

## Resource Signals
Important runtime signals include:
- CPU utilization.
- Memory utilization.
- Request rate.
- Request latency.
- Error rate.
- Instance restart frequency.
- Connection pool usage.

## Resource Exhaustion
Resource pressure can cause:
- Increased latency.
- Request failures.
- Timeouts.
- Instance restarts.
- Connection exhaustion.

Engineers should correlate resource metrics with application and dependency metrics rather than treating high CPU or memory as the root cause automatically.

## Scaling
Scaling decisions should consider:
- Traffic volume.
- Request latency.
- CPU and memory pressure.
- Queue depth.
- Dependency capacity.
- Database connection limits.

Scaling an application service does not automatically solve a bottleneck in PostgreSQL, Redis, an external provider, or another constrained dependency.

## Related Knowledge
Use with High Latency Runbook, Database Incident Runbook, Redis Incident Runbook, and System Architecture Overview.
