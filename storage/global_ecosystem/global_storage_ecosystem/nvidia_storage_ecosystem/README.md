# NVIDIA Storage Ecosystem

STORAGE-owned taxonomy namespace for NVIDIA. Catalog and foundation only; no live provider integration is implied.

## Responsibility
This package owns storage-side identity, metadata, taxonomy, object lifecycle definitions and storage health metadata. Provider API clients, authentication and external operations remain in their respective API/integration layers.

## Readiness boundary
The foundation does not prove provider API support, account entitlement, authorized connectivity or working upload/download/delete operations. Mark a provider connected only after authorized live health checks and end-to-end read/write tests pass. Never commit credentials or personal data.
