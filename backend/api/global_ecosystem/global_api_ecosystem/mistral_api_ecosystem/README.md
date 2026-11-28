# MISTRAL AI API ECOSYSTEM

Canonical Mistral AI provider catalog for SUPREMESETUHUB.

## Service families
- `mistral_chat_api_ecosystem/` — chat completions.
- `mistral_models_api_ecosystem/` — model discovery and metadata.
- `mistral_embeddings_api_ecosystem/` — text embeddings.
- `mistral_agents_api_ecosystem/` — agents and agent execution.
- `mistral_ocr_api_ecosystem/` — document and image OCR.
- `mistral_fine_tuning_api_ecosystem/` — fine-tuning jobs.
- `mistral_batch_api_ecosystem/` — asynchronous batch jobs.
- `mistral_fim_completions_api_ecosystem/` — fill-in-the-middle/code completions.
- `mistral_audio_api_ecosystem/` — supported audio endpoints.

Shared runtime adapter: `backend/integrations/providers/mistral.py`. Registry key: `MISTRAL`.

## Setup and verification
Create a Mistral API key and add it to backend deployment secrets as `MISTRAL_API_KEY`. Never commit it or expose it in frontend code.

- Configuration status: `GET /api/v1/integrations/providers/mistral/status`
- Live key verification: `POST /api/v1/integrations/providers/mistral/verify`

The verifier makes an authenticated request to `GET https://api.mistral.ai/v1/models`, uses a 15-second timeout, disables redirects, and does not persist or return the key.

## Service-family scope

| Family | API area | Purpose |
|---|---|---|
| Chat | `POST /v1/chat/completions` | Conversational inference |
| Models | `GET /v1/models` | List models available to the key |
| Embeddings | `POST /v1/embeddings` | Text embeddings |
| Agents | `/v1/agents` | Agent configuration/execution where supported |
| OCR | `POST /v1/ocr` | Document and image text extraction |
| Fine-tuning | `/v1/fine_tuning` | Fine-tuning job lifecycle |
| Batch | `/v1/batch` | Asynchronous batch processing |
| FIM completions | `POST /v1/fim/completions` | Fill-in-the-middle completions |
| Audio | `/v1/audio` | Audio capabilities where supported |

Each directory is a catalog/setup boundary, not a claim that every operation is implemented. Verify current endpoints, models, permissions, account entitlement, limits and pricing against official docs before enabling production workflows.

## Status semantics
- `NEEDS_CONFIGURATION`: server-side key is absent.
- `CONFIGURED_NOT_VERIFIED`: key is present, but no successful probe is recorded.
- `CONNECTED`: authenticated models-list request succeeded at verification time.

A successful probe verifies access to the models endpoint only; it does not certify all service families or customer-specific authorization.

Official docs: https://docs.mistral.ai/api/
