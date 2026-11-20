# Historical Incident: Authentication 401 Errors After Deployment

## Summary
Protected APIs began returning HTTP 401 shortly after an authentication-related deployment. Login requests continued to succeed, but tokens issued after deployment were rejected by downstream verification.

## Impact
Authenticated users could log in but could not access protected APIs such as user and order endpoints.

## Detection
Monitoring showed a sharp increase in HTTP 401 responses while authentication login success remained normal.

## Investigation
Engineers compared the request path:

Client -> API Gateway -> Authentication/Token Verification -> Protected Service

Logs showed token verification failures. The token issuer and signing configuration were compared between the token issuer and verifier.

## Root Cause
The deployment introduced a JWT configuration mismatch. Tokens were issued using configuration that did not match the configuration expected by the verification layer.

## Resolution
The authentication configuration was restored to the known-good values and the service was redeployed.

## Validation
Engineers verified:
- login success
- protected endpoint access
- 401 error rate
- token issuance and verification
- gateway request flow

## Lessons Learned
Authentication configuration changes should be validated against both token issuance and token verification paths before production rollout.

Related:
- `03_authentication_architecture.md`
- `02_authentication_401_incident_runbook.md`
- `02_authentication_api.md`
