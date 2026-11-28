# Ecosystem Foundation

This directory contains the reusable folder/file foundation for its named ecosystem. Existing provider-specific files are preserved.

## Added foundation modules
- `ecosystem_service.py` — service identity and health contract
- `ecosystem_models.py` — typed domain records
- `ecosystem_registry.py` — thread-safe metadata registry
- `ecosystem_config.py` — runtime configuration (no secrets in source)
- `ecosystem_manifest.json` — Bharat-to-global scope and integration state
- `tests/test_foundation.py` — offline foundation tests

## Status policy
FOUNDATION_READY means the local package foundation loads. It does not mean a third-party API is connected. External integrations require authorized credentials, permissions, a live health check, and end-to-end read/write tests. Production records must use the central database, not the in-memory registry.

## Governance
Use least privilege, encryption, audit logs, data minimization, retention controls, consent where required, and applicable Indian and international laws. Never commit credentials or personal data.
