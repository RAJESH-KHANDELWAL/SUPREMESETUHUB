# Ecosystem Foundation

Reusable provider-neutral domain storage foundation aligned with the GOOGLE STORAGE ECOSYSTEM parent-catalog pattern. Existing shared ecosystem modules and domain-specific child folders are retained.

## Catalog architecture
- `README.md` — parent ecosystem overview and navigation to all child ecosystems
- `taxonomy/global_domain_storage_taxonomy.json` — canonical domain storage taxonomy grouped by capability
- `category_index.json` — canonical folder/path index for all 17 child ecosystems
- `ecosystem_manifest.json` — ecosystem identity, child catalog, geographic scope, readiness, and governance

## Foundation modules
- `ecosystem_service.py` — ecosystem identity and truthful health contract
- `ecosystem_models.py` — typed domain metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `service.py` — domain ecosystem capability descriptor
- `tests/test_foundation.py` — offline foundation tests

## Child ecosystem contract
Each independent child folder retains its own `README.md` and `manifest.json` or `ecosystem_manifest.json`, with domain-specific scope and governance. Core registration, DNS/nameserver, portfolio, and hosting packages remain distinct from the 13 domain capability catalogs.

## Readiness
FOUNDATION_READY means local package code loads. It does not mean a registrar, DNS, hosting, or certificate provider is connected. Production persistence belongs in the central database. Provider APIs and external operations belong in the API/integration layer. Use least privilege, encryption, audit logs, retention controls, consent, and jurisdictional compliance. Never commit credentials, authorization codes, API tokens, or personal data.
