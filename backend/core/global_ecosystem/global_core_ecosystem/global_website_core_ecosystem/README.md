# GLOBAL WEBSITE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_website_core_ecosystem/`  
**Layer:** CORE

## Mission
A provider-neutral, read-only control plane for website provider identity, hosting/platform capability classification, domain taxonomy, policy boundaries, readiness contracts and dependency discovery.

## Canonical architecture
- `constants.py`: ecosystem identity, layer, canonical master-catalog reference and capabilities.
- `manager.py`: stable Python entry point and `get_manager()`.
- `manager.php`: thin PHP interoperability facade; no provider requests.
- `catalog.py`: assembled provider, product-family and domain catalog.
- `provider_catalog.py`: curated provider identity metadata.
- `product_catalog.py`: website hosting/platform capability families.
- `domain_catalog.py`: provider-neutral website taxonomy.
- `contracts.py`: tenant context, secret references, readiness and result contracts.
- `policy.py`: publishing, destructive-change, security and consent guardrails.
- `module_service.py`: reusable read-only service for provider namespaces.
- `domain_runtime.py`: shared runtime for metadata-only domain descriptions.
- `orchestrator.py`: provider/domain/product discovery, health and dependency metadata.
- `service.py`: public status and service interface.
- `test_global_website_core.py`: structural and behavior tests.

## Provider namespaces
AWS, Google, Microsoft and ViceTemple are the four provider/platform namespaces already represented by the existing directory layout. Their registration is catalog metadata only. It does not establish account ownership, subscription, entitlement, credentials, region support, API access, website ownership or a live connection.

## Domain coverage
Website governance; domain registration; DNS; shared, cloud, managed and static hosting; website builders; CMS and headless CMS; web servers and runtimes; deployment and CI/CD; TLS/HTTPS; WAF/DDoS; identity/access/secrets; CDN/edge; caching and optimization; availability, backup and recovery; SEO/indexing; analytics/tagging; accessibility/compliance; commerce classification; integrations inventory; migration; multi-site and multi-tenancy.

The taxonomy is shared metadata, not a claim that each domain has a separately deployed service. No folder is generated for every taxonomy term.

## Master catalog alignment
The read-only source is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. The verified canonical topic represented here is `S09_websites` (Technology & Digital Ecosystem → Websites). This package does not edit the master catalog, duplicate its topic list, inflate the 2,468 target, or count catalog topics as implemented features.

## Layer ownership
| Layer | Responsibility |
|---|---|
| WEBSITE CORE | Provider identity, catalogs, taxonomy, contracts, policy and readiness metadata |
| WEBSITE API | HTTP clients, OAuth, provider SDKs, API routes and request/response transport |
| WEBSITE ENGINE | Provisioning/deployment jobs, queues, retries, scheduling and execution |
| WEBSITE DATABASE | Schemas, queries, migrations and transactions |
| WEBSITE STORAGE | Durable site assets, media, backups and retention |
| WEBSITE APPLICATION | Site builder UI, dashboards, user sessions and publishing workflows |

CORE does not perform domain purchases, DNS changes, deployment, publishing, payment processing, API transport, remote provisioning or durable persistence.

## Security and operational boundaries
- Never place tokens, API keys, passwords, client secrets or private keys in this package.
- Store credentials only in an external secret manager; metadata may carry secret references, never secret values.
- Production, publishing, domain-transfer and destructive actions require explicit authorization and audit in their owning execution layer.
- Tracking and analytics require consent-aware configuration in the owning application/API layers.
- Catalog presence is not proof of integration, entitlement, availability or live connectivity.
- Remote operations remain disabled; API calls performed by this package are zero.

## Validation
Run the repository-configured Python test suite and CI checks. Validate import paths, uniqueness, domain-family references, provider metadata boundaries and PHP syntax before production readiness is claimed.
