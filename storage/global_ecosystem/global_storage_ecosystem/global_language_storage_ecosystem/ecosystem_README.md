# GLOBAL LANGUAGE Storage Ecosystem Foundation

Reusable storage foundation for the GLOBAL LANGUAGE API ecosystem. Existing root modules and provider-specific API identities are retained; storage namespaces are mapped in `api_namespace_index.json`.

## Root modules
- `ecosystem_service.py` — provider-neutral identity and health contract
- `ecosystem_models.py` — typed metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_manifest.json` — ecosystem scope and readiness state
- `api_namespace_index.json` — API-to-storage namespace map
- `tests/` — offline foundation tests

## Child namespace structure

The API mapping contains 52 namespaces: 12 provider namespaces, 37 domain namespaces, and 3 support-module namespaces. Each child namespace currently contains a README scaffold. The scaffold establishes ownership and naming only; detailed models, schemas, adapters, and persistence must be implemented against the shared storage contracts and source API modules.

## Readiness

FOUNDATION_SCAFFOLD_CREATED means namespace scaffolding exists. It does not mean an external provider is connected or that production upload/download/delete operations are ready. Production persistence belongs in the central database. Use least privilege, encryption, audit logs, retention controls, and jurisdictional compliance. Never commit credentials or personal data.
