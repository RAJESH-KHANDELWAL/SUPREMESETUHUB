# ATLASSIAN CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/`

## Mission
Provider-level control plane and canonical capability inventory for Atlassian product families. Owns product identity, family/domain classification, capability metadata, tenant context, policy boundaries, lifecycle/readiness metadata and cross-family discovery.

## Product-family coverage
- Atlassian Administration and Identity
- Bitbucket
- Confluence
- Jira
- Jira Service Management

The five families are grounded in the existing Atlassian API ecosystem directories in this repository. Family registration is metadata only and does not imply API authentication, product entitlement or live connectivity.

## Layer ownership
| Layer | Responsibility |
|---|---|
| Atlassian Core | Product identity, capability metadata, policy, lifecycle, discovery and readiness |
| Atlassian API Ecosystem | OAuth/API tokens, HTTP transport, SDKs, request/response normalization |
| Storage Ecosystem | Durable records, tenant isolation, retention and backups |
| Database Ecosystem | Schemas, queries, migrations and transactions |
| Runtime/Engine | Jobs, retries, queues and scheduling |
| Application/UI | User sessions, consent, workflows and product UI |

Core performs no Atlassian network calls, credential exchange, persistence, queue execution or user workflow operations.

## Implementation
- `catalog.py`: provider and five product-family records.
- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `policy.py`: safe metadata summaries and capability classification.
- `module_service.py`: reusable read-only product-family service.
- `product_catalog.py`: five family offering records and API references.
- `domain_catalog.py`: six-domain taxonomy and family assignment.
- `orchestrator.py`: discovery, health, inventory and dependency mapping.
- `service.py`: provider status facade.
- `php/AtlassianCoreContract.php`: PHP 8+ payload validation/normalization.

Each product-family package contains the ten standard Google-style subfolders with product-specific contracts, metadata and tests.

## Security and readiness
1. Tenant and actor identity must come from the authenticated application layer.
2. Capability metadata is not authorization; the API/application layers must enforce scopes, permissions and tenant access.
3. Store tokens and secrets only in an approved external secret manager; this Core package stores opaque references only.
4. Administrative, destructive, write and publishing operations require explicit authorization and audit.
5. API availability and live connectivity remain unverified until provider credentials, permissions and deployment-level smoke tests are validated.
