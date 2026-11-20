# Evidence Trace and Final Knowledge Base Validation

## Purpose
This document defines how to validate that the knowledge base supports grounded incident investigation rather than isolated keyword matching.

## Evidence Requirements
A useful retrieved evidence set should provide enough information to establish:
- What component is affected.
- What the component depends on.
- What symptoms are expected.
- What investigation steps should be performed.
- What known historical patterns may be relevant.
- What recovery actions are appropriate.

## Cross-Document Consistency
The following relationships should remain consistent:
- Service names across architecture and API documents.
- Endpoint names across API documents and runbooks.
- Dependency relationships across architecture and incident reports.
- Incident symptoms with their referenced runbooks.
- Policies with the operational behavior described in runbooks.

## Validation Questions
Representative queries should include:

1. "Login works but protected endpoints return 401 after deployment. What should I investigate?"
2. "Orders are returning 503 because payment calls are timing out. What is the likely dependency chain?"
3. "Notification queue depth is increasing. What should I check?"
4. "Redis is unavailable and database traffic has increased. Why?"
5. "A deployment caused order requests to fail. How do I determine whether it was a compatibility regression?"
6. "A payment request timed out and the client retried. How do we avoid duplicate charges?"
7. "The service is running but readiness is failing. What dependencies should I inspect?"
8. "Product latency increased after cache expiry. What could cause this?"
9. "How should a significant incident be documented after recovery?"

## Expected Retrieval
A strong system should retrieve multiple relevant sources when the question spans:
- Architecture.
- API behavior.
- Troubleshooting.
- Historical evidence.
- Policies.
- Infrastructure.

## Evidence Grading
The agent should distinguish:
- Relevant evidence.
- Partially relevant evidence.
- Irrelevant evidence.
- Conflicting or ambiguous evidence.

Low-quality retrieval should trigger query refinement rather than unsupported conclusions.

## Final Response Validation
Before producing a final incident response, the agent should check:
1. Is the explanation grounded in retrieved evidence?
2. Are assumptions clearly distinguished from facts?
3. Are investigation steps actionable?
4. Are supporting sources available?
5. Is the proposed cause consistent with the observed symptoms?
6. Has uncertainty been communicated where evidence is insufficient?

## Completion Criterion
The knowledge base should be considered ready for the first Agentic RAG implementation when representative incident questions can retrieve coherent evidence across the relevant document layers.
