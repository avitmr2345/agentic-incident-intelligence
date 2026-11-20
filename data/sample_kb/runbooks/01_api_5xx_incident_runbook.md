# API 5xx Incident Runbook

## Purpose

Use this runbook when one or more APIs begin returning HTTP 5xx responses.

The goal is to determine whether the failure originates in the API service, a downstream dependency, the gateway, infrastructure, or a recent change.

## Symptoms

Typical symptoms include:

- increased 500 responses
- increased 502 responses
- increased 503 responses
- elevated request latency
- multiple endpoints failing simultaneously
- customer reports of unavailable functionality

## Investigation Workflow

### 1. Establish the Scope

Determine:

- affected endpoint
- affected service
- percentage of failed requests
- whether all users or a subset are affected
- incident start time
- whether failures are isolated to one region/environment if applicable

### 2. Check Metrics

Review:

- request rate
- 5xx error rate
- latency
- saturation/resource utilization

Determine whether the failure began suddenly or increased gradually.

### 3. Check Logs

Search application logs using:

- timestamp
- endpoint
- status code
- correlation ID
- exception type

Look for repeated exceptions rather than isolated errors.

### 4. Check Dependencies

Use the service dependency map to identify downstream systems.

For example, an Order API failure may require checking:

- Order Service
- Product Catalog Service
- Payment Service
- PostgreSQL
- Message Broker

### 5. Check Recent Changes

Review:

- application deployments
- API configuration changes
- secret/configuration changes
- database migrations
- gateway routing changes

A strong temporal correlation does not prove causation, so validate the suspected change with logs and metrics.

## Interpretation

### 500
The application encountered an unexpected internal failure.

### 502
A gateway/proxy received an invalid or unusable upstream response.

### 503
The service or a required dependency is unavailable.

Do not assume the service returning the error is necessarily the root cause.

## Evidence Standard

Before identifying a root cause, try to establish at least two independent signals.

Example:

- Order API 503 rate increased
- traces show Payment Service timeouts
- Payment Service metrics show provider latency increased

This provides stronger evidence than the 503 alone.

## Escalation

Escalate when:

- multiple critical services are affected
- data integrity may be at risk
- payment operations may be duplicated or lost
- the suspected cause cannot be isolated
- recovery requires infrastructure or provider intervention

Related documents:

- `02_service_dependency_map.md`
- `08_observability_architecture.md`
- `09_error_response_and_status_codes.md`
- service-specific architecture and API documents
