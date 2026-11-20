# Deployment Architecture

## Purpose
This document describes the production deployment flow and the operational checks required after releasing a service.

## Deployment Flow
A typical deployment follows:

1. Source change is validated.
2. Application artifact is built.
3. Automated tests and checks run.
4. Configuration is prepared.
5. Service is deployed.
6. Health and readiness checks run.
7. Traffic is served by the new version.
8. Operational metrics are monitored.

## Service Deployment
Each service should be independently deployable where practical.

Examples:
- Authentication Service
- Order Service
- Payment Service
- Notification Service

A deployment of one service may still affect dependent services when an API contract, event schema, configuration, or runtime behavior changes.

## Rolling Changes
During a rolling deployment, old and new service instances may temporarily coexist.

Therefore:
- API contracts must remain compatible.
- Event consumers must tolerate supported message versions.
- Database migrations must be safe for mixed application versions.

## Post-Deployment Validation
Check:
- `/health`
- `/ready`
- HTTP error rates
- p95/p99 latency
- dependency errors
- queue depth
- database health
- Redis health
- business success metrics

## Rollback
Rollback should restore the last known-good application version when a deployment is strongly correlated with customer impact and a compatible recovery path is not immediately available.

Configuration changes may also require rollback.

## Incident Signals
Deployment-related failures commonly show:
- Sudden increase in 4xx or 5xx responses.
- Readiness failures.
- Authentication failures.
- Increased latency.
- Dependency connection errors.
- Queue processing problems.

## Related Knowledge
Use with Deployment/Rollback Policy, API Backward Compatibility Policy, Readiness Failure Incident, and Deployment Regression Incident.
