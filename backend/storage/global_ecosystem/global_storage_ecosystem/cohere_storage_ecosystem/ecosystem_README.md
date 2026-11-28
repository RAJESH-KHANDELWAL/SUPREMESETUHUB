# COHERE Storage Ecosystem Foundation

Provider-neutral storage foundation with a Cohere-specific taxonomy and read-only catalog.

## Modules
- `ecosystem_service.py` — provider identity and truthful health contract
- `ecosystem_models.py` — typed metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_manifest.json` — Bharat-to-global scope and readiness state
- `taxonomy/cohere_storage_taxonomy.json` — grouped category taxonomy
- `category_index.json` — planned category folder index
- `ecosystem_taxonomy.py` — taxonomy loader and lookup helpers
- `catalog_api.py` — read-only listing, lookup and health interface
- `tests/test_foundation.py` — offline foundation and catalog tests

## Readiness
FOUNDATION_READY means local package code loads. It does not mean an external Cohere connection, data transfer, backup, synchronization, model API access or storage operation is active. Production persistence belongs in the central database. Never commit credentials or personal data.
