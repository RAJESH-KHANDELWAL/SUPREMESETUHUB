# MISTRAL CHAT COMPLETIONS API ECOSYSTEM

Provider: Mistral AI  
Family: Chat Completions  
API area: `POST /v1/chat/completions`

## Purpose
Conversational and text-generation requests.

## Setup
Configure `MISTRAL_API_KEY` in backend deployment secrets. Never put credentials in source code or frontend configuration. Shared adapter: `backend/integrations/providers/mistral.py`.

## Implementation boundary
This directory is a service-family catalog and setup boundary. It does not claim all operations are implemented. Confirm current official endpoint, model, schema, account entitlement, limits and pricing before enabling production use.

The shared live verifier checks authenticated access to `GET https://api.mistral.ai/v1/models` only. It does not verify this service family.

Official documentation: https://docs.mistral.ai/api/
