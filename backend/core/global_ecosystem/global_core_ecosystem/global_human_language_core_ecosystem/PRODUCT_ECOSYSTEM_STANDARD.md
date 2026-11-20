# HUMAN LANGUAGE DOMAIN MODULE STANDARD

Use the Google Core separation pattern, adapted to human-language domain modules.

A domain module should contain only files that implement a real contract:
- `README.md`: scope, ownership and boundaries.
- `__init__.py`: stable public exports.
- `ecosystem_config.py`: immutable identity/configuration metadata.
- `ecosystem_manifest.json`: machine-readable module identity and status.
- `service.py`: read-only domain metadata service.
- `capabilities/catalog.py`: defined capability metadata.
- `models/` and `schemas/`: typed domain structures and validation schemas.
- `security/policy.py`: domain-specific privacy, rights and safety policy.
- `tests/`: executable contract tests.

Add authentication, events, lifecycle or docs submodules only when a real interface or contract exists. Do not create empty placeholder files or claim live execution. Provider API transport belongs to API; persistence belongs to Storage/Database; jobs belong to Runtime/Engine.
