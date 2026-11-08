# GLOBAL DATABASE ECOSYSTEM

Independent database and data-persistence domain under:

`backend/database/global_ecosystem/global_database_ecosystem/`

## Architecture

- `catalog.py`: canonical database taxonomy metadata.
- `models.py`: database ecosystem descriptors and health metadata.
- `manager.py`: database-owned provider discovery and status.
- `provider_base.py`: adapter contract.
- `registry.py`: provider adapter registry.
- Provider packages: AWS, Google, Mega, Microsoft, Proton, plus mirrored database-domain taxonomy folders.

## Layer boundary

This package is DATABASE-owned. It must not import, copy, or depend on implementation code from API, CORE, or ENGINE. Shared interaction, when required, must happen through stable contracts at the application composition boundary.

## Mirrored taxonomy

The directory taxonomy is structurally aligned with the API ecosystem directory tree. Folder alignment does not imply an API integration, database implementation, schema, migration, credential, or live connection.

Existing provider adapters and files are preserved. Missing taxonomy leaf folders are represented by `.gitkeep`.

## Operational truth

Provider discovery is metadata-only. Live database connectivity, migrations, persistence behavior, backup/restore, transactions, and production readiness must be independently implemented and tested per provider.
