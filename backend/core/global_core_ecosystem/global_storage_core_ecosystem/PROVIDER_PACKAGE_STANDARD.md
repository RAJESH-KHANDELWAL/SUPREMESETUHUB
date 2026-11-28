# Global Storage Provider Package Standard

Each provider package lives directly under `backend/core/global_ecosystem/global_core_ecosystem/global_storage_core_ecosystem/` and owns provider-specific Core metadata only.

Required provider package contents:
- `__init__.py`: public package interface.
- `README.md`: purpose, ownership, boundaries and readiness.
- `ecosystem_config.py`: stable provider identity and configuration metadata.
- `ecosystem_manifest.json`: machine-readable identity, capabilities, dependencies and security boundary.
- `service.py`: read-only provider Core status and capability discovery.
- `contracts.py`: provider Core data contracts where provider-specific contracts are needed.
- `policy.py`: provider metadata policy checks where provider-specific rules are needed.
- `authentication/`: authentication-context metadata only; actual OAuth/token exchange remains in API/auth layer.
- `capabilities/`: declared capabilities and readiness metadata.
- `docs/`: provider Core documentation.
- `events/`: event schemas and lifecycle metadata, not queue execution.
- `lifecycle/`: provider registration and lifecycle metadata.
- `models/`: provider Core models and value objects.
- `schemas/`: JSON/Python schema definitions.
- `security/`: policy metadata and redaction rules, no secrets.
- `services/`: provider Core read-only domain services.
- `tests/`: unit and contract tests.
 
Create only the files needed by the implementation; do not populate folders with empty placeholders when useful implementation files exist. Do not place API clients, access tokens, database engines, storage upload/download logic, job queues or UI here.
