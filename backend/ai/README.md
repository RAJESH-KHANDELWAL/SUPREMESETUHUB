# AI DOMAIN LAYER

The AI domain layer defines provider-neutral AI contracts, capability vocabulary, and domain-facing interfaces for SUPREMESETUHUB.

## Ownership

- `backend/ai/`: AI domain contracts, capability definitions, policies, prompts, and service-facing abstractions.
- `backend/engine/ai/`: execution engine, provider registration, dispatch, retries, and runtime orchestration.
- `backend/api/`: HTTP routes, request validation, and response serialization.
- `backend/core/`: shared business rules and application-independent domain services.
- `backend/global_ecosystem/global_ai_ecosystem/`: global AI category catalog.
- `backend/global_ecosystem/<provider>_ecosystem/`: provider ecosystem metadata.

## Boundaries

This package must not contain HTTP routes, database adapters, provider credentials, provider SDK clients, or duplicate the AI engine. Provider execution remains in the engine layer. Secrets must be read only by approved runtime adapters and never returned in public metadata.

## Current runtime

The existing runtime dispatcher is `backend/engine/ai/manager.py` (`AIEngine`). This domain package supplies stable, provider-neutral types; it does not claim that every listed capability or provider is already connected.

## Initial package

- `capabilities.py`: canonical capability identifiers.
- `contracts.py`: typed request and result contracts.
