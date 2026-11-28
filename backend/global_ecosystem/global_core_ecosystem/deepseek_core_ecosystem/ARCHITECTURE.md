# DeepSeek Core Architecture

## Control-plane flow

1. `catalog.py` declares the provider and four capability packages.
2. `manager.py` exposes the stable consumer-facing interface.
3. `orchestrator.py` provides discovery, health and dependency metadata.
4. `service.py` dispatches payloads to capability-specific validators.
5. Each capability package validates its own request shape and rejects secret-like fields.
6. `policy.py` blocks operations that must be authorized by a higher layer.

## Capability packages

- `deepseek_chat_completions_core_ecosystem`
- `deepseek_responses_core_ecosystem`
- `deepseek_search_core_ecosystem`
- `deepseek_fetch_core_ecosystem`

Each package owns its capability contract, service facade, manifest and package documentation. Existing capability packages are preserved; this alignment does not generate duplicate product implementations.

## Shared packages

Shared package names follow the provider naming convention and end in `_core_ecosystem`. They contain reusable cross-capability concerns only. Capability-specific validation remains in the relevant capability package.

## Boundaries

- API transport, OAuth/credential resolution and provider SDK clients belong to the DeepSeek API layer.
- Retries, queues, timeouts and scheduled execution belong to ENGINE.
- Persistence and durable artifacts belong to DATABASE/STORAGE.
- Core does not make network calls or claim live connectivity.
