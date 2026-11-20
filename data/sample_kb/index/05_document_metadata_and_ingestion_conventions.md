# Document Metadata and Ingestion Conventions

## Purpose
This document defines conventions for preparing the knowledge base for chunking, embedding, retrieval, and agentic reasoning.

## Source Categories
Documents belong to one of these categories:
- architecture
- api
- runbook
- incident
- policy
- infrastructure
- index

## Recommended Metadata
Each ingested document should be associated with metadata such as:
- `document_id`
- `title`
- `category`
- `service`
- `topic`
- `source_type`

Optional metadata:
- `incident_id`
- `severity`
- `api_version`
- `dependency`
- `environment`

## Chunking Principles
Chunks should preserve enough context to remain meaningful when retrieved independently.

Avoid:
- Splitting a heading from all of its relevant content.
- Creating extremely small fragments with no useful context.
- Combining unrelated sections simply to increase chunk size.

## Retrieval Metadata
Metadata can help narrow retrieval when the user clearly identifies:
- A service.
- An incident type.
- A document category.
- A dependency.

However, metadata filters should not be so restrictive that useful cross-document evidence is excluded.

## Cross-Document Retrieval
The knowledge base intentionally contains relationships across document types.

For example:
- Architecture explains dependencies.
- APIs explain observable behavior.
- Runbooks explain investigation.
- Historical incidents provide previous failure patterns.
- Policies explain expected operational behavior.
- Infrastructure documents explain runtime conditions.

## Source Attribution
The final Agentic RAG response should identify the supporting internal sources when appropriate.

## Ingestion Changes
When documents are added or modified:
1. Re-ingest affected content.
2. Ensure stale vectors are replaced or versioned appropriately.
3. Validate retrieval for representative questions.
4. Check that document relationships remain discoverable.

## Related Knowledge
This convention supports the ingestion pipeline from Markdown source documents to chunks, embeddings, Pinecone retrieval, evidence grading, and final grounded responses.
