# GLOBAL WEB CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_web_core_ecosystem/`  
**Layer:** CORE

## Mission
Provider-neutral, read-only control plane for web provider identity, product-family classification, domain taxonomy, capability metadata, policy boundaries, readiness contracts and dependency discovery.

## Shared architecture
- `constants.py`: canonical identity and capability declarations.
- `manager.py`: stable Python entry point and `get_manager()`.
- `manager.php`: thin PHP 8+ interoperability facade; no provider calls.
- `catalog.py`: assembled provider, product-family and domain catalog.
- `provider_catalog.py`: curated provider identity metadata.
- `product_catalog.py`: web capability/product-family taxonomy.
- `domain_catalog.py`: provider-neutral web domain taxonomy.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: capability and security guardrails.
- `module_service.py`: reusable read-only service for provider packages.
- `orchestrator.py`: provider/domain/product discovery, health and dependency metadata.
- `service.py`: public ecosystem status and service interface.
- `test_global_web_core.py`: structural and behavior tests.

## Provider namespaces
The initial registry contains AWS, Cloudflare, Google and Microsoft, matching the provider namespaces already present in this package. Registration is metadata only; it does not establish account ownership, subscription, entitlement, credentials, region support, API access or a live connection.

## Domain coverage
1. Web governance and lifecycle
2. Web infrastructure
3. Domains and DNS
4. Web hosting and deployment
5. Web servers and runtime
6. CDN and edge
7. Web protocols and standards
8. Web security and privacy
9. Web development
10. CMS and website platforms
11. Web applications
12. Search and indexing
13. Web analytics and observability
14. Web performance and reliability
15. Web storage and assets
16. Web API interoperability
17. Browser and client compatibility
18. Web accessibility and inclusion
19. Web identity and access
20. Web commerce and monetization
21. Web compliance and jurisdiction

These are shared taxonomy entries, not 21 automatically generated folders. A domain package is added only when it has an independent, testable CORE responsibility. Existing provider folders remain in place.

## Layer ownership
| Layer | Owns |
|---|---|
| WEB CORE | Provider identity, capability taxonomy, catalogs, metadata contracts, policy and readiness discovery |
| WEB API | HTTP clients, OAuth, API routes, request/response transport and provider adapters |
| WEB ENGINE | Execution, deployment jobs, retries, queues and scheduling |
| WEB DATABASE | Schemas, queries, migrations and transactions |
| WEB STORAGE | Durable files, media, backups and retention |
| WEB APPLICATION | Websites, dashboards, user sessions and application workflows |

CORE must not implement API transport, OAuth/token exchange, provider SDK execution, remote provisioning, durable persistence, billing or application UI.

## Security and operational boundaries
- Tenant and actor identity must come from the authenticated application/API layer.
- Never commit or return tokens, API keys, passwords, client secrets or private keys.
- Use least privilege and an external secret store.
- Destructive, administrative, publishing and billing actions require explicit authorization and audit.
- Catalog presence is not proof of an integration, entitlement or live connection.
- Remote operations remain disabled in CORE; API calls performed by this package remain zero.
- Live connectivity may be reported only after a separate authenticated deployment smoke test.

## Master catalog alignment
`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` remains the read-only master planning taxonomy. This package references it; it does not edit it, inflate the 2,468 target, or claim implementation coverage merely from a catalog entry. Add taxonomy references only when exact canonical entry IDs have been verified.

## Validation
Run the repository's configured Python test suite and CI checks. Validate imports, provider/domain uniqueness, metadata boundaries and PHP syntax before treating the package as production-ready.
