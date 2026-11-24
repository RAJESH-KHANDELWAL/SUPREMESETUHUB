# GLOBAL_AI_PROMPT_AND_CONTEXT_STORAGE_ECOSYSTEM

- **Folder:** `global_ai_prompt_and_context_storage_ecosystem/`
- **Category:** PROMPT_AND_CONTEXT
- **Group:** AI_PROMPT_AND_KNOWLEDGE
- **Provider:** GLOBAL AI
- **State:** Category foundation scaffold; external connection is not configured.

## Package contents
- `__init__.py` — package export
- `ecosystem_config.py` — runtime configuration
- `ecosystem_models.py` — category metadata model
- `ecosystem_service.py` — health and description contract
- `service.py` — category-specific adapter boundary
- `api/routes.py` — framework-neutral API handlers
- `models/record.py` — model export
- `schemas/manifest.schema.json` — manifest schema
- `tests/test_foundation.py` — offline tests
- `php/global_ai_prompt_and_context_storage_ecosystem.php` — PHP metadata reader

## Responsibility
Prompt templates, context packages, retrieval references and version history.

## Safety and integration boundary
This folder is a category namespace, not proof that any AI provider offers this exact service. Do not mark connected until authorized credentials, provider-specific live health checks and end-to-end tests pass. No inference, upload, download or delete operation is enabled by this scaffold. Never commit credentials or personal data.
