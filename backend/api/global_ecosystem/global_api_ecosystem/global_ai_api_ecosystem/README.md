# GLOBAL AI API ECOSYSTEM

This is the AI category inside `backend/api/global_ecosystem/global_api_ecosystem/`.
It is kept separate from CORE and ENGINE.

## Included
- AI provider catalogue and canonical links to existing provider ecosystems.
- Capability taxonomy for text, image, audio, video, embeddings, code, agents and safety.
- Service, tool and integration contracts.
- FastAPI read-only catalogue routes.
- Explicit connection and runtime status.

## Routes
- `GET /ai/status`
- `GET /ai/providers`
- `GET /ai/providers/{provider_id}`
- `GET /ai/search?q=...`
- `GET /ai/capabilities`
- `GET /ai/models`
- `GET /ai/architecture`
- `GET /ai/services`
- `GET /ai/tools`
- `GET /ai/integrations`

## Honest implementation status
This commit establishes catalogue data and contracts only. Provider credentials,
SDK adapters, live model discovery, inference execution and external connections
are not configured. Providers remain `NOT_CONFIGURED`; runtime execution is
disabled. Do not place API keys in source files.

## Boundaries
Do not duplicate CORE or ENGINE logic here. Provider-specific clients belong in
future adapter modules behind normalized contracts. Adjacent adult-industry,
payment, advertising and creator-platform directories are not automatically AI
providers merely because they have an AI-named folder.
