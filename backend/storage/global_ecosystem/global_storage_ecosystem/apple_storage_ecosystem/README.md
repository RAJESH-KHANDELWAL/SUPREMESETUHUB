# APPLE Storage Ecosystem

Canonical Apple provider storage catalog for SUPREMESETUHUB.

## Package responsibilities
This package owns storage-side identity, metadata, child catalog entries, object lifecycle definitions and storage health metadata. Apple API clients, authentication and external operations remain in their respective API/integration layers.

## Child catalog
Eight Apple product namespaces are maintained in this package. Each product README describes its catalog scope. The former per-product taxonomy folders contain only repeated placeholder documentation; their classification scope is being consolidated into provider-level documentation rather than duplicated under every product.

## Foundation modules
- `ecosystem_manifest.json` — geographic scope, readiness state and governance declarations
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider identity and truthful health contract
- `tests/` — offline foundation tests

## Readiness boundary
FOUNDATION_READY means local package code is available. It does not prove Apple API support, account entitlement, authorized connectivity or working upload/download/delete operations. Mark a provider connected only after authorized live health checks and end-to-end read/write tests pass. Production persistence belongs in the central database. Apply least privilege, encryption, audit logs, retention controls and jurisdictional compliance. Never commit credentials or personal data.
