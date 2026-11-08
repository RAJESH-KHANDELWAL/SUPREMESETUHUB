# Cohere Tokenization and Model Metadata

Provider: COHERE API ECOSYSTEM

## Scope

Token counting/tokenization and model metadata only where exposed by Cohere's current supported API/SDK.

## Authentication and setup

Use a Cohere API key supplied through the server-side `COHERE_API_KEY` environment variable or managed secret storage. Never hard-code the key, commit it, expose it to browser code, or log authorization headers. Confirm model availability, account entitlements, supported endpoint and API version before enabling any operation.

## Operational requirements

- Apply request timeouts and bounded retries for transient failures.
- Handle rate limits, usage quotas and API error responses.
- Validate input size, model identifiers and response schemas.
- Redact credentials and sensitive user content from logs.
- Enforce tenant-level authorization and per-tenant usage limits.

## Status

Catalog/documentation scaffold only. This folder does not execute live Cohere API requests or validate credentials.
