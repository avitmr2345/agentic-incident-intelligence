# Service Dependency Map

## Purpose

This document describes direct dependencies between platform components and helps engineers determine whether an incident is local to a service or caused by a downstream dependency.

## Dependency Overview

```text
Client
  |
  v
API Gateway
  |
  +--> Authentication Service --> PostgreSQL / Redis
  |
  +--> User Service -----------> PostgreSQL / Redis
  |
  +--> Product Catalog -------> PostgreSQL / Redis
  |
  +--> Order Service ----------> PostgreSQL
  |        |                    Product Catalog
  |        |                    Payment Service
  |        +------------------> Message Broker
  |
  +--> Payment Service --------> PostgreSQL
  |                             External Payment Provider
  |                             Message Broker
  |
  +--> Notification Service --> Message Broker
                                Email/SMS/Push Providers
```

## Direct Dependencies

### API Gateway
- Authentication Service
- routing configuration
- Redis for rate limiting where enabled
- logging and tracing infrastructure

### Authentication Service
- PostgreSQL
- Redis
- JWT signing configuration
- secret/configuration management

### User Service
- PostgreSQL
- Redis where caching is enabled

### Product Catalog Service
- PostgreSQL
- Redis where product caching is enabled

### Order Service
- PostgreSQL
- Product Catalog Service
- Payment Service
- Redis where applicable
- Message Broker

### Payment Service
- PostgreSQL
- External Payment Provider
- Message Broker

### Notification Service
- Message Broker
- external email/SMS/push providers

## Dependency Failure Patterns

### Direct Failure
A service itself is unhealthy. Example: Order Service returns 500 because its application process is failing.

### Dependency Failure
A service is healthy but a required dependency is failing. Example: Order Service returns 503 because Payment Service is unavailable.

### Cascading Failure
A dependency problem propagates across multiple services. Example: database saturation causes payment timeouts, which delay orders and eventually create a notification backlog.

## Investigation Use

When a user reports an error, identify the owning service and traverse only the dependencies relevant to that path.

For a 503 from order creation, check:

1. Order Service health
2. Order Service database
3. Product Catalog availability
4. Payment Service availability
5. Message Broker health if asynchronous processing is affected

Do not assume every dependency is relevant to every endpoint.

Related documents:
- `01_system_architecture_overview.md`
- service-specific architecture documents
- service API documents
- `08_observability_architecture.md`
