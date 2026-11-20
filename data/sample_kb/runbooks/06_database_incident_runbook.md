# Database Incident Runbook

## Purpose

Use this runbook when a service reports database errors, increased query latency, connection failures, or database-related timeouts.

## Symptoms

Common symptoms include:

- HTTP 500 or 503 responses
- increased API latency
- database connection errors
- connection pool exhaustion
- slow queries
- lock waits
- transaction failures

## Investigation Workflow

### 1. Establish Scope

Determine:

- affected service
- affected endpoint
- incident start time
- percentage of requests affected
- whether multiple services using the same database are affected

### 2. Check Application Signals

Review:

- database connection errors
- connection pool usage
- query latency
- transaction failures
- timeout counts

### 3. Check Database Health

Inspect available database metrics for:

- CPU utilization
- memory pressure
- storage capacity
- active connections
- lock waits
- query latency

### 4. Check Recent Changes

Review:

- schema migrations
- application deployments
- query changes
- configuration changes
- traffic increases

### 5. Identify the Failure Pattern

#### Connection Exhaustion

If the application cannot obtain database connections, inspect:

- connection pool limits
- active connections
- long-running requests
- leaked connections
- sudden traffic increases

#### Query Latency

If connections are available but queries are slow, investigate:

- expensive queries
- lock contention
- database resource pressure
- recent schema/index changes

#### Storage Pressure

Low storage can cause writes or other database operations to fail.

## Root-Cause Evidence

A strong conclusion should connect application behavior with database evidence.

Example:

```text
Order API latency increased
        +
Order Service connection pool reached its limit
        +
Database active connections increased sharply
```

This is stronger evidence than an application timeout alone.

## Recovery

Depending on the confirmed cause:

- resolve the blocking query/transaction
- restore database capacity
- correct an inefficient query
- roll back a faulty migration/change
- reduce unnecessary traffic
- restart affected application components only when appropriate

Do not restart services blindly if doing so could hide the underlying database problem.

Related documents:

- `07_data_storage_and_cache_architecture.md`
- `04_order_service_architecture.md`
- `08_observability_architecture.md`
