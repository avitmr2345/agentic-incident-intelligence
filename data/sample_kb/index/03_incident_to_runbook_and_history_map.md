# Incident-to-Runbook and Historical Incident Map

## Purpose
This map connects recurring incident symptoms to the most relevant troubleshooting runbooks and historical incidents.

| Symptom | Primary Runbook | Related Historical Incident |
|---|---|---|
| Login succeeds but protected APIs return 401 | Authentication 401 Runbook | Authentication 401 After Deployment |
| Broad API 5xx increase | API 5xx Runbook | Multiple service-specific incidents |
| Order creation returns 503 | Order Creation 503 Runbook | Order 503 Payment Timeout |
| Payment requests time out | Payment Timeout Runbook | Payment Provider Latency |
| Notifications are delayed | Notification Delay Runbook | Notification Queue Backlog |
| Database connections exhausted | Database Runbook | Database Connection Exhaustion |
| Redis unavailable | Redis Runbook | Redis Failure Database Load |
| Message consumer repeatedly crashes | Message Broker Runbook | Message Consumer Crash |
| Failure starts after deployment | Deployment/Configuration Runbook | Deployment Regression |
| Service is running but not ready | Deployment/Configuration Runbook | Readiness Failure |
| p95/p99 latency increases | High Latency Runbook | High Latency Database Queries |
| Users receive unexpected 429 responses | API 5xx/appropriate API investigation | Rate Limit Incident |
| Client retries a payment after timeout | Payment Timeout Runbook | Payment Duplicate Request Prevented |
| One notification provider fails | Notification Delay Runbook | Partial Notification Provider Failure |
| Orders fail across multiple dependencies | Order Creation 503 Runbook | Cascading Order Incident |
| Product/catalog latency follows cache expiry | Redis/High Latency Runbook | Cache Stampede Catalog |

## Investigation Pattern
For a new incident:
1. Identify the observable symptom.
2. Select the matching runbook.
3. Check the historical incident map for similar failures.
4. Retrieve architecture and API evidence for the affected component.
5. Apply relevant operational policies.
6. Compare current evidence with historical root causes.

## Important Constraint
A matching historical incident is evidence for investigation, not proof that the current incident has the same root cause.
