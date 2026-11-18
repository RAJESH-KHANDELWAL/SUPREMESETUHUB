# GLOBAL AI CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-AI-CORE-ECOSYSTEM`  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/`

## Mission

Global AI Core is the provider-level control plane and canonical product Core inventory for the Bharat-to-global AI ecosystem. It owns provider identity, canonical registration, domain classification, capability metadata, Core policy metadata, lifecycle/readiness reporting and orchestration.

The runtime provider registry remains the single source of truth:
`backend/global_ecosystem/global_ai_ecosystem/providers.py`.

Each canonical runtime registry entry maps to exactly one dedicated:
`<provider_id>_core_ecosystem/` package.

## Coverage model

The inspected runtime registry contains **68 canonical provider entries**. The ecosystem defines **19 AI domains**. The product index separately records **17 legacy API aliases** and **24 adjacent integration aliases**; these compatibility entries are not additional canonical AI providers.

The canonical provider inventory includes hosted model providers, open model families, agent frameworks, inference infrastructure and enterprise AI platforms. Their original runtime classifications must be preserved. Registration does not imply an available public API, entitlement, authenticated account, provider authorization or live integration.

## Canonical ten-folder product standard

Every canonical product Core package follows the Google Core ten-folder convention:

1. `authentication/` — authentication-context contract references only; credentials and token exchange remain outside Core.
2. `capabilities/` — declared capability metadata and policy classification.
3. `docs/` — provider-specific architecture and implementation documentation.
4. `events/` — lifecycle and domain event contracts.
5. `lifecycle/` — registration, readiness and lifecycle metadata.
6. `models/` — model/service metadata, not model execution.
7. `schemas/` — provider-specific metadata schemas and validation contracts.
8. `security/` — security policy metadata and safe handling rules.
9. `services/` — read-only provider Core facade and service contracts.
10. `tests/` — provider package and contract tests.

Do not create a second provider identity for an alias. Resolve aliases to the canonical provider ID and preserve legacy import paths only where compatibility requires them.

## Core domains

The taxonomy contains 19 domains:

- Bharat Indic and Regional AI
- Global Foundation Models
- Open Model Families
- Agent Frameworks and Orchestration
- Enterprise and Business AI
- Inference and AI Infrastructure
- Generative Media and Creative AI
- Speech, Audio and Language AI
- Video and Media Generation
- Search, Knowledge and Retrieval
- Developer and Code AI
- Safety, Governance and Evaluation
- AI Research and Evaluation
- On-device and Edge AI
- Multimodal and Spatial AI
- Healthcare and Life Sciences AI
- Finance and Risk AI
- Education and Learning AI
- Specialty and Cross-product AI

Provider-to-domain assignment is metadata classification, not a claim that every provider offers every capability in that domain. Unclassified entries must remain visible in the specialty domain until reviewed.

## Layer ownership

| Layer | Owns |
|---|---|
| Global AI Core | Canonical provider identity, registry mapping, domain classification, capability metadata, Core policy, lifecycle, readiness and orchestration |
| Global AI API | Provider authentication, OAuth where applicable, secret resolution, SDK clients, HTTP transport, retries and response normalization |
| Global AI Engine | Model inference, agent execution, tool execution, routing and runtime execution |
| Global AI Database | Structured records, schemas, queries, migrations and transactions |
| Global AI Storage | Durable artifacts, tenant isolation, retention and backups |
| Application/UI | User sessions, consent, user workflows and presentation |

Core must not duplicate API transport, token exchange, secret storage, inference execution, tool execution, persistence or user-interface workflows.

## Python implementation

- `catalog.py`: canonical provider lookup, legacy alias resolution and registry validation.
- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `policy.py`: tenant-context checks, capability metadata policy and recursive secret-field filtering. It is not application authorization or provider authorization.
- `request_contracts.py`: strict provider-neutral task payload validation and secret-material rejection.
- `module_service.py`: shared read-only product Core service.
- `provider_service.py`: compatibility facade for legacy API aliases.
- `product_catalog.py`: unified provider offering inventory.
- `domain_catalog.py`: 19-domain taxonomy and provider coverage.
- `orchestrator.py`: provider/domain discovery, inventory, health and dependency map.
- `ecosystem_service.py`: manager registration and ecosystem status.
- `service.py`: executor-injected task boundary; execution remains delegated to the application/Engine.

## PHP interoperability

`php/GlobalAICoreContract.php` validates and normalizes PHP 8+ JSON result contracts. It performs no network I/O and does not duplicate provider authentication, API clients or inference execution.

## Security and lifecycle rules

- Tenant and actor identity must originate from the authenticated application layer.
- A Core policy pass is not proof of application authorization, provider authorization, OAuth consent, entitlement or API availability.
- Secret values, access tokens, refresh tokens, API keys and private keys must never be committed or exposed in Core status payloads.
- Store opaque secret references only; resolve secret material in the API/security boundary.
- Destructive, administrative, publishing, billing, training and tool-execution capabilities require explicit authorization and audit.
- A provider marked `live` in registry metadata is not considered connection-verified by Core.
- Report a live connection only after deployment-level authentication and provider smoke tests succeed.
- Catalog health must report zero live connections and zero API calls unless verified runtime evidence is supplied by the owning integration layer.

## Verification requirements

Before declaring this ecosystem production-ready, CI must verify:

1. Runtime registry IDs are unique and every canonical entry has exactly one Core package.
2. Every canonical package contains the ten required folders.
3. The product index, runtime registry and package inventory agree.
4. Every alias resolves to a canonical provider or is explicitly marked compatibility-only.
5. Domain totals reconcile to the canonical provider total and specialty assignments remain visible.
6. Python imports, contract tests and PHP syntax/contract tests pass.
7. No credentials or secret material appear in tracked files or status responses.

A successful catalog check does not establish a live provider connection.
