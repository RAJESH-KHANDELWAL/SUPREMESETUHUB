# GLOBAL AI CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-AI-CORE-ECOSYSTEM`  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/`

## Mission

Global AI Core is the canonical provider-level control plane and product inventory for the Bharat-to-global AI ecosystem. It owns provider identity mapping, domain classification, capability metadata, tenant context contracts, Core policy metadata, lifecycle/readiness reporting, discovery and dependency mapping.

The runtime provider registry remains the single source of truth:
`backend/global_ecosystem/global_ai_ecosystem/providers.py`.

Each canonical runtime registry entry maps to exactly one `<provider_id>_core_ecosystem/` package. Compatibility aliases resolve to canonical IDs and do not create duplicate provider identities.

## Google Core-aligned public structure

- `manager.py`: canonical `GlobalAICoreManager`, `get_manager()`, and read-only master-catalog inventory access.
- `manager.php`: PHP interoperability facade with matching read-only master-catalog access.
- `domain_runtime.py`: shared read-only manager for the 19 AI domains.
- `catalog.py`: canonical provider lookup, alias resolution and registry validation.
- `product_catalog.py`: unified provider offering inventory.
- `domain_catalog.py`: 19-domain taxonomy and provider coverage.
- `contracts.py`: tenant context, opaque secret reference, readiness and result contracts.
- `policy.py`: capability metadata guardrails and recursive secret-field filtering.
- `request_contracts.py`: strict provider-neutral task payload validation and secret-material rejection.
- `module_service.py`: reusable read-only service for provider Core packages.
- `orchestrator.py`: provider/domain discovery, health, offerings and dependency mapping.
- `ecosystem_service.py`: global registry registration/status and registered-module discovery.
- `service.py`: executor-injected task boundary; execution remains delegated to the application/ENGINE.
- `php/GlobalAICoreContract.php`: PHP 8+ result-contract validation and sanitization.
- `test_global_ai_core_domains.py`: provider, domain, catalog coverage and manager contract tests.
- `<provider_id>_core_ecosystem/`: existing provider-specific Core packages.

Provider packages keep the ten Google Core folders: `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/` and `tests/`. Do not create duplicate managers or unnecessary nested folders in every provider package.

## Coverage model

The canonical runtime inventory is verified by CI and currently contains at least 68 provider entries. The ecosystem defines 19 AI domains. The product index separately records 17 legacy API aliases and 24 adjacent integration aliases; these compatibility entries are not additional canonical AI providers.

The inventory includes hosted model providers, open model families, agent frameworks, inference infrastructure and enterprise AI platforms. Their original runtime classifications must be preserved. Registration does not imply a public API, entitlement, authenticated account, provider authorization or live integration.

## Complete master Bharat-to-Supreme catalog coverage

The single source of truth remains:
`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`.

Global AI Core now exposes the existing catalog through `master_catalog_inventory()` and `get_master_catalog_entry(entry_id)` in Python, with matching `masterCatalogInventory()` and `getMasterCatalogEntry()` PHP methods. The bridge is read-only and loads the source file on demand; it does not copy the catalog into another file, move ownership, create provider records, or generate placeholder entries.

The last verified source snapshot contains:

| Catalog measure | Count |
|---|---:|
| Target unique entries | 2,468 |
| Current unique entries | 246 |
| Remaining unique entries | 2,222 |
| Numbered source rows | 248 |
| Cross-reference rows included in source rows | 2 |
| Master catalog sections | 13 |

The 246 unique entries consist of the catalog's non-cross-reference rows; the two cross-reference rows are also returned by default and retain their canonical entry IDs. The catalog's own count fields are checked whenever the inventory is loaded. If the source file is missing, malformed, or its counts do not reconcile, the bridge raises an explicit error instead of silently returning partial or fabricated data.

The master catalog is cross-ecosystem planning data, not an AI provider count. Global AI Core exposes all current source rows as a read-only planning inventory, while the AI provider registry remains separate and authoritative for provider operations. The 2,468 target is not treated as permission to create folders, files, dummy records or duplicate modules. Only meaningful, individually defined, non-duplicate entries may be added to the master catalog by its owning layer, `GLOBAL_ENGINE_ECOSYSTEM`.

## Core domains

The taxonomy contains 19 domains:

1. Bharat Indic and Regional AI
2. Global Foundation Models
3. Open Model Families
4. Agent Frameworks and Orchestration
5. Enterprise and Business AI
6. Inference and AI Infrastructure
7. Generative Media and Creative AI
8. Speech, Audio and Language AI
9. Video and Media Generation
10. Search, Knowledge and Retrieval
11. Developer and Code AI
12. Safety, Governance and Evaluation
13. AI Research and Evaluation
14. On-device and Edge AI
15. Multimodal and Spatial AI
16. Healthcare and Life Sciences AI
17. Finance and Risk AI
18. Education and Learning AI
19. Specialty and Cross-product AI

Provider-to-domain assignment is metadata classification, not a claim that every provider offers every capability in that domain. Unclassified entries remain visible in the specialty domain until reviewed.

## Layer ownership

| Layer | Owns |
|---|---|
| Global AI Core | Canonical provider identity, registry mapping, domain classification, capability metadata, Core policy, lifecycle, readiness, discovery and read-only master-catalog access |
| Global AI API | Provider authentication, OAuth, secret resolution, SDK clients, HTTP transport, retries and response normalization |
| Global AI Engine | Model inference, agent execution, tool execution, routing and runtime execution |
| Global AI Database | Structured records, schemas, queries, migrations and transactions |
| Global AI Storage | Durable artifacts, tenant isolation, retention and backups |
| Application/UI | User sessions, consent, user workflows and presentation |

Core must not duplicate API transport, token exchange, secret storage, inference execution, tool execution, persistence or user-interface workflows.

## Security and lifecycle rules

- Tenant and actor identity must originate from the authenticated application layer.
- A Core policy pass is not proof of application authorization, provider authorization, OAuth consent, entitlement or API availability.
- Secret values, access tokens, refresh tokens, API keys and private keys must never be committed or exposed in Core status payloads.
- Store opaque secret references only; resolve secret material in the API/security boundary.
- Destructive, administrative, publishing, billing, training and tool-execution capabilities require explicit authorization and audit.
- A provider marked `live` in registry metadata is not considered connection-verified by Core.
- Report a live connection only after deployment-level authentication and provider smoke tests succeed.
- Core health reports zero live connections and zero provider API calls.

A successful catalog check does not establish a live provider connection.
