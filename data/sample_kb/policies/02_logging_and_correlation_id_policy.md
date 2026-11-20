# Logging and Correlation ID Policy

## Purpose
This policy defines the minimum logging and request-correlation practices required for effective incident investigation.

## Correlation IDs
Every inbound request should have a correlation identifier.

The API Gateway should:
- Accept an incoming `X-Correlation-ID` when supplied.
- Generate one when absent.
- Propagate it to downstream services.
- Include it in access logs and relevant application logs.

Services should preserve the same identifier across synchronous downstream calls and associate it with asynchronous processing when supported by the message metadata.

## Required Log Information
Relevant operational logs should include:
- Timestamp.
- Service name.
- Environment.
- Log level.
- Correlation ID.
- Request or operation name.
- Relevant resource identifier where appropriate.
- HTTP status or operation result.
- Error type and useful diagnostic context.

## Structured Logging
Operational logs should use structured fields rather than relying exclusively on free-form messages.

Example fields:
- `service`
- `environment`
- `level`
- `correlation_id`
- `request_id`
- `operation`
- `status_code`
- `duration_ms`
- `error_type`

## Sensitive Data
Logs must not expose:
- Passwords.
- Authentication tokens.
- Secret keys.
- Payment credentials.
- Other sensitive customer information.

Diagnostic context should be sufficient to investigate the failure without exposing confidential values.

## Incident Investigation
For an API failure, engineers should correlate:
1. Gateway access logs.
2. Service application logs.
3. Downstream dependency logs.
4. Relevant metrics.
5. Distributed traces when available.

The correlation ID should be used as the primary link between these signals.

## Logging Failure Considerations
If logs are missing:
- Check the service health.
- Check log collection.
- Check logging configuration.
- Use metrics and traces as alternate evidence.
- Do not assume that absence of logs means absence of an application failure.

## Related Knowledge
Use this policy with the Observability Architecture, API Gateway documentation, error-response policy, and incident runbooks.
