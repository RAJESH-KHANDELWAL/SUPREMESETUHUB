# GLOBAL CLOUD STORAGE ECOSYSTEM

A provider-neutral, global catalog and metadata foundation for cloud-storage services.

## Package identity
- **Ecosystem ID:** `GLOBAL_CLOUD_STORAGE_ECOSYSTEM`
- **Namespace:** `global_cloud_storage_ecosystem`
- **Scope:** Global cloud-storage taxonomy and metadata
- **Default readiness:** `FOUNDATION_READY`
- **Provider connection state:** `NOT_CONFIGURED`

## Responsibility
This package owns storage-side provider and service identity, taxonomy, metadata contracts, object-lifecycle vocabulary, and storage-health metadata. It provides a consistent catalog foundation across cloud-storage categories.

## Catalog scope
- Cloud object and blob storage
- Cloud file and shared-file storage
- Cloud block and volume storage
- Backup, archive, and disaster-recovery storage
- Hybrid and multi-cloud storage governance
- Storage lifecycle, observability, and cost metadata

## Architecture boundaries
This package is the storage-domain catalog and contract layer.

- **This package owns:** storage taxonomy, provider identity, metadata schemas, lifecycle definitions, catalog registry contracts, and health metadata.
- **API/integration layers own:** provider SDKs, authentication, authorization, external API clients, network requests, callbacks, and provider operations.
- **Central database layer owns:** durable production persistence and operational records.

Do not place provider credentials, SDK clients, or direct external upload/download/delete implementations in this package.

## Readiness and verification
The foundation can be initialized without any provider being connected. A catalog entry or provider namespace does not prove product availability, account entitlement, region support, authorized connectivity, or operational compatibility.

A provider may be marked connected only after:
1. The account owner has authorized the integration.
2. Credentials are obtained from an approved external secret source.
3. A live provider health check succeeds.
4. End-to-end tests verify the permitted read/write operations.
5. The integration's permissions, limitations, and region support are recorded.

Until then:
- Connection state remains `NOT_CONFIGURED`.
- External connectivity remains unverified.
- Storage operations remain disabled.
- Regions and capabilities remain unverified unless supported by evidence.

## Security
Never commit credentials, access tokens, private keys, personal data, customer file contents, or production secrets. Use an approved secret manager and least-privilege authorization for future integrations.

## Package contents
- `ecosystem_README.md` — package ownership, provider namespace convention, and safety boundary
- `ecosystem_config.py` — environment-backed, credential-free configuration
- `ecosystem_manifest.json` — machine-readable ecosystem identity, taxonomy, and readiness declarations
- `ecosystem_models.py` — typed storage catalog records
- `ecosystem_registry.py` — local metadata registry contract
- `ecosystem_service.py` — provider-neutral description and foundation health contract
- `tests/` — offline tests for catalog and readiness behavior

## Important
`FOUNDATION_READY` means the catalog foundation is initialized. It does **not** mean a cloud provider is connected or that live storage operations are available.
