# Deployment, Rollback, and Change Management Policy

## Purpose
This policy defines safe practices for production deployments, configuration changes, validation, and rollback.

## Before Deployment
Before a production change:
- Identify affected services and dependencies.
- Review API and data compatibility.
- Validate configuration.
- Confirm rollback strategy.
- Identify health and business metrics to monitor.
- Ensure the change can be correlated with subsequent incidents.

## Deployment Monitoring
After deployment, monitor:
- Request success rate.
- 4xx and 5xx responses.
- p95/p99 latency.
- Dependency errors.
- Database and cache health.
- Queue depth and consumer health.
- Service readiness.
- Business-level signals such as order and payment success.

## Health Versus Readiness
A running process does not necessarily mean that a service is ready to accept traffic.

A deployment should be considered healthy only when:
- Liveness is healthy.
- Readiness is healthy.
- Required dependencies are available.
- Error and latency metrics remain within expected ranges.

## Rollback
Rollback should be considered when:
- A deployment introduces clear customer impact.
- A previous version is known to be healthy.
- Recovery through configuration correction is slower or less reliable.
- The failure is strongly correlated with the change.

Rollback does not replace root-cause investigation.

## Configuration Changes
Configuration changes should be treated as production changes because they can cause failures without application code changes.

Examples:
- JWT signing configuration.
- Database connection settings.
- Redis configuration.
- Timeout values.
- Rate limits.
- External provider settings.

## Post-Change Verification
After recovery:
- Verify the affected endpoint.
- Verify dependent services.
- Confirm error rates have normalized.
- Check for delayed queues or retries.
- Record the final change and recovery action.

## Related Knowledge
This policy supports the Deployment/Configuration Runbook, Readiness Failure Incident, Authentication 401 Incident, API Regression Incident, and Observability Architecture.
