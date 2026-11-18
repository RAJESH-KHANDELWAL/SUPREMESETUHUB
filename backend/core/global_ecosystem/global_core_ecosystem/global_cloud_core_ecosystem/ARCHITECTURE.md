# GLOBAL CLOUD CORE — ARCHITECTURE

## Control-plane flow

```text
backend/global_ecosystem/global_cloud_ecosystem/
   catalog.py | capabilities.py | scope.py | workloads.py
                         |
                         v
              GLOBAL CLOUD CORE
       provider identity + taxonomy + policy
                         |
             safe metadata contracts
                         |
                         v
          API / Engine / Database / Storage
             (separate owning layers)
```

## Responsibility boundaries

- **Core:** canonical provider identity, capability groups, cloud scope, workload taxonomy, readiness metadata, policy metadata and safe read-only snapshots.
- **API:** credentials, authentication, IAM, provider SDK/HTTP clients, request/response transport and retries.
- **Engine:** deployment plans, provisioning orchestration, resource lifecycle execution and jobs.
- **Database:** resource inventory and structured state.
- **Storage:** actual object/file/block storage, backup and replication operations.
- **Infrastructure/Network:** compute, network, DNS, routing, edge and security controls.

Core must not import provider SDKs, read secret material, perform network I/O or mutate provider resources.

## Registry authority

The runtime catalog is the sole canonical provider inventory. The Core layer may add safe projections and validation but must not fork provider IDs or silently treat legacy package directories as registered providers.

## Readiness

- `CATALOG_ONLY`: catalog metadata exists; no integration evidence.
- `DOCUMENTED`: requirements and boundaries are documented.
- `SCAFFOLD`: a non-operational integration contract exists.
- `CONFIGURED`: owning runtime layer has verified configuration evidence.
- `LIVE_VERIFIED`: authenticated runtime smoke test and evidence have succeeded.

A provider can only be promoted by evidence from the owning API/Engine layer. This Core catalog currently has no live-verified provider records.

## Provider package convention

The Google Cloud Core package is the structural reference and contains the ten responsibility folders documented in its local README files. Folder presence alone is not an implementation; each responsibility requires contracts, tests and evidence.

## Safety invariants

- No credentials or secret values in Core.
- No provisioning, deployment, cloud API calls or persistence.
- No claim of live access without explicit runtime verification.
- Sensitive and regulated workloads require jurisdictional and data-governance controls.
- Adult-industry workloads remain subject to age assurance, consent, rights clearance, nonconsensual-content prevention, anti-exploitation and takedown safeguards defined by the runtime workload taxonomy.
