# Redis and Cache Incident Runbook

## Purpose

Use this runbook when Redis connectivity, cache performance, rate limiting, or cache-related behavior becomes abnormal.

## Symptoms

Possible symptoms:

- increased API latency
- Redis connection errors
- reduced cache hit rate
- increased database traffic
- unexpected rate-limit behavior
- cache-related application failures

## Investigation Workflow

### 1. Determine Redis Usage

Identify whether the affected service uses Redis for:

- caching
- rate limiting
- temporary state
- session-related functionality

The impact depends on how Redis is used by that service.

### 2. Check Application Metrics

Review:

- cache hit rate
- cache miss rate
- Redis request latency
- Redis connection errors
- timeout count

### 3. Check Redis Health

Inspect available signals such as:

- memory utilization
- evictions
- connection count
- latency
- availability
- resource pressure

### 4. Compare Database Traffic

A Redis problem may indirectly increase PostgreSQL traffic because cache misses force more requests to the authoritative database.

Look for:

```text
Redis failure
    ↓
Cache misses increase
    ↓
Database requests increase
    ↓
Database latency increases
```

This can become a cascading incident.

### 5. Check Rate Limiting

If Redis stores rate-limit state, verify whether:

- valid requests are being rejected
- limits are not being enforced
- rate-limit state is unavailable

## Root-Cause Patterns

### Redis unavailable
Applications cannot connect to Redis.

### Cache degradation
Redis is available but latency or eviction behavior has changed.

### Cache stampede
Many requests simultaneously miss the cache and overload the database.

### Rate-limit state failure
Rate limiting behaves unexpectedly because Redis state cannot be read or written.

## Recovery

After fixing Redis:

1. verify connectivity
2. verify cache hit rate
3. monitor database traffic
4. verify API latency
5. verify rate-limit behavior
6. monitor for continued cascading effects

Related documents:

- `07_data_storage_and_cache_architecture.md`
- `02_service_dependency_map.md`
- `08_observability_architecture.md`
