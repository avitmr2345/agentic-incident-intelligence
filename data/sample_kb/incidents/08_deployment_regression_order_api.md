# Historical Incident: Order API Regression After Deployment

## Summary
Order creation failures increased immediately after a new application version was deployed.

## Impact
A subset of order requests failed validation.

## Investigation
The incident timeline was compared with deployment timing. Logs showed validation errors for a request field that had previously been accepted.

## Root Cause
A backward-incompatible API validation change was deployed without accounting for existing clients.

## Resolution
The deployment was rolled back and the API contract was reviewed.

## Validation
Order creation success returned to baseline.

## Lessons Learned
API changes must be evaluated for client compatibility before deployment.

Related:
- `09_deployment_and_configuration_incident_runbook.md`
- `10_api_versioning_and_change_policy.md`
- `04_order_api.md`
