# GOOGLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/`

## Mission

Google Core is the provider-level control plane and canonical capability inventory for Google products and services. It coordinates provider identity, product registration, domain classification, capability metadata, tenant context, policy boundaries, discovery, dependency mapping and readiness.

## Structure

- `manager.py`: canonical Python entry point for status, product/domain discovery, offering inventory and dependency metadata.
- `manager.php`: thin PHP interoperability facade over the shared result contract.
- `catalog.py`: provider identity and the curated product-family registry.
- `product_catalog.py`: registered Google runtime offerings and their routing metadata.
- `domain_catalog.py`: cross-product domain taxonomy and coverage summary.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: Core metadata and capability guardrails.
- `module_service.py`: reusable read-only service for individual product Core packages.
- `orchestrator.py`: product/domain discovery, health and dependency metadata.
- `service.py`: public ecosystem status and global registry integration.
- `php/GoogleCoreContract.php`: PHP 8+ result-contract validation and sanitization.
- `php/GoogleCoreDomainContract.php`: PHP 8+ domain-result contract validation and sanitization.
- `domain_runtime.py`: shared read-only implementation used by all 19 domain managers.
- `test_google_core_domains.py`: structural and behavior tests for the 19 domain packages.
- `google_*_core_ecosystem/`: existing product-specific Core packages (130 product package directories at the time of this update).
- The 19 domain packages (`provider_governance/` through `specialty_services/`) group existing products by Core responsibility; they do not duplicate product implementations.

Product packages should contain only files required by that product's real Core responsibilities. Do not generate a fixed set of empty subfolders or duplicate shared managers in every product package.

## Coverage domains

1. Provider governance and product lifecycle
2. Identity, access and administration
3. Workspace and collaboration
4. Cloud infrastructure and networking
5. Storage, databases and data platforms
6. AI, machine learning and intelligence
7. Analytics and observability
8. Maps, geospatial and travel
9. Developer and application platform
10. Android and mobile
11. Security, privacy and compliance
12. Advertising, commerce and monetization
13. Search, publishing and discovery
14. Media, video and audio
15. Business, education and local services
16. Payments, wallet and subscriptions
17. Consumer devices and smart home
18. Language, accessibility and productivity
19. Specialty and cross-product services

## Layer ownership

| Layer | Owns |
|---|---|
| Google Core | Product identity, domain classification, capability metadata, lifecycle, policy and readiness |
| Google API Ecosystem | OAuth flows, Google SDK clients, API transport and response normalization |
| Google Storage Ecosystem | Durable records, tenant isolation, retention and backups |
| Google Database Ecosystem | Database engines, schemas, queries, migrations and transactions |
| Google Runtime/Engine | Jobs, retries, queues, scheduling and execution |
| Application/UI | User sessions, consent screens, user workflows and product UI |

Core must not duplicate API clients, token exchange, persistence, queue execution or product UI.

## Security and lifecycle rules

1. Tenant and actor identity must come from the authenticated application layer.
2. Registered capabilities do not prove caller authorization, OAuth consent, product entitlement or API availability.
3. Never commit or expose access tokens, refresh tokens, client secrets or private keys.
4. Use least-privilege scopes and explicit consent; use Cloud IAM/workload identity for Cloud workloads where appropriate.
5. Destructive, administrative, publishing, billing and write operations require explicit authorization and audit.
6. Products without a verified API adapter remain catalog-only or eligibility-gated.
7. Report a live connection only after deployment authentication and provider smoke tests succeed.

## Implementation boundary

This package provides catalog, taxonomy, policy metadata and orchestration. Catalog presence does not mean every Google product has a public API or that an account/project is connected. API credentials and live provider verification are not part of this Core package.
