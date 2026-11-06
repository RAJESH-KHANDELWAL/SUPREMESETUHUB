# COHERE API ECOSYSTEM

This directory is the canonical provider-owned catalog for Cohere integrations in SUPREMESETUHUB.

## Provider scope

Cohere provides enterprise AI capabilities. This catalog covers only relevant, officially supported API families:

- **Command models** — text generation and conversational/model inference.
- **Embed** — text and document embeddings for semantic retrieval.
- **Rerank** — relevance reranking for search and retrieval pipelines.
- **Tokenization and model metadata** — only where exposed by the current official API and account access.

## Architecture

- Provider catalog: `cohere_api_ecosystem.py`
- Shared category routing: GLOBAL AI and GLOBAL DEVELOPER API ECOSYSTEM mappings.
- Provider adapter and IntegrationRegistry registration: not yet implemented.
- Live API connectivity: not verified.

## Setup boundary

A future adapter should accept a Cohere API key from server-side environment configuration (for example, `COHERE_API_KEY`), never from source code or client-side browser storage. It should validate configuration, use official Cohere API endpoints and supported SDK/API versions, apply timeouts and bounded retries, redact credentials from logs, and enforce tenant-level authorization and usage limits.

Do not treat catalog presence or a configured key as proof of successful connectivity. A live status should be reported only after a safe authenticated API health/model-list request succeeds.

## Implementation status

**CATALOG_ONLY** — this directory documents provider scope and routing. It does not currently make network calls, store credentials, or claim that Cohere is connected.
