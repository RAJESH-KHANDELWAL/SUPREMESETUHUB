# Ecosystem Foundation

Reusable provider-neutral domain storage foundation. Existing shared ecosystem modules are retained.

## Modules
- `ecosystem_service.py` — ecosystem identity and truthful health contract
- `ecosystem_models.py` — typed domain metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_manifest.json` — Bharat-to-global scope and readiness state
- `service.py` — domain ecosystem capability descriptor
- `tests/test_foundation.py` — offline foundation tests

## Readiness
FOUNDATION_READY means local package code loads. It does not mean a registrar or DNS provider is connected. Production persistence belongs in the central database. Use least privilege, encryption, audit logs, retention controls, and jurisdictional compliance. Never commit credentials or personal data.
