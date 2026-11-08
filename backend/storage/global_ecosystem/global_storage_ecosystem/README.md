# GLOBAL STORAGE ECOSYSTEM

Independent storage layer for provider discovery, storage identity, hierarchy
management, provider adapter contracts, and storage object metadata.

## Included foundation

- Provider catalog: AWS S3, Google Cloud Storage, Azure Blob Storage, Proton
  Drive, MEGA, and Hostinger Storage.
- Thread-safe in-memory registry with parent validation and defensive reads.
- Manager operations for status, health, lookup, registration, provider
  discovery, hierarchy tree, and relationship map.
- Provider-neutral adapter contract for live health, listing, upload, download,
  and delete operations.
- Storage object metadata model and offline unit tests.

## Layer isolation

This package is self-contained. It does not import or copy API, CORE, ENGINE,
or DATABASE implementation code. STORAGE owns provider metadata, identity
models, registry, manager, and provider adapter contract.

## Runtime and production boundaries

The registry is in-memory, not persistent. Provider folders are organizational
namespaces, not proof of live integrations. No credentials, cloud SDK clients,
network connections, uploads, downloads, deletes, encryption, replication, or
synchronization are activated by this foundation. A provider is not connected
until its adapter is implemented, securely configured, and passes live health
checks.

Before production use, adapters must enforce authorization, safe object names,
bounded streaming, integrity checks, audit logging, retention rules, and safe
deletion. Never commit credentials or tokens.

## Tests

Run from repository root:
python -m pytest backend/storage/global_ecosystem/global_storage_ecosystem -q
