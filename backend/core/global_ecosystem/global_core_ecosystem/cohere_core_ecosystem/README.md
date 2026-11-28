# COHERE CORE ECOSYSTEM

Provider: Cohere  
Parent: GLOBAL CORE ECOSYSTEM  
Root: `backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/`  
API catalog: `backend/api/global_ecosystem/global_api_ecosystem/cohere_api_ecosystem/`  
Engine: `backend/engine/global_ecosystem/global_engine_ecosystem/cohere_engine_ecosystem/`

## Mission

Cohere Core is the provider-owned, metadata-first control plane for capability identity, canonical registration, domain classification, request/result contracts, tenant boundaries, policy, lifecycle, readiness and discovery. It follows the Google Core provider-root architecture while preserving Cohere's five actual capability families and four domain groups.

## Canonical provider architecture

- `catalog.py`: canonical provider and five-capability registry.
- `contracts.py`: tenant context, opaque secret references, request/result and readiness contracts.
- `policy.py`: capability validation, operation guardrails and safe metadata summaries.
- `module_service.py`: reusable read-only capability metadata service.
- `product_catalog.py`: five capability offering inventory.
- `domain_catalog.py`: four Cohere-specific capability domains and assignment.
- `domain_runtime.py`: read-only domain manager and domain entry point.
- `orchestrator.py`: capability discovery, domain inventory, health and dependency mapping.
- `manager.py`: canonical `CohereCoreManager` and `get_manager()`.
- `service.py`: provider validation and authorization facade.
- `manager.php` and `php/`: PHP interoperability contract.
- `ecosystem_manifest.json` and `product_ecosystem_index.json`: machine-readable provider and capability maps.
- `tests/`: provider-wide Google Core alignment and regression tests.

## Capability packages

Exactly five capability packages are registered:

| Capability | Package | Domain |
|---|---|---|
| Classify | `cohere_classify_core_ecosystem` | Language Understanding |
| Command | `cohere_command_core_ecosystem` | Text Generation |
| Embed | `cohere_embed_core_ecosystem` | Vector Representation |
| Rerank | `cohere_rerank_core_ecosystem` | Language Understanding |
| Tokenize | `cohere_tokenize_core_ecosystem` | Text Processing |

Each capability package owns its typed request contract, validation service, non-secret configuration, manifest, documentation and ten standard Google-style subfolders. Capability packages delegate to their own validators; provider-wide routing does not duplicate their implementation.

## Domain packages

The four domain groups are Language Understanding, Text Generation, Vector Representation and Text Processing. The root `domain_runtime.py` provides a read-only manager for each registered domain. Domain classification is metadata and does not establish model availability or API entitlement.

## Shared support areas

The existing Cohere shared support modules provide compatibility, configuration, contracts, documentation, events, exceptions, orchestration, security, testing, utilities and validation. Their current directory names are `cohere_shared_<area>`; the provider-specific shared-directory suffix normalization is a remaining structural naming task and is not represented as completed here.

## Layer boundaries

| Layer | Responsibility |
|---|---|
| Cohere Core | Provider/capability identity, contracts, policy, lifecycle, readiness and discovery |
| Cohere API Ecosystem | HTTP transport, SDK clients, authentication adapters and response normalization |
| Cohere Engine | SDK execution, retries, timeouts, queues and scheduling |
| Database / Storage | Persistence, schemas, artifacts, retention and backups |
| Application / UI | User sessions, tenant authorization, consent and workflows |

Core performs no Cohere network calls, token exchange, SDK execution, persistence, queue execution or user workflow operations.

## Security and readiness

No provider secrets or tokens belong in Git or Core metadata. Credentials are opaque references resolved only by an approved runtime secret manager. Tenant and actor identity must originate from the authenticated application layer. Sensitive operations require explicit authorization and audit in the approved API/Engine workflow. Capability registration is not authorization, entitlement or proof of model availability.

All five capabilities remain `CORE_CONTRACT_ONLY`; live provider calls are disabled, live connections verified: 0, API calls performed by Core: 0. These are control-plane facts only, not production connectivity claims.
