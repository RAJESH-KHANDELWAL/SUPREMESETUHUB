# GLOBAL STORAGE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_storage_core_ecosystem/`

## Mission

Provider-neutral control plane for storage provider identity, curated product-family inventory, domain classification, capability metadata, tenant context, lifecycle/readiness, dependency mapping and policy boundaries.

## Provider coverage

- **Apple** — iCloud Drive, iCloud Photos, iCloud Backup.
- **Amazon Web Services** — Amazon S3, Amazon S3 Glacier storage classes, Amazon EFS, Amazon FSx, Amazon EBS, AWS Storage Gateway, AWS Backup.
- **DigitalOcean** — DigitalOcean Spaces, DigitalOcean Volumes, DigitalOcean Droplet Backups.
- **Google Cloud** — Google Cloud Storage, Google Cloud Filestore, Google Persistent Disk, Backup and DR Service, Storage Transfer Service.
- **Microsoft** — Azure Blob Storage, Azure Files, Azure Managed Disks, Azure NetApp Files, Azure Backup, OneDrive, SharePoint document libraries.

## Responsibility domains

1. **Provider Governance** — Provider identity, registration, eligibility, ownership and provider lifecycle.
2. **Object Storage** — Buckets, containers, objects, namespaces, metadata and object lifecycle.
3. **File Storage** — Managed file shares, network file systems, protocols and file access metadata.
4. **Block Storage** — Volumes, disks, snapshots and attachment metadata.
5. **Personal Cloud Drives** — Personal files, folders, sync clients and user-owned cloud-drive metadata.
6. **Collaborative Document Storage** — Team document libraries, shared workspaces, permissions and version metadata.
7. **Backup and Recovery** — Backup plans, restore points, retention, recovery objectives and restore authorization.
8. **Archive and Retention** — Cold/archive tiers, retention schedules, legal holds and lifecycle rules.
9. **Data Transfer and Migration** — Bulk transfer, migration planning, transfer jobs and validation metadata.
10. **Sync and Replication** — Sync policies, replication topology, consistency and conflict metadata.
11. **Sharing and Access** — Sharing links, access scopes, permissions, IAM boundaries and access reviews.
12. **Encryption and Key Boundaries** — Encryption metadata, key references, customer-managed key boundaries and rotation state.
13. **Storage Security and Compliance** — Threat protection, audit metadata, compliance posture and data residency.
14. **Observability and Cost** — Capacity, usage, metrics, quotas, billing references and cost optimization metadata.
15. **Edge and Hybrid Storage** — Hybrid gateways, edge caches, local/cloud tiering and connected storage metadata.
16. **Lifecycle and Versioning** — Object versions, snapshots, lifecycle policies, immutability and deletion boundaries.
17. **Tenancy and Data Governance** — Tenant isolation, data classification, ownership, residency and governance metadata.

## Architecture

- `catalog.py`: provider registry and canonical ecosystem identity.
- `product_catalog.py`: curated product-family registry and filtering.
- `domain_catalog.py` / `domain_runtime.py`: taxonomy and shared domain manager.
- `contracts.py`: tenant, provider, product-reference and result contracts.
- `policy.py`: metadata validation, redaction and action classification.
- `module_service.py`: reusable provider-scoped read-only service.
- `orchestrator.py`: provider/product/domain discovery, health and dependencies.
- `service.py`: public read-only service.
- `manager.py`: canonical Python entry point.
- `manager.php`: thin PHP interoperability facade.
- `integrations/registry.py`: adapter reference registry only; no API transport.
- `services/storage_inventory_service.py`: read-only product inventory facade.
- `tools/validate_storage_catalog.py`: offline catalog validation.
- `global_*_core_ecosystem/`: responsibility-specific domain managers.
- Provider packages retain their existing package names and add only provider-specific manager interfaces.

## Layer boundaries

Core owns identity, inventory and policy metadata. Provider Storage owns provider-specific storage operations. API owns OAuth, SDK clients, transport and response normalization. Database owns persistence engines and transactions. Runtime owns queues, jobs and retries. Application owns UI and user consent.

## Security and truthfulness

Catalog entries do not prove installation, account connection, permission, subscription, licensing or service entitlement. Never store credentials, access tokens, private keys or encryption keys in this package. Live connectivity must remain false until authenticated deployment smoke tests pass. Destructive, restore, sharing, retention and administrative actions require explicit authorization and audit. No upload, download, delete or restore API is implemented here.
