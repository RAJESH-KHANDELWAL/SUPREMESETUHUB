# GLOBAL DATABASE ECOSYSTEM

Independent DATABASE-owned hierarchy and provider discovery package.

## Runtime modules

- `catalog.py`: DATABASE-owned root, category and provider taxonomy.
- `models.py`: identity and health models with UTC lifecycle timestamps.
- `ecosystem_registry.py`: thread-safe hierarchy registry with parent validation.
- `registry.py`: provider adapter registry (AWS, Google, Microsoft, Proton and Mega).
- `manager.py`: initialization, registration, lookup, listing, status, health, tree and relationship map.
- `test_manager.py`, `test_registry.py`: standard-library unittest coverage.

## Layer boundary

This package does not import or copy implementation code from API, CORE or ENGINE. Its catalog and registry are DATABASE-owned. Any future cross-layer interaction must be wired at the application composition boundary through explicit contracts.

## Operational status

The hierarchy and provider discovery are implemented locally. Existing provider adapters currently expose metadata and report `not_configured`; this package does not claim live database connectivity. Production persistence, provider authentication, migrations, transactions, backup/restore and integration tests remain separate implementation work.
