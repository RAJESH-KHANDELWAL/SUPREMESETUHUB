# GLOBAL CLOUD — WHAT GLOBAL CLOUD PROVIDES — STORAGE ECOSYSTEM

Provider-neutral, global storage taxonomy and metadata foundation for cloud, hybrid, multi-cloud, and infrastructure storage providers.

## Ecosystem identity
- **Ecosystem:** `GLOBAL_CLOUD_STORAGE_ECOSYSTEM`
- **Package:** `global_cloud_storage_ecosystem`
- **Hierarchy:** GLOBAL CLOUD → WHAT GLOBAL CLOUD PROVIDES → STORAGE ECOSYSTEM
- **Scope:** Global
- **Foundation state:** `FOUNDATION_READY`
- **Provider connection state:** `NOT_CONFIGURED`

## Storage category ecosystems

Each storage domain has its own package namespace and follows the shared category-package layout: README, Python package entry point, configuration, manifest, models, service contract, API boundary placeholder, model/schema directories, PHP metadata reader where applicable, and offline tests.

1. [GLOBAL CLOUD OBJECT & BLOB STORAGE ECOSYSTEM](categories/global_cloud_object_blob_storage_ecosystem/README.md) — object stores, blob stores, S3-compatible catalogs, archive-object metadata.
2. [GLOBAL CLOUD FILE STORAGE ECOSYSTEM](categories/global_cloud_file_storage_ecosystem/README.md) — managed file shares, network file systems, shared files, file-sync metadata.
3. [GLOBAL CLOUD BLOCK & VOLUME STORAGE ECOSYSTEM](categories/global_cloud_block_volume_storage_ecosystem/README.md) — block volumes, boot/persistent volumes, snapshots.
4. [GLOBAL CLOUD BACKUP & ARCHIVE STORAGE ECOSYSTEM](categories/global_cloud_backup_archive_storage_ecosystem/README.md) — backup catalogs, long-term archive, restore points, disaster-recovery metadata.
5. [GLOBAL CLOUD HYBRID & MULTI-CLOUD STORAGE ECOSYSTEM](categories/global_cloud_hybrid_multi_cloud_storage_ecosystem/README.md) — hybrid catalogs, replication, migration inventory, multi-cloud policies.
6. [GLOBAL CLOUD STORAGE GOVERNANCE & OBSERVABILITY ECOSYSTEM](categories/global_cloud_storage_governance_observability_storage_ecosystem/README.md) — lifecycle, access, encryption, capacity, cost, audit, and retention metadata.

The canonical category list is maintained in `category_index.json`; detailed domain vocabulary is in `taxonomy/global_cloud_storage_taxonomy.json`.

## Global provider ecosystems

Provider namespaces are separate from storage categories. The provider catalog currently includes these namespace families:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud
- Oracle Cloud Infrastructure
- IBM Cloud
- DigitalOcean
- Cloudflare and Cloudflare R2
- Wasabi and Backblaze
- Alibaba Cloud, Tencent Cloud, and Huawei Cloud
- OVHcloud, Akamai Cloud/Linode, Hetzner, Vultr, IONOS, and Scaleway
- MinIO, Nutanix, Pure Storage, Dell Technologies, NetApp, and Red Hat

See `provider_index.json` for canonical provider IDs and package paths, and `providers/` for provider-specific namespaces. Provider inclusion is catalog coverage only; it is not a claim of product entitlement, region support, or working integration.

## Root package architecture

- `README.md` — ecosystem overview and navigation
- `ecosystem_README.md` — package ownership and engineering conventions
- `__init__.py` — Python package entry point
- `ecosystem_config.py` — credential-free environment configuration
- `ecosystem_manifest.json` — machine-readable identity, scope, governance, and readiness
- `ecosystem_models.py` — typed storage catalog records
- `ecosystem_registry.py` — local metadata registry
- `ecosystem_service.py` / `service.py` — foundation health and service entry points
- `ecosystem_taxonomy.py` — taxonomy loader and validation
- `catalog_api.py` — local read-only catalog facade
- `category_index.json` — category-to-package index
- `provider_index.json` — provider-to-package index
- `taxonomy/` — canonical global cloud storage taxonomy
- `categories/` — storage-domain category packages
- `providers/` — provider-specific catalog packages
- `tests/` — offline foundation and taxonomy tests

## Ownership and integration boundaries

- **Storage ecosystem owns:** provider identity, storage taxonomy, object/file metadata, lifecycle vocabulary, catalog records, storage health metadata, and storage-side governance.
- **API/integration layer owns:** provider SDKs, OAuth/authentication, authorization, external API clients, network calls, callbacks, and live provider operations.
- **Central database owns:** durable production persistence and operational records.

Do not embed provider credentials, SDK clients, or direct upload/download/delete operations in the taxonomy/catalog foundation.

## Readiness and verification

`FOUNDATION_READY` means local metadata/catalog code is initialized. It does not mean any provider is connected.

Keep every provider at `NOT_CONFIGURED` until an authorized integration has approved least-privilege credentials, a successful live health check, and end-to-end tests for each enabled operation. Record verified region support, entitlements, and limitations from authoritative evidence.

## Global governance and security

Apply privacy, security, least privilege, encryption, auditability, retention/deletion controls, consent where required, and jurisdictional compliance. Never commit credentials, access tokens, private keys, personal data, customer file contents, or production secrets.
