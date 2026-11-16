# COHERE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/`

## Mission

Cohere CORE is the provider-level control plane for Cohere capability identity, registration, contracts, validation, policy metadata, lifecycle and readiness. Its layout follows the same provider-root and product-package pattern used by Google CORE, adapted to Cohere's five registered capabilities.

## Coverage model

The current CORE inventory contains five capability packages:
- `cohere_classify_core_ecosystem`
- `cohere_command_core_ecosystem`
- `cohere_embed_core_ecosystem`
- `cohere_rerank_core_ecosystem`
- `cohere_tokenize_core_ecosystem`

These are capability packages, not a claim of five live product integrations. Each package follows the Google product-Core subfolder standard: `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, and `tests/`, plus its manifest, config, contracts and service entry point.

## Provider-level structure

The root owns provider inventory and discovery:
- `catalog.py`, `product_catalog.py`, `product_ecosystem_index.json`: canonical capability inventory and routing.
- `domain_catalog.py`: Cohere capability domain taxonomy.
- `contracts.py`, `policy.py`, `policies.py`: shared contracts and policy boundary.
- `module_service.py`, `orchestrator.py`, `service.py`, `manager.py`: provider-level discovery, capability-specific validation dispatch and public facade.
- `php/`: PHP interoperability contract.
- `cohere_shared_*/`: provider-wide shared compatibility, configuration, contracts, documentation, events, exceptions, orchestration, security, testing, utilities and validation.

## Layer ownership

| Layer | Owns |
|---|---|
| Cohere CORE | Capability identity, contracts, validation, policy metadata, lifecycle and readiness |
| Cohere API Ecosystem | HTTP transport, SDK clients, provider response normalization |
| Cohere ENGINE | Provider SDK execution, retries, timeouts, queues and scheduling |
| Cohere DATABASE | Structured persistence, schemas, queries and transactions |
| Cohere STORAGE | Files, artifacts, retention and backups |
| Application/UI | User sessions, consent and product workflows |

CORE must not duplicate API transport, token exchange, SDK execution, persistence, queue execution or UI.

## Security and readiness

- No provider secrets belong in Git or CORE request metadata.
- Credentials are referenced through a secure runtime/secret manager and injected by an approved API/ENGINE integration.
- Catalog registration does not prove account entitlement, model availability, API access or authorization.
- Destructive, administrative, billing and provider-write operations require explicit authorization and audit.
- Live status remains disabled until approved API/ENGINE adapters, secure credentials, model configuration, integration tests and provider smoke tests succeed.

## Current implementation boundary

**Status:** `interface_only`  
**Live Cohere calls:** disabled.

The repository contains capability contracts, validation foundations, manifests, package services, provider-level discovery metadata and a provider facade that dispatches to capability-specific validators. The provider network adapter, live execution, persistence and production authentication are separate integration work.
