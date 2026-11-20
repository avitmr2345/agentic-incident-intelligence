# Environment and Runtime Architecture

## Purpose
This document describes the environments and runtime boundaries used to operate the platform consistently across development, testing, and production.

## Environments
The platform should maintain clear separation between:
- Development: used for local feature development and debugging.
- Staging: used for integration and deployment validation.
- Production: customer-facing environment.

Each environment should have its own configuration and credentials.

## Runtime Components
The application runtime contains:
- API Gateway
- Authentication Service
- User Service
- Product Catalog Service
- Order Service
- Payment Service
- Notification Service
- PostgreSQL
- Redis
- Message Broker
- Object Storage
- Observability components

## Configuration
Environment-specific values should include:
- Database connection settings.
- Redis connection settings.
- Message broker endpoints.
- Authentication configuration.
- External provider configuration.
- Logging and monitoring configuration.

Application code should not depend on environment-specific hard-coded values.

## Runtime Isolation
Production credentials and data should not be reused in development or staging.

The same service may run with different configuration across environments, so configuration changes must be treated as potential production risks.

## Incident Investigation
When an issue occurs, determine:
1. Which environment is affected.
2. Whether the same deployment exists in other environments.
3. Whether configuration differs.
4. Whether a dependency is environment-specific.
5. Whether the issue began after a deployment or configuration change.

## Related Knowledge
Use with Deployment and Change Management Policy, Security and Secret Handling Policy, System Architecture Overview, and Deployment/Configuration Incident Runbook.
