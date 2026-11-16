# GLOBAL HOSTING CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_hosting_core_ecosystem/`

## Mission
A provider-neutral control plane for hosting vendors, cloud infrastructure, managed web hosting, PaaS, edge/CDN/object storage platforms and hosting control panels. Core owns provider identity, capability taxonomy, tenant-scoped metadata policy, readiness contracts, discovery and dependency mapping.

## Inventory model
The supplied GitHub directory snapshot contains **118 hosting-related child folders**:
- **111 provider/platform packages** — infrastructure clouds, managed hosting companies, PaaS/application platforms, CDN/object-storage platforms and hosting control panels.
- **7 capability packages** — `app_platform`, `cloud_hosting`, `dedicated_vps`, `edge_storage_cdn`, `india_hosting`, `privacy_specialty`, `web_hosting`.
- Shared `integrations/`, `services/` and `tools/` are excluded.

The inventory is derived from folder names. Provider category labels are an initial taxonomy and must be checked against each package's contents and official product documentation before provider-specific API work is enabled.

## Ownership boundaries
| Layer | Owns |
|---|---|
| Global Hosting Core | Provider identity, taxonomy, metadata policy, readiness, discovery and dependency map |
| Global Hosting API | Provider auth, API clients, HTTP transport, response normalization and remote control-plane calls |
| Global Hosting Engine | Deployments, provisioning, retries, jobs, orchestration and long-running execution |
| Global Hosting Database | Durable tenant/provider/resource records, migrations and transactions |
| Global Hosting Storage | Backups, artifacts, deployment bundles, logs and stored assets |
| Application/UI | User sessions, consent, account linking and user-facing workflows |

Core must not provision servers, deploy applications, change DNS, issue credentials, upload files, perform provider API calls or persist operational state.

## Core modules
- `catalog.py`: canonical ecosystem identity and capability taxonomy.
- `provider_catalog.py`: 111 provider/platform records and 7 separately listed capability packages.
- `contracts.py`: tenant context, readiness and result contracts.
- `policy.py`: tenant/capability metadata validation and recursive secret-field filtering.
- `orchestrator.py`: provider discovery, inventory, health and dependency mapping.
- `service.py`: read-only public service and parent registry status.
- `ecosystem_manifest.json`: machine-readable inventory and ownership metadata.

## Readiness and security
All inventory rows are `CORE_CATALOG_ONLY`. API availability is unknown (`null`), connected is false, live connection is unverified and API calls performed are zero. No account access, provider entitlement, adapter implementation, server provisioning or deployment success is implied.

Tenant and actor identity must originate from the authenticated application layer. Provider authorization, account linking, consent, secret resolution and audit enforcement remain in their owning layers. Never commit API tokens, passwords, SSH keys, private keys, access keys, credentials, server IPs tied to private accounts or customer data.

## Verification boundary
This package is an inventory and Core metadata foundation only. It does not establish live hosting coverage, pricing, availability, account authorization, API connectivity, server provisioning, deployment success, backup completion or DNS propagation. Run focused tests and provider-specific sandbox checks before production use.
