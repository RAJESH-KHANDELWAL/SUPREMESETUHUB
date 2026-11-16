# GLOBAL CLOUD CORE ECOSYSTEM

**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-CLOUD-CORE-ECOSYSTEM`  
**Runtime domain:** `GLOBAL_CLOUD_ECOSYSTEM`  
**Runtime source of truth:** `backend/global_ecosystem/global_cloud_ecosystem/`

## Mission

Global Cloud Core is the provider-neutral control plane for cloud-provider identity, cloud capability taxonomy, geographic and sovereignty scope, workload classification, lifecycle/readiness metadata and safe catalog reporting across Bharat and global cloud infrastructure.

It is a metadata and policy-contract layer. It does not provision infrastructure, create cloud resources, authenticate to providers, execute workloads, move files, change billing, or perform network operations.

## Canonical runtime catalog

The authoritative provider inventory is `backend/global_ecosystem/global_cloud_ecosystem/catalog.py`. Core must consume its canonical IDs and metadata rather than maintain a competing inventory.

The runtime catalog currently contains **41 canonical provider records**. Each record is explicitly `catalog_only` with `live_connection_verified=False`. Catalog presence is not proof of an account, subscription, credentials, region availability, legal entitlement, service availability or live connection.

The adjacent runtime taxonomies remain authoritative:
- `capabilities.py` — capability groups and capability identifiers.
- `scope.py` — geographic, personal, business and advanced cloud scopes.
- `workloads.py` — workload domains, tiers, regions and adult-industry safety guardrails.
- `providers/` — provider adapter packages owned by the runtime integration boundary; their presence alone does not prove operational integration.

## Layer ownership

| Layer | Responsibility |
|---|---|
| Global Cloud Core | Provider identity, capability taxonomy, scope, workload classification, policy metadata, readiness and safe catalog snapshots |
| Global Cloud API | Provider authentication, IAM/OAuth, secret resolution, SDK/HTTP transport, API schemas and response normalization |
| Global Cloud Engine | Provisioning orchestration, deployment plans, adapters, jobs and runtime operations |
| Global Cloud Database | Resource inventory, structured state, migrations and transactions |
| Global Cloud Storage | Object/file/block storage operations, backups, replication and retention |
| Infrastructure / Network | Actual network, compute, DNS, edge, routing and infrastructure controls |
| UI | User consent, approvals, billing display and workflows |

Core must not duplicate provider API clients, credentials, provisioning, execution, persistence or UI responsibilities.

## Google reference package

`google_cloud_core_ecosystem/` is the reference provider Core package. It follows the ten-folder standard:
1. `authentication/` — identity/authentication requirements only; no token exchange.
2. `capabilities/` — declared cloud capability metadata.
3. `docs/` — provider scope, mapping, limitations and evidence.
4. `events/` — lifecycle and domain event contracts.
5. `lifecycle/` — registration, readiness and lifecycle state.
6. `models/` — typed provider/resource metadata.
7. `schemas/` — Core metadata validation schemas.
8. `security/` — security and secret-handling policy metadata.
9. `services/` — read-only Core facade contracts.
10. `tests/` — offline contract and metadata tests.

Other provider folders are preserved. Their existence does not mean they have the complete ten-folder standard or are canonical runtime providers. The current Core directory contains legacy/duplicate names that do not map one-to-one to the 41 runtime provider IDs; do not delete or rename them without an explicit migration plan. Canonical mapping and gaps are recorded in `GLOBAL_CLOUD_CORE_IMPLEMENTATION_STATUS.md`.

## Core service contract

`GlobalCloudCoreService` is read-only:
- `resolve_provider(provider_id)` resolves a canonical runtime provider.
- `provider_snapshot(provider_id)` returns allow-listed, secret-filtered metadata and readiness.
- `catalog_snapshot()` returns provider, origin, capability, scope and verification counts.
- `list_workloads(...)` and `workload_snapshot(workload_id)` expose safe workload taxonomy.
- `health_snapshot()` reports catalog and workload integrity.

Every snapshot explicitly reports that execution and persistence were not performed.

## Security and governance

- Tenant/actor context is descriptive input from the authenticated application layer; it is not authorization.
- Core never stores cloud credentials, access keys, private keys, passwords, tokens or secret values.
- Opaque secret references, if ever needed by a contract, are resolved only in the API/security boundary.
- Resource creation/deletion, IAM changes, network exposure, billing changes, data export and destructive operations require owning-layer authorization, explicit approval where appropriate, audit and policy checks.
- Workloads involving regulated, sensitive, adult or age-restricted data require lawful purpose, data minimization, jurisdictional compliance, access controls and safeguards. Catalog taxonomy is not approval to host or distribute content.
- Readiness may only be elevated using evidence from the owning API/Engine integration. Never infer a live connection from a provider name, folder, registry row or configured label alone.

## Verification requirements

CI should validate unique canonical provider IDs, provider metadata, scope/capability/workload taxonomies, Core-to-runtime mapping, ten-folder coverage, secret filtering, Python imports and owning-layer compatibility tests. A passing catalog test is not a cloud connectivity test.
