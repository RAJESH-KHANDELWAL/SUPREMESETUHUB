# ADOBE Storage Ecosystem

Canonical Adobe provider storage catalog for SUPREMESETUHUB.

## Package responsibilities
This package owns storage-side identity, metadata, child catalog entries, object lifecycle definitions and storage health metadata. Adobe API clients, OAuth, authentication and external operations remain in the Adobe API/integration layer.

## Child catalog
Nine product namespaces are maintained in this package. Each product README describes its catalog scope; these entries do not imply a live Adobe connection or generic storage API.

## Foundation modules
- `adobe_storage_ecosystem.py` — provider catalog and child ecosystem listing
- `ecosystem_manifest.json` — geographic scope, readiness state and governance declarations
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider identity and truthful health contract
- `tests/` — offline catalog and foundation tests

## Readiness boundary
FOUNDATION_READY means local package code is available. It does not prove provider API support, account entitlement, authorized connectivity or working upload/download/delete operations. Mark a provider connected only after authorized live health checks and end-to-end read/write tests pass. Production persistence belongs in the central database. Apply least privilege, encryption, audit logs, retention controls and jurisdictional compliance. Never commit credentials or personal data.
