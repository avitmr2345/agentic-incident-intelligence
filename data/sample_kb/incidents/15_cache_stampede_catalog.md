# Historical Incident: Product Catalog Cache Stampede

## Summary
A cache expiration event caused many requests to miss Redis simultaneously, producing a sudden increase in database traffic.

## Impact
Product Catalog latency increased and some requests timed out.

## Investigation
Redis remained available, but cache hit rate dropped sharply. PostgreSQL query volume increased at the same time.

## Root Cause
A large group of frequently requested cache entries expired within a short period, causing many requests to query the database concurrently.

## Resolution
Cache behavior was stabilized and database load returned to normal.

## Lessons Learned
Cache availability alone is not enough. Cache hit rate and database load should be monitored together.

Related:
- `07_redis_cache_incident_runbook.md`
- `03_product_catalog_api.md`
- `07_data_storage_and_cache_architecture.md`
