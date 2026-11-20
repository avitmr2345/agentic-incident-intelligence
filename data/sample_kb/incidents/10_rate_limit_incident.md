# Historical Incident: Unexpected API Rate Limiting

## Summary
Valid users began receiving HTTP 429 responses from APIs.

## Impact
Some users were temporarily unable to access normal application functionality.

## Investigation
Gateway metrics showed increased 429 responses. Redis-backed rate-limit state was examined and request volume was compared with the configured limits.

## Root Cause
A configuration change lowered the effective rate limit for a production route.

## Resolution
The rate-limit configuration was restored to the approved value.

## Validation
429 rates returned to baseline and normal requests succeeded.

## Lessons Learned
Rate-limit changes should be reviewed alongside expected traffic patterns and monitored immediately after deployment.

Related:
- `01_api_gateway.md`
- `07_redis_cache_incident_runbook.md`
