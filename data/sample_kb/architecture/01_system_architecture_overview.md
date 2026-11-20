# System Architecture Overview

## Purpose
The Commerce Platform is a modular enterprise application that supports customer accounts, product discovery, order processing, payments, notifications, and operational workflows.

This document explains the major components, request flow, asynchronous events, ownership boundaries, and the signals engineers should use when investigating incidents.

## Major Components

- API Gateway
- Authentication Service
- User Service
- Product Catalog Service
- Order Service
- Payment Service
- Notification Service
- PostgreSQL databases
- Redis
- Message Broker
- Object Storage
- Centralized logging, metrics, and tracing

Each service owns its business logic and primary data. Cross-service workflows are coordinated through synchronous API calls and asynchronous events.

## Request Flow

A typical synchronous request follows:

Client -> API Gateway -> Target Service -> Database/Cache -> Response

The API Gateway handles routing, authentication forwarding, request validation, rate limiting, correlation IDs, and access logging.

Services may use Redis for short-lived state or caching and PostgreSQL for durable business data.

Long-running or non-critical side effects are commonly handled asynchronously:

Service -> Message Broker -> Consumer -> Downstream Provider/Service

## Core Service Responsibilities

### Authentication Service
Handles login, token issuance, token refresh, and authentication-related validation.

### User Service
Manages user profiles and preferences.

### Product Catalog Service
Provides product information and catalog search.

### Order Service
Owns order creation, lifecycle transitions, and order-related orchestration.

### Payment Service
Coordinates payment authorization/capture with the external payment provider.

### Notification Service
Consumes events and delivers email, SMS, or push notifications.

## Important Events

Common events include:

- `OrderCreated`
- `PaymentAuthorized`
- `PaymentFailed`
- `OrderCompleted`
- `NotificationRequested`

Consumers should process events idempotently because messages may be retried or delivered more than once.

## Reliability Principles

The platform uses:

- bounded retries
- request timeouts
- idempotent operations and consumers
- correlation IDs
- health and readiness endpoints
- structured logs
- metrics and distributed tracing

Retries should not be used blindly. A retry can increase load when the underlying dependency is already unhealthy.

## Incident Investigation

When investigating an incident, engineers should first establish:

1. Which user-facing symptom is occurring?
2. Which endpoint or workflow is affected?
3. Which service owns that behavior?
4. Which dependencies does that service require?
5. Are failures isolated or widespread?
6. Did a deployment or configuration change occur recently?
7. What do logs, metrics, and traces show?

Related documents:
- `02_service_dependency_map.md`
- `08_observability_architecture.md`
- relevant service architecture and API documents
