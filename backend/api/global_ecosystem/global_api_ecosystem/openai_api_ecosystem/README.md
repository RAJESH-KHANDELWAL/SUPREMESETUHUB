# OPENAI API ECOSYSTEM

Canonical provider folder:

`backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/`

Provider identity:
- Provider ID: `openai`
- Display name: `OPENAI API ECOSYSTEM`
- Catalog module: `openai_api_ecosystem.py`

## Capability catalog

The catalog separates official OpenAI API capability areas into independently
organizable modules: Platform, Models, Responses, Chat Completions, Embeddings,
Images, Audio, Realtime, Files, Batch, Vector Stores, Fine-tuning, Moderation,
Evaluations, Webhooks, Developer Tools, and an Assistants migration reference.

The child entries are architecture/catalog records. They do not mean that each
child has a production adapter or that a live connection has been tested.

## Intended connection flow

1. An authenticated user opens OpenAI API Ecosystem.
2. The user supplies their own OpenAI API key through a protected connection UI.
3. The backend validates the key with a minimal official API request.
4. The backend stores the key only in an encrypted, tenant-scoped secret store.
5. The user can inspect connection status, usage/cost limits, rotate or revoke the key.

## Security and implementation boundary

- Never commit API keys or place them in source code, logs, URLs, or responses.
- Do not treat a ChatGPT subscription as API billing or API-key access.
- Production multi-user onboarding requires authenticated routes, encrypted
  per-user secret storage, authorization checks, rate limits, usage metering,
  cost controls, rotation, and revocation.
- These user onboarding and durable credential-storage workflows are not
  implemented by this catalog change.
- `live_connection_verified` remains false until a real credential is tested
  safely in the deployed environment.

Consult the current official OpenAI Platform documentation before implementing
individual endpoint adapters, because API availability and lifecycle can change.
