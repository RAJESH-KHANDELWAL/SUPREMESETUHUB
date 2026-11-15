# GLOBAL CLOUD STORAGE ECOSYSTEM

A provider-neutral storage catalog and metadata foundation for global cloud-storage services.

## Scope
- Cloud object and blob storage
- Cloud file and shared-file storage
- Cloud block and volume storage
- Backup, archive and disaster-recovery storage
- Hybrid and multi-cloud storage governance
- Storage observability, lifecycle and cost metadata

## Architecture boundary
This package owns taxonomy, provider identity, storage metadata contracts, lifecycle vocabulary and health metadata. Provider authentication, SDK clients, network calls, callbacks/webhooks and upload/download/delete operations belong in dedicated API/integration packages. Production persistence belongs in the central database layer.

## Readiness
All provider namespaces start as `NOT_CONFIGURED`. A catalog entry is not evidence of product availability, account entitlement, region support, connectivity or operational compatibility. Do not report a provider connected until authorized health checks and end-to-end tests have passed.

Never commit credentials, access tokens, personal data or customer file contents.
