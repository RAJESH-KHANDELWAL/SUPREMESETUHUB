# OPENAI API ECOSYSTEM

Canonical provider folder:

`backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/`

Provider ID: `openai`  
Display name: `OPENAI API ECOSYSTEM`  
Catalog module: `openai_api_ecosystem.py`

## Purpose

This provider-owned ecosystem is the canonical catalog and onboarding boundary for OpenAI Platform APIs. It is separate from the shared AI, Developer, Tools, Language, Database, and other category ecosystems.

## Capability map

The catalog currently defines these 17 independently organizable capability areas:

1. Platform
2. Models
3. Responses
4. Chat Completions
5. Embeddings
6. Images
7. Audio
8. Realtime
9. Files
10. Batch
11. Vector Stores
12. Fine-tuning
13. Moderation
14. Evaluations
15. Webhooks
16. Developer Tools
17. Assistants migration reference

These are catalog entries, not 17 completed production adapters. Each adapter must be implemented and tested against the current official OpenAI Platform documentation before it is advertised as available.

## Intended user connection experience

The product-side experience should be simple:

1. User opens **OPENAI API ECOSYSTEM**.
2. User chooses **Connect OpenAI**.
3. User provides their own OpenAI API key in a protected input (or selects an approved managed-secret integration).
4. Backend validates the credential with a minimal, documented API request.
5. UI shows connected / invalid / revoked state without revealing the secret.
6. User can disconnect, rotate the key, and view usage and cost controls where supported.

Users should not need to configure backend infrastructure themselves. Administrators configure the secret-management service and deployment environment once; individual users only connect their authorized credentials through the product UI.

## Security requirements

- Never commit API keys or place them in source code, logs, URLs, analytics, or error responses.
- Never send a user's key to the browser after initial submission.
- Use authenticated, tenant-scoped authorization for every credential operation.
- Encrypt credentials at rest using a managed KMS or equivalent secret vault.
- Redact authorization headers and secrets from logs and traces.
- Apply request timeouts, rate limits, usage metering, and configurable cost limits.
- Support credential rotation and revocation.
- Do not confuse ChatGPT subscription access with OpenAI API billing or API-key access.

## Implementation status

This folder currently contains provider catalog metadata and architecture guidance only. It does **not** yet provide the full multi-user connection UI, authenticated connection routes, durable encrypted per-user key storage, usage metering, or production endpoint adapters. `live_connection_verified` must remain false until a real credential is safely tested in the deployed environment.

## Integration points in this repository

- Shared AI category: `global_ai_api_ecosystem/openai_ai_api_ecosystem`
- Shared Developer category: `global_developer_api_ecosystem/openai_developer_api_ecosystem`
- Shared Tools category: `global_tools_api_ecosystem/openai_tools_api_ecosystem`
- Shared Language category: `global_language_api_ecosystem/openai_language_api_ecosystem`
- Shared Database reference: `global_database_api_ecosystem/openai_database_api_ecosystem`
- Central provider registry: `backend/api/global_api_ecosystem_catalog.py`
- Existing runtime image connector: `backend/integrations/connectors/openai_image.py`
- Existing central AI engine registry: `backend/engines/ai/manager.py`

The category folders are reusable cross-provider capability groupings. The provider-owned folder remains the authoritative OpenAI provider identity and catalog.

## Documentation

Before implementing or enabling any capability, verify current endpoint availability, authentication requirements, model access, account entitlements, regional availability, and lifecycle status in the official OpenAI Platform documentation.