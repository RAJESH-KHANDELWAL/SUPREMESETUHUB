# GLOBAL STORAGE ECOSYSTEM
Independent STORAGE-owned catalog, models, hierarchy registry, manager and provider adapter contract.

## Architecture
- Root, category and provider catalogs maintained by STORAGE.
- Provider/category taxonomy aligned by naming with existing ecosystem families without importing API, CORE, ENGINE or DATABASE runtime code.
- Storage identity, health and object metadata models.
- Thread-safe registry; parent-first hierarchy manager; provider discovery; tree and connection map.
- Provider-neutral contract for live health, object listing, streaming upload/download and delete.
- Offline tests for catalog integrity, hierarchy, registry validation and object metadata.

## Readiness boundary
Provider records and folders are catalog/scaffolding only. They do not prove SDK support or live connections. Credentials, network clients, uploads, downloads, deletes, sync, replication, encryption and persistence are not enabled until independently implemented, securely configured and integration-tested. Never commit credentials.

Run: `python -m pytest backend/storage/global_ecosystem/global_storage_ecosystem -q`
