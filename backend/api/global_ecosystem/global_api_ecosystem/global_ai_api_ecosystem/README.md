# GLOBAL AI API ECOSYSTEM

This is the AI-focused child view of GLOBAL API ECOSYSTEM. It groups AI-provider APIs while keeping the central runtime registry distinct from the wider provider catalog.

## Current runtime registry
The central AI engine is implemented in `backend/engines/ai/manager.py`. Its registered runtime providers are currently returned separately by `GET /api/v1/global-ai-ecosystem/providers`. Runtime registration is not itself proof that a live API call will succeed; provider credentials, quotas, model availability and API tests still matter.

## Provider catalog
The shared catalog is `backend/api/global_api_ecosystem_catalog.py`. Its AI-family view includes Google, Microsoft, AWS, OpenAI, NSFWInfra, Anthropic, Meta, NVIDIA, Hugging Face, DeepSeek, Mistral, Cohere, Oracle and IBM. Some entries are catalog-only and do not yet have provider-specific adapters.

## API endpoints
- `GET /api/v1/global-ai-ecosystem/status`
- `GET /api/v1/global-ai-ecosystem/capabilities`
- `GET /api/v1/global-ai-ecosystem/providers`
- `GET /api/v1/global-ai-ecosystem/api-ecosystems`

Provider-specific implementations should be added to the appropriate provider/family package, with least-privilege credentials, secure durable token storage, user consent where required, safe error handling and automated tests. Catalog entries do not imply live connections.
