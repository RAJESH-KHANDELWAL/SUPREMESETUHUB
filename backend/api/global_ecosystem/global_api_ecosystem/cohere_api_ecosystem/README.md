# COHERE API ECOSYSTEM

Canonical provider-owned API catalog for Cohere integrations in SUPREMESETUHUB.

## Provider structure

- `cohere_api_ecosystem.py` — provider metadata and API-family listing.
- `cohere_command_api_ecosystem/` — Command model inference.
- `cohere_embed_api_ecosystem/` — text and supported multimodal/document embeddings.
- `cohere_rerank_api_ecosystem/` — search/retrieval reranking.
- `cohere_tokenize_api_ecosystem/` — tokenization and model metadata where supported.
- `cohere_classify_api_ecosystem/` — classification capabilities where currently supported.

Shared provider adapter: `backend/integrations/providers/cohere.py`.

Shared integration registration: `backend/integrations/registry.py` (provider key: `COHERE`).

## API family overview

| Family | Purpose | Setup boundary |
|---|---|---|
| Command | Text generation and conversational inference | Check current model availability and supported API version |
| Embed | Text/document and supported multimodal embeddings | Validate input type, embedding dimensions and model |
| Rerank | Relevance scoring and document reranking | Validate query/document limits and model |
| Tokenize & metadata | Token counts/tokenization and model metadata where exposed | Do not assume every utility endpoint is available to every account |
| Classification | Classification where supported by current Cohere APIs | Confirm endpoint, model and account entitlement before enablement |

## Configuration

The readiness adapter checks the server-side environment variable:

- `COHERE_API_KEY`

Supply the key only through deployment environment configuration or a managed secret store. Do not place it in source code, browser storage, frontend variables or logs.

## Security and operations

- Enforce tenant-level authorization and usage limits.
- Apply bounded timeouts and retries for transient failures.
- Handle rate limits, quota responses and API errors.
- Validate model identifiers, input sizes and output schemas.
- Redact authorization headers and credentials from logs.
- Keep model access and customer data scoped to the requesting tenant.

## Status semantics

- `NEEDS_CONFIGURATION`: `COHERE_API_KEY` is not present.
- `CONFIGURED_NOT_VERIFIED`: the key is present; no live request has been validated.
- `CONNECTED`: only report after a safe authenticated request to a currently supported Cohere endpoint succeeds.

The adapter currently checks only configuration presence. It does not exchange tokens or call Cohere APIs. Each API family remains a documentation/catalog scaffold until implemented and tested independently.
