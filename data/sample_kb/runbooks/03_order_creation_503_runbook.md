# Order Creation 503 Runbook

## Purpose

Use this runbook when order creation requests begin returning HTTP 503.

## Example Symptom

```text
POST /api/v1/orders -> 503
```

A 503 does not automatically mean that the Order Service itself is broken.

## Dependency Path

A typical order creation path is:

```text
API Gateway
    |
    v
Order Service
    |
    +--> Product Catalog
    |
    +--> PostgreSQL
    |
    +--> Payment Service
              |
              v
      External Payment Provider
```

## Investigation Workflow

### 1. Check Order Service

Inspect:

- `/health`
- `/ready`
- error rate
- request latency
- application logs
- resource utilization

### 2. Check Product Catalog

Determine whether product validation calls are:

- failing
- timing out
- returning unexpected responses
- experiencing increased latency

### 3. Check Payment Service

Inspect:

- payment request latency
- timeout rate
- 5xx responses
- provider response errors
- recent configuration changes

### 4. Check Database

Review:

- connection errors
- connection pool saturation
- query latency
- database resource pressure
- recent schema changes

### 5. Check Message Broker

If order creation succeeds but downstream processing is delayed, inspect:

- queue depth
- consumer health
- processing latency
- failed messages

## Root-Cause Examples

### Payment dependency timeout

Evidence may include:

- Order API 503 increase
- traces showing Order Service waiting on Payment Service
- Payment Service timeout increase

### Database saturation

Evidence may include:

- order requests slow before failing
- database connection pool exhaustion
- elevated query latency
- database resource pressure

### Application deployment failure

Evidence may include:

- failure starts immediately after deployment
- readiness failures
- application startup errors
- increased 5xx responses

## Recovery

Depending on the confirmed cause:

- restore a failing dependency
- roll back a faulty deployment
- correct configuration
- reduce excessive traffic where appropriate
- resolve database saturation
- restore payment provider connectivity

Validate successful order creation after recovery.

Related documents:

- `04_order_service_architecture.md`
- `04_order_api.md`
- `05_payment_service_architecture.md`
- `05_payment_api.md`
- `08_health_and_readiness_endpoints.md`
