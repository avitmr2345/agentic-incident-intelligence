# High Latency Incident Runbook

## Purpose

Use this runbook when API response times increase significantly even if error rates remain low.

High latency can be an early signal of an incident before requests begin failing.

## Symptoms

- p95/p99 latency increases
- user-facing pages or APIs become slow
- timeouts begin increasing
- database or dependency latency increases
- queue processing slows
- resource utilization increases

## Investigation Workflow

### 1. Identify the Affected Endpoint

Determine:

- endpoint
- HTTP method
- affected service
- latency percentile affected
- incident start time

Compare p50, p95, and p99 where available.

### 2. Check Traces

Use distributed traces to determine where time is being spent.

Example:

```text
Gateway       20 ms
Order Service 40 ms
Catalog       30 ms
Payment      900 ms
```

This suggests Payment is consuming most of the request time.

### 3. Check Dependencies

Review:

- database latency
- Redis latency
- downstream service latency
- external provider latency
- broker processing latency

### 4. Check Resource Utilization

Inspect:

- CPU
- memory
- connection pools
- worker/thread utilization
- database connections

### 5. Check Traffic

Determine whether request volume increased significantly.

A traffic spike may cause:

```text
Traffic increase
      ↓
Resource saturation
      ↓
Queueing
      ↓
Latency increase
      ↓
Timeouts
      ↓
Retries
      ↓
More load
```

## Root-Cause Patterns

### Slow downstream dependency
Traces show most request time spent waiting on another service.

### Database performance degradation
Database queries become slower and increase request latency.

### Resource saturation
CPU, memory, workers, or connections become constrained.

### Traffic spike
Request volume exceeds the normal operating capacity.

### Retry amplification
Retries create additional traffic and increase latency.

## Recovery

Depending on the confirmed cause:

- restore the slow dependency
- resolve database performance issues
- scale capacity where appropriate
- reduce excessive traffic
- correct retry behavior
- roll back a regression

After recovery, monitor latency percentiles rather than only average latency.

Related documents:

- `08_observability_architecture.md`
- `07_data_storage_and_cache_architecture.md`
- `02_service_dependency_map.md`
- service-specific architecture documents
