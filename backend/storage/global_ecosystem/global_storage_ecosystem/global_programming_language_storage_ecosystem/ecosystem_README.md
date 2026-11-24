# GLOBAL PROGRAMMING LANGUAGE Storage Ecosystem Foundation

This storage namespace mirrors the existing GLOBAL PROGRAMMING LANGUAGE API taxonomy. It is intentionally separate from the human-language storage ecosystem.

## Root modules
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — typed metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider-neutral foundation and health contract
- `ecosystem_manifest.json` — geographic scope, governance and readiness state
- `api_namespace_index.json` — exact API-to-storage namespace mapping
- `tests/` — existing offline foundation tests

## Namespace coverage
27 API-aligned domain namespaces are represented as child storage namespaces. See `api_namespace_index.json` for exact source and destination paths.

## Readiness
The current state is `FOUNDATION_SCAFFOLD_CREATED`. Existing local metadata foundation code and tests are retained. This does not mean language runtimes, compilers, interpreters, persistence, external integrations or execution services are production-ready. Production persistence belongs in the central database. Apply least privilege, encryption, audit logs, retention controls, dependency/license review and jurisdictional compliance. Never commit credentials or private data.
