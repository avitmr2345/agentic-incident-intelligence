# Historical Incident: Database Connection Pool Exhaustion

## Summary
Order API latency increased and eventually produced database-related failures.

## Impact
Order requests became slow and some requests failed.

## Detection
Application metrics showed database connection pool utilization reaching its configured limit.

## Investigation
Database monitoring showed a high number of active connections and several long-running operations.

## Root Cause
A workload change caused long-running database operations to hold connections longer than expected, exhausting the application connection pool.

## Resolution
The problematic workload was addressed and affected services recovered.

## Validation
Connection pool usage, query latency, and API latency returned to normal.

## Lessons Learned
Application-level connection pool metrics should be monitored together with database connection metrics.

Related:
- `06_database_incident_runbook.md`
- `07_data_storage_and_cache_architecture.md`
