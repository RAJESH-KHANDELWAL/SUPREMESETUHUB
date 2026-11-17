# COHERE CORE ECOSYSTEM

Parent: GLOBAL CORE ECOSYSTEM  
Root: backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/  
Provider: Cohere  
Layer: CORE  
Status: interface_only

## Standards and status

- PRODUCT_ECOSYSTEM_STANDARD.md defines the five capability packages and ten-folder standard.
- COHERE_CORE_IMPLEMENTATION_STATUS.md records implementation boundaries and verification state.
- ARCHITECTURE.md and STRUCTURE_MAP.md define ownership and the canonical repository layout.

## Mission

Cohere CORE is the provider-level control plane for capability identity, canonical registration, domain classification, request contracts, validation, policy metadata, lifecycle, discovery and readiness. Its provider-root and capability-package layout follows the Google CORE product-package standard while retaining Cohere's own capability inventory.

## Canonical capability inventory

Exactly five Cohere capabilities are registered:

| Capability | Package | Domain |
|---|---|---|
| classify | cohere_classify_core_ecosystem | language_understanding |
| command | cohere_command_core_ecosystem | text_generation |
| embed | cohere_embed_core_ecosystem | vector_representation |
| rerank | cohere_rerank_core_ecosystem | language_understanding |
| tokenize | cohere_tokenize_core_ecosystem | text_processing |

These are CORE contract packages, not five claims of live integrations, model entitlements or API availability. The canonical source is catalog.py; product routing and JSON index are synchronized metadata.

## Provider-level structure

- catalog.py, product_catalog.py, product_ecosystem_index.json: provider and capability inventory.
- domain_catalog.py: canonical Cohere capability taxonomy and coverage.
- contracts.py and policy.py: shared request/result contracts and policy boundary.
- module_service.py, orchestrator.py, manager.py, service.py: discovery, readiness, provider facade and capability-specific validation dispatch.
- php/: provider-wide PHP contract.
- cohere_shared_*/: provider-wide compatibility, configuration, contracts, documentation, events, exceptions, orchestration, security, testing, utilities and validation.

## Capability package standard

Each capability package follows the Google product-Core package convention with ten subfolders: authentication/, capabilities/, docs/, events/, lifecycle/, models/, schemas/, security/, services/, and tests/. Each also owns typed contracts.py, service.py, non-secret ecosystem_config.py, ecosystem_manifest.json, README.md and __init__.py. The PHP caller-context contract lives in authentication/contract.php, matching the Google package convention.

## Layer ownership

| Layer | Owns |
|---|---|
| Cohere CORE | Capability identity, contracts, validation, policy metadata, lifecycle, discovery and readiness |
| Cohere API Ecosystem | HTTP transport, SDK clients, authentication adapters and provider response normalization |
| Cohere ENGINE | SDK execution, retries, timeouts, queues and scheduling |
| Cohere DATABASE | Structured persistence, schemas, queries and transactions |
| Cohere STORAGE | Files, artifacts, retention and backups |
| Application/UI | User sessions, consent and product workflows |

CORE must not duplicate API transport, token exchange, SDK execution, persistence, queue execution or UI.

## Security and readiness

- No provider secrets or tokens belong in Git or request metadata.
- Credentials are represented only by opaque references and resolved by an approved runtime secret manager.
- Tenant and actor identity must come from the authenticated application layer.
- Catalog registration does not prove account entitlement, model availability, API access or authorization.
- Sensitive operations require explicit authorization and audit in the approved API/ENGINE workflow.
- Live status remains disabled until approved adapters, secure credentials, model configuration, integration tests and provider smoke tests succeed.

## Current implementation boundary

Status: interface_only  
Live Cohere calls: disabled.

The provider facade dispatches to five capability-specific validators and returns normalized CORE validation results. The repository does not claim live Cohere execution, production authentication, persistence, or provider connectivity.
