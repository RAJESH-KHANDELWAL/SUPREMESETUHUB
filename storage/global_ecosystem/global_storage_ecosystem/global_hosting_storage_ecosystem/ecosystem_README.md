# Ecosystem Foundation

Reusable provider-neutral hosting storage foundation aligned with the GOOGLE STORAGE ECOSYSTEM parent-catalog pattern. Existing shared modules and provider-specific files are retained.

## Catalog architecture
- `README.md` — parent hosting ecosystem overview and capability navigation
- `taxonomy/global_hosting_storage_taxonomy.json` — canonical hosting taxonomy grouped by capability
- `category_index.json` — canonical index of all 23 hosting storage capability folders
- `ecosystem_manifest.json` — ecosystem identity, category identifiers, geographic coverage, readiness and governance

## Foundation modules
- `ecosystem_service.py` — ecosystem identity and truthful health contract
- `ecosystem_models.py` — typed hosting metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `tests/test_foundation.py` — offline foundation tests

## Readiness and integration boundary
FOUNDATION_READY means local package code loads. It does not mean a hosting provider is connected or that provisioning, deployment, DNS, certificates, backups, monitoring, upload, download or deletion operations work. External provider clients and operations belong in the API/integration layer. Production persistence belongs in the central database.

Never commit credentials, SSH keys, API tokens, database passwords, private logs or personal data. Use least privilege, secret management, encryption, audit logs, retention controls and jurisdictional compliance.
