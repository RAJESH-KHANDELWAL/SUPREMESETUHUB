# OPENAI CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/openai_core_ecosystem/`

## Mission

OpenAI Core is the provider-level control plane for OpenAI product identity, product-family registration, domain classification, capability metadata, tenant context, policy boundaries, lifecycle, dependency discovery and readiness.

## Product coverage

The canonical Core catalog contains the 14 named product/service families already represented by the OpenAI API product catalog: ChatGPT and its workspace editions, Codex, Dots, Agents API, Agents SDK, Apps SDK, ChatKit, SDK libraries, Plugins/MCP and the retired Sora reference. API capability families are kept separate from user-facing products.

## Main files

- `catalog.py`: provider identity and the 14 curated product-family records.
- `product_catalog.py`: product inventory and separate API capability inventory.
- `domain_catalog.py`: 11 meaningful cross-product Core domains.
- `domain_runtime.py`: shared read-only domain manager.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: capability classification, tenant-context validation and metadata sanitization.
- `module_service.py`: shared service used by each product package.
- `orchestrator.py`: product/domain discovery, health and dependency metadata.
- `service.py`: provider status and Global Core registry integration.
- `manager.py`: canonical Python entry point.
- `manager.php`: PHP interoperability facade; it does not call OpenAI APIs.
- `openai_php_core_ecosystem/`: PHP result contracts.
- `test_openai_core.py`: structural, behavior, policy and registry tests.
- `openai_*_core_ecosystem/`: product packages and domain packages.

## Master catalog alignment

This Core references the existing `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` master catalog. Relevant existing entries are Artificial Intelligence, Machine Learning, Software, Cloud Computing, Data Analytics and Cybersecurity. The master catalog is read-only here: no entries are manufactured to reach its 2,468-entry target. Its current catalog count remains whatever the source file reports.

## Layer boundaries

| Layer | Responsibility |
|---|---|
| OpenAI Core | Product identity, catalog, domains, capabilities, policy and readiness |
| OpenAI API Ecosystem | API routes, request validation, SDK/HTTP transport and response normalization |
| OpenAI Runtime/Global AI | Provider runtime and model-provider registry |
| OpenAI Storage/Database | Tenant-isolated durable records, secret references and migrations |
| OpenAI Engine | Execution, retries, scheduling and job orchestration |
| Application/UI | User sessions, consent, API-key entry, billing and user workflows |

Core does not import API clients, exchange tokens, read API keys, persist credentials, perform inference, execute tools or make network requests. The existing Global AI OpenAI compatibility facade remains a separate thin alias; it is not a second product catalog.

## Security and status

- Tenant and actor identity must come from the authenticated application layer.
- API keys and tokens must never appear in Core catalog records, logs or responses.
- Secret references are opaque; secret bytes belong in an external tenant-scoped secret store.
- Product presence and registered capabilities do not prove account entitlement, API access, billing, authorization or live connectivity.
- ChatGPT subscriptions and OpenAI API billing are separate.
- ChatGPT Health is a product surface, not a medical diagnosis API.
- Sora remains a retired historical reference and is not an active integration.
- Every product reports live connectivity as unverified until deployment-level credential checks and provider smoke tests pass.
