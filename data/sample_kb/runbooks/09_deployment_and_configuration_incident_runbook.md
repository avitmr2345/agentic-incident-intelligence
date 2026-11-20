# Deployment and Configuration Incident Runbook

## Purpose

Use this runbook when an incident begins during or immediately after a deployment, configuration change, secret update, API change, or infrastructure configuration change.

## Symptoms

Typical indicators:

- failures begin immediately after deployment
- error rate increases for a newly changed endpoint
- readiness checks fail
- authentication behavior changes
- downstream calls begin timing out
- configuration-related exceptions appear in logs

## Investigation Workflow

### 1. Establish Temporal Correlation

Record:

- incident start time
- deployment start/end time
- configuration change time
- first observed error

A matching timestamp is evidence of correlation, not proof of causation.

### 2. Identify What Changed

Review:

- application code
- environment variables
- secrets
- API contracts
- gateway routes
- database migrations
- timeout values
- dependency endpoints

### 3. Compare With Last Known Good State

Compare:

```text
Current version/configuration
        vs
Previous known-good version/configuration
```

Focus on changes related to the affected request path.

### 4. Check Service Readiness

A deployment may appear successful while the service is not actually ready.

Check:

- `/health`
- `/ready`
- startup logs
- dependency connectivity

### 5. Check Downstream Compatibility

For API or configuration changes, verify that:

- clients still send supported fields
- downstream services accept the new request format
- gateway routes point to the intended version
- authentication configuration remains compatible

## Root-Cause Patterns

### Application regression
A code change introduces an application failure.

### Configuration mismatch
The deployment contains incorrect environment configuration.

### Secret/configuration rotation issue
A dependent service cannot authenticate to another service.

### API incompatibility
A changed contract breaks a client or downstream service.

### Database migration issue
Application and schema versions are incompatible.

## Recovery

Depending on evidence:

- roll back the application
- restore previous configuration
- correct the configuration and redeploy
- complete a compatible database migration
- disable a faulty feature where supported

After recovery, verify:

1. error rate
2. latency
3. health/readiness
4. affected endpoint
5. downstream dependencies
6. business workflow

Related documents:

- `10_api_versioning_and_change_policy.md`
- `08_health_and_readiness_endpoints.md`
- `01_api_gateway.md`
- `08_observability_architecture.md`
