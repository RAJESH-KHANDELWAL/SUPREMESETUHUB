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


## Provider ownership vs AI category (clarified)

This directory is the shared **AI category ecosystem**; it is not the provider-owned folder for every AI company. Each vendor has its own catalog at the sibling provider path, for example:

- Google: `global_google_api_ecosystem/`
- AWS: `global_aws_api_ecosystem/`
- Microsoft: `global_microsoft_api_ecosystem/`
- Apple: `global_apple_api_ecosystem/`
- OpenAI: `global_openai_api_ecosystem/`
- Anthropic: `global_anthropic_api_ecosystem/`
- NVIDIA: `global_nvidia_api_ecosystem/`
- Hugging Face: `global_huggingface_api_ecosystem/`

Provider-specific capabilities must also be indexed under the appropriate shared category when relevant. For example, a Google database capability belongs in both the Google provider catalog and the shared `global_database_api_ecosystem/google_database_api_ecosystem/` category subfolder. Google storage maps to `global_storage_api_ecosystem/google_storage_api_ecosystem/`; Google compute/cloud maps to the respective shared cloud/server categories. Apply the same routing convention to AWS, Microsoft, Apple, and all other providers based on their actual product/API offerings.

These paths are catalog/routing boundaries. They do not by themselves implement an adapter or prove live authentication, API calls, or deployment.


## AI provider sub-ecosystems (actual folders)

The AI category now contains provider-specific subfolders for the AI providers listed below. Each subfolder contains a README and a Python metadata module. These are category-routing/catalog files, not claims of live provider connections.

- `google_ai_api_ecosystem/`
- `aws_ai_api_ecosystem/`
- `microsoft_ai_api_ecosystem/`
- `apple_ai_api_ecosystem/`
- `openai_ai_api_ecosystem/`
- `nsfwinfra_ai_api_ecosystem/`
- `anthropic_ai_api_ecosystem/`
- `meta_ai_api_ecosystem/`
- `nvidia_ai_api_ecosystem/`
- `huggingface_ai_api_ecosystem/`
- `deepseek_ai_api_ecosystem/`
- `mistral_ai_api_ecosystem/`
- `cohere_ai_api_ecosystem/`
- `oracle_ai_api_ecosystem/`
- `ibm_ai_api_ecosystem/`

Each provider's broader catalog remains in its sibling `global_<provider>_api_ecosystem/` folder. This AI category subfolder is the AI-specific view; the provider-owned folder remains the full provider view. Shared cross-provider APIs and endpoints remain in the parent category implementation. Live connectivity still requires a working adapter, valid credentials and tests.
