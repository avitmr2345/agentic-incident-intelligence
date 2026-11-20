# Historical Incident: Redis Failure Increased Database Load

## Summary
Redis became unavailable for a service that depended on it for caching. Cache misses increased and database traffic rose sharply.

## Impact
API latency increased and PostgreSQL resource utilization approached its normal operating limit.

## Investigation
Redis connection errors increased first. Shortly afterward, cache hit rate dropped and database query volume increased.

## Root Cause
Redis availability degraded, causing requests to bypass the cache and repeatedly query PostgreSQL.

## Resolution
Redis availability was restored and cache behavior returned to normal.

## Lessons Learned
Cache failures can create secondary database incidents. Redis and database metrics should be correlated during investigation.

Related:
- `07_redis_cache_incident_runbook.md`
- `07_data_storage_and_cache_architecture.md`
