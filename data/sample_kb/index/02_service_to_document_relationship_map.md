# Service-to-Document Relationship Map

## Purpose
This document maps each major service to the knowledge sources most likely to contain evidence about that service.

## API Gateway
Primary:
- System Architecture Overview
- Service Dependency Map
- API Gateway
- Error Response and Status Codes
- Observability Architecture
- Logging and Correlation ID Policy
- Deployment Architecture

Common investigation topics:
- Routing failures
- Authentication forwarding
- Rate limiting
- 4xx/5xx responses
- Correlation IDs

## Authentication Service
Primary:
- Authentication Architecture
- Authentication API
- Authentication 401 Incident Runbook
- Authentication 401 Historical Incident
- Security and Secret Handling Policy
- Configuration and Secrets Runtime

Common investigation topics:
- Login failures
- Token validation
- JWT configuration
- 401 versus 403
- Secret/configuration changes

## Product Catalog Service
Primary:
- System Architecture Overview
- Product Catalog API
- Order Service Architecture
- High Latency Runbook
- High Latency Database Historical Incident
- Cache Stampede Historical Incident

Common investigation topics:
- Product lookup failures
- Catalog latency
- Database pressure
- Cache behavior

## Order Service
Primary:
- Order Service Architecture
- Order API
- Order Creation 503 Runbook
- Cascading Order Historical Incident
- Deployment Regression Historical Incident
- Retry/Timeout/Idempotency Policy

Common investigation topics:
- Order 503
- Payment dependency failures
- Order lifecycle
- API validation regressions
- Retry amplification

## Payment Service
Primary:
- Payment Service Architecture
- Payment API
- Payment Timeout Runbook
- Payment Provider Latency Historical Incident
- Payment Duplicate Request Historical Incident
- Retry/Timeout/Idempotency Policy
- Data Integrity and Reconciliation Policy

Common investigation topics:
- Provider latency
- Payment timeout
- duplicate requests
- idempotency
- reconciliation

## Notification Service
Primary:
- Notification Service Architecture
- Notification API
- Notification Delay Runbook
- Notification Queue Backlog Historical Incident
- Partial Provider Failure Historical Incident
- Message Broker Runbook

Common investigation topics:
- Queue backlog
- consumer failures
- provider failures
- delayed delivery

## PostgreSQL
Primary:
- Data Storage and Cache Architecture
- Database Incident Runbook
- Database Connection Exhaustion Historical Incident
- High Latency Database Historical Incident
- Data Integrity and Reconciliation Policy
- Capacity and Performance Operations

## Redis
Primary:
- Data Storage and Cache Architecture
- Redis/Cache Incident Runbook
- Redis Failure Historical Incident
- Cache Stampede Historical Incident
- Capacity and Performance Operations

## Message Broker
Primary:
- Service Dependency Map
- Message Broker Incident Runbook
- Message Consumer Crash Historical Incident
- Notification Queue Backlog Historical Incident
- Data Integrity and Reconciliation Policy

## External Providers
Primary:
- Payment Service Architecture
- Notification Service Architecture
- Payment Timeout Runbook
- Payment Provider Latency Historical Incident
- Partial Notification Provider Failure Historical Incident
- Networking and Service Connectivity
