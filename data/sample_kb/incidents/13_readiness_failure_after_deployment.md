# Historical Incident: Service Readiness Failure After Deployment

## Summary
A newly deployed service was running but did not become ready to receive traffic.

## Impact
The gateway returned unavailable responses for requests routed to the service.

## Investigation
`/health` returned successfully, while `/ready` failed. Startup logs showed that a required dependency connection could not be established.

## Root Cause
The deployment contained an incorrect dependency configuration value.

## Resolution
The configuration was corrected and the service was redeployed.

## Validation
Both health and readiness checks succeeded and API traffic recovered.

## Lessons Learned
A running process is not necessarily a ready service. Health and readiness must be interpreted separately.

Related:
- `08_health_and_readiness_endpoints.md`
- `09_deployment_and_configuration_incident_runbook.md`
