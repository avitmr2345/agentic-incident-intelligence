# Data Storage and Cache Architecture

## Purpose

This document describes durable storage and caching patterns used by the platform.

## PostgreSQL

PostgreSQL is the primary durable store for business data.

Typical ownership:

- Authentication: identity and authentication-related records
- User Service: profile and preference data
- Product Catalog: product/catalog data
- Order Service: orders and lifecycle state
- Payment Service: payment records

Services should access data through their own service boundaries rather than directly modifying another service's tables.

## Redis

Redis is used for short-lived or performance-sensitive data such as:

- cache entries
- rate-limit state
- temporary session-related state where configured

Redis should not be treated as the source of truth for durable business records unless explicitly designed for that purpose.

## Cache Failure Behavior

A cache miss should normally cause the service to retrieve the authoritative data from PostgreSQL or another configured source.

A Redis outage can therefore produce:

- increased database traffic
- increased request latency
- rate-limiting issues
- cache-related application errors, depending on implementation

## Database Incident Signals

Check:

- connection errors
- connection pool saturation
- query latency
- lock waits
- CPU/memory pressure
- storage capacity
- recent schema or deployment changes

## Cache Incident Signals

Check:

- cache hit rate
- Redis connection errors
- latency
- memory usage
- eviction activity
- rate-limit behavior

Related documents:
- `02_service_dependency_map.md`
- `08_observability_architecture.md`
- service-specific architecture documents
