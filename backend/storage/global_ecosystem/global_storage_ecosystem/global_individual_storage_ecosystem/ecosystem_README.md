# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM — Category Foundation

This package follows the standardized category-foundation layout used by the Google Storage Ecosystem category packages. It defines the provider-neutral individual-storage metadata contract; it is not a live personal cloud drive and does not claim a connection to an external storage provider.

## Canonical identity
- Ecosystem ID: `GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM`
- Package: `global_individual_storage_ecosystem`
- Provider / owner: `GLOBAL_INDIVIDUAL`
- Category: `INDIVIDUAL`
- Category group: `PERSONAL_AND_INDIVIDUAL_STORAGE`

## Foundation modules
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_manifest.json` — canonical identity, safety flags and readiness state
- `ecosystem_models.py` — metadata record contract with opaque owner reference
- `ecosystem_registry.py` — in-memory registry for local development and tests only
- `ecosystem_service.py` — taxonomy/index consistency validation and health contract
- `service.py` — category-specific service entry point
- `api/routes.py` — framework-neutral status and health handlers
- `models/record.py` — public model export
- `schemas/manifest.schema.json` and `schemas/individual_storage_record.schema.json` — JSON contracts
- `taxonomy/global_individual_storage_taxonomy.json` and `category_index.json` — taxonomy source and flat index
- `tests/test_foundation.py` — offline tests
- `php/global_individual_storage_ecosystem.php` — read-only PHP metadata reader

## Data ownership and security
Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations belong to their respective services. This package stores opaque references and minimized metadata only. It must not store personal file content, credentials, authentication secrets or cryptographic keys.

## Readiness contract
`CATEGORY_FOUNDATION_SCAFFOLD` means the package structure and local contracts exist. Health reports validate the manifest identity, taxonomy/index agreement and safe integration defaults. It does not mean an external provider is connected. Authorized integration, live provider health checks and end-to-end tests are required before any storage operation can be enabled. Upload, download, delete and synchronization remain disabled.
