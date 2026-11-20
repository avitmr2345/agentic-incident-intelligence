# Query Routing and Retrieval Guide

## Purpose
This document provides examples of how incident questions can be decomposed into the knowledge sources required for evidence-based retrieval.

## Single-Document Queries
Some questions can be answered primarily from one source.

Examples:
- "What does the health endpoint mean?" → Health and Readiness Endpoints.
- "What payment states exist?" → Payment Service Architecture or Payment API.
- "What causes Redis cache pressure?" → Data Storage and Cache Architecture.

## Multi-Document Queries

### Authentication After Deployment
Question:
"Users can log in, but protected APIs return 401 after today's deployment."

Likely retrieval:
1. Authentication Architecture.
2. Authentication API.
3. Deployment and Configuration Runbook.
4. Security and Secret Handling Policy.
5. Authentication 401 Historical Incident.
6. Configuration and Secrets Runtime.

### Order 503 With Payment Timeout
Question:
"Order creation is returning 503 and payment requests are timing out."

Likely retrieval:
1. Order Service Architecture.
2. Order API.
3. Payment Service Architecture.
4. Payment Timeout Runbook.
5. Order 503 Payment Timeout Historical Incident.
6. Retry/Timeout/Idempotency Policy.

### Notification Backlog
Question:
"Notifications are delayed and the queue is growing."

Likely retrieval:
1. Notification Service Architecture.
2. Notification API.
3. Message Broker Runbook.
4. Notification Delay Runbook.
5. Notification Queue Backlog Historical Incident.
6. Capacity and Performance Operations.

### High Latency
Question:
"Product requests became slow without a large traffic increase."

Likely retrieval:
1. Product Catalog API.
2. Data Storage and Cache Architecture.
3. High Latency Runbook.
4. High Latency Database Historical Incident.
5. Cache Stampede Historical Incident.
6. Capacity and Performance Operations.

## Retrieval Strategy
The system should prefer evidence that:
- Directly addresses the incident.
- Identifies the affected component.
- Describes dependencies.
- Provides diagnostic signals.
- Explains recovery or mitigation.
- Is consistent with other retrieved documents.

## Query Refinement
If the initial retrieval is weak, rewrite the query using:
- Service name.
- Endpoint.
- Error code.
- Dependency.
- Observable symptom.
- Deployment timing.
- Relevant operational term.

## Web Fallback
External search should be considered only after internal knowledge retrieval is insufficient, because the incident knowledge base represents the primary source of truth for the fictional platform.
