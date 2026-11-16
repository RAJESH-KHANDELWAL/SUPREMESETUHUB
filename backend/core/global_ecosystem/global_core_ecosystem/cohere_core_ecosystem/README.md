# Cohere CORE Ecosystem

Provider-neutral orchestration and policy boundary for Cohere capabilities.

## Product modules
- `cohere_classify_core_ecosystem`: classification requests and response normalization.
- `cohere_command_core_ecosystem`: command/chat generation request contracts.
- `cohere_embed_core_ecosystem`: text embedding contracts and vector validation.
- `cohere_rerank_core_ecosystem`: relevance reranking contracts.
- `cohere_tokenize_core_ecosystem`: tokenization/counting contracts.

## Shared CORE
`contracts.py`, `service.py`, `manager.py`, `policies.py`, `capabilities/`, `models/`, `schemas/`, `security/`, `lifecycle/`, `events/`, `services/`, `authentication/`, `tests/`, and `php/`.

## Layer boundaries
CORE owns domain contracts, validation, safe orchestration and capability metadata. API owns HTTP transport. ENGINE owns execution, retries and provider SDK calls. DATABASE/STORAGE own persistence. Authentication credentials and secrets must be injected by a secure runtime; never commit keys.

## Status
The modules define interfaces and validation only. Live Cohere calls remain disabled until the ENGINE adapter, credentials, approved model configuration and integration tests are supplied.
