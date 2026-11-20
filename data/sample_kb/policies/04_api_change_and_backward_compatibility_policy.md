# API Change and Backward Compatibility Policy

## Purpose
This policy defines how API changes should be introduced without unexpectedly breaking clients or dependent services.

## Versioning
The platform uses versioned API paths such as:
- `/api/v1/...`

A version should remain compatible with existing clients unless a planned breaking change requires a new version.

## Backward-Compatible Changes
Generally safer changes include:
- Adding optional response fields.
- Adding optional request fields.
- Adding new endpoints.
- Improving documentation.
- Extending supported values without changing existing behavior.

## Potentially Breaking Changes
Examples include:
- Removing response fields.
- Renaming fields.
- Changing field types.
- Making an optional field mandatory.
- Changing validation rules in a way that rejects previously valid requests.
- Changing status-code semantics.
- Changing authentication requirements.

## Deployment Considerations
API changes should account for mixed-version deployments.

During a rolling deployment:
- Older and newer service versions may coexist.
- Producers and consumers must remain compatible.
- Schema changes should follow a safe migration sequence.
- Dependency contracts should be reviewed before deployment.

## Validation Changes
Validation changes deserve special attention because a seemingly small change can cause widespread 4xx responses.

After deployment, monitor:
- Request success rate.
- 4xx/5xx rates.
- Endpoint latency.
- Dependency errors.
- Client-specific failure patterns.

## Incident Response
If an API change causes production failures:
1. Compare the failure start time with the deployment.
2. Identify changed endpoints or validation rules.
3. Compare current behavior with the previous version.
4. Check whether clients are sending the previously accepted format.
5. Roll back or apply a compatible fix when appropriate.

## Related Knowledge
Use this policy with API Versioning and Change Policy, Order API documentation, Deployment Regression historical incident, and Deployment/Configuration Incident Runbook.
