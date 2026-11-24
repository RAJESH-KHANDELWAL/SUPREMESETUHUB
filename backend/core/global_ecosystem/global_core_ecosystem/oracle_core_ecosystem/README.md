# ORACLE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Reference:** `google_core_ecosystem/`

Oracle Core is a read-only provider control plane for product identity, capability inventory, domain classification, policy, readiness and dependency metadata.

## Canonical files
- `manager.py`: stable Python entry point and `get_manager()`.
- `manager.php`: PHP interoperability facade; Python remains canonical.
- `constants.py`: stable identifiers and cross-layer references.
- `product_catalog.py`: curated product inventory and lookup.
- `domain_catalog.py`: capability domains and product ownership.
- `contracts.py`: tenant, secret-reference and readiness contracts.
- `policy.py`: scope guardrails and metadata redaction.
- `module_service.py`: shared read-only product service.
- `orchestrator.py`: discovery, health and dependency metadata.
- `service.py`: public status and master-catalog bridge.
- `ecosystem_manifest.json`: machine-readable inventory.
- `tests/`: structural and behavior tests.

Each of the 17 existing product packages contains only a small manager binding and package export. Shared logic is not duplicated.

## Product families
Oracle AI Services; Autonomous Database; Base Database; Block Volumes; Compute; Compute Instances; Data Science; Database Tools; Enterprise Applications; Fusion Cloud Applications; Generative AI; Identity; MySQL HeatWave; Networking; Object Storage; Observability; Virtual Cloud Networks.

## Layer ownership
| Layer | Responsibility |
|---|---|
| Core | Product identity, taxonomy, capability metadata, policy and readiness |
| API | Authentication, SDK clients, API transport and response normalization |
| Storage | Durable object/block data, retention and backups |
| Database | Database engines, schemas, migrations and transactions |
| Engine | Jobs, retries, provisioning and execution |
| Application/UI | Sessions, consent and user workflows |

## Security and lifecycle
1. Authenticated tenant and actor context must come from the application layer.
2. Catalog registration does not prove entitlement, authorization, regional availability or live connectivity.
3. Never store tokens, passwords, private keys or client secrets in Core.
4. Provisioning, billing, administrative and destructive operations require authorization and audit in the owning layer.
5. Report live connectivity only after authenticated deployment and provider smoke tests.

## Master catalog 2468
`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` is referenced read-only and on demand. Oracle inventory is not copied into numbered entries. No master-catalog entries are added.

## Implementation status
Metadata foundation only. No Oracle Cloud API calls, account authentication or remote provisioning are performed here.
