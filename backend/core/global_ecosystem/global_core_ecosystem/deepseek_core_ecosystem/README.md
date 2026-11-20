# DEEPSEEK CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/deepseek_core_ecosystem/`

## Mission

DeepSeek Core is the provider-level control plane for the registered DeepSeek capabilities: chat completions, responses, search and fetch. It owns provider identity, capability registration, request contracts, policy metadata, readiness and orchestration metadata.

## Canonical structure

- `manager.py`: stable Python entry point for status, discovery, health and request-contract validation.
- `manager.php`: thin PHP interoperability facade over the language-neutral result contract.
- `catalog.py`: canonical provider identity and capability registry.
- `contracts.py`: provider-level result and request context contracts.
- `service.py`: capability-specific request validation; no provider transport.
- `orchestrator.py`: discovery, health and dependency metadata.
- `policy.py`: metadata and operation guardrails.
- `deepseek_*_core_ecosystem/`: four capability-specific Core packages.
- `deepseek_shared_*_core_ecosystem/`: shared contracts, security and supporting concerns.
- `test_deepseek_core_domains.py` and `tests/`: structural and behavior tests.
- `ecosystem_manifest.json` and `product_ecosystem_index.json`: machine-readable registry metadata.

## Capability inventory

| Capability | Core package | Responsibility |
|---|---|---|
| Chat completions | `deepseek_chat_completions_core_ecosystem` | Chat request contract |
| Responses | `deepseek_responses_core_ecosystem` | Responses request contract |
| Search | `deepseek_search_core_ecosystem` | Search request contract |
| Fetch | `deepseek_fetch_core_ecosystem` | Fetch request contract |

## Layer ownership

| Layer | Owns |
|---|---|
| DeepSeek Core | Provider identity, capability metadata, contracts, policy and readiness |
| DeepSeek API Ecosystem | HTTP transport, API versioning, response normalization and provider adapter |
| DeepSeek Engine | SDK execution, retries, timeouts, queues and scheduling |
| Database / Storage | Durable records, tenant isolation, retention and artifacts |
| Application | Authenticated user context, consent and user-facing workflows |

Core validates metadata and request shape only. It must not resolve credentials, exchange tokens, make network requests, retry, persist data, or execute provider operations.

## Security and readiness rules

1. Secret material must never be accepted in Core request payloads or committed to the repository.
2. Tenant and actor identity must be supplied by the authenticated application layer.
3. Capability registration is not authorization, entitlement, API availability or live connectivity.
4. Administrative, destructive and billing operations require explicit authorization in the appropriate API/application layer.
5. A live connection may be reported only after deployment authentication and provider smoke tests succeed.

**Current state:** interface and request-contract validation only. Live provider calls are disabled and no live connection is verified.
