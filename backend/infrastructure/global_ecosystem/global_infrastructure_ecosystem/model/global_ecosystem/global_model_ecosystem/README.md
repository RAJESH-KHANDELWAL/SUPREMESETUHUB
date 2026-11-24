# Global Model Ecosystem

Provider-neutral infrastructure contracts shared across the infrastructure domains.

## Language layout

- `.py`: executable model implementation used by the current Python backend.
- `.php`: parallel PHP implementation for PHP-based services and integrations.
- The contracts use matching snake_case serialized field names in both languages.
- Python does not execute PHP files. PHP files require a PHP runtime and are loaded independently.
- Keep both implementations aligned; the repository CI workflow runs the Python and PHP contract tests.

## Model families

| Family | Contract |
|---|---|
| Resource identity | Stable platform ID, resource type and optional provider reference |
| Provider reference | Provider ID and external resource ID; never credentials |
| Resource category | Provider-neutral resource categories and type vocabulary |
| Relationships | Typed links between infrastructure resources |
| Lifecycle | Planned, provisioning, active, degraded, suspended, failed and retired states |
| Location | Region, zone, data center and location metadata |
| Capacity | CPU, memory, storage and bandwidth metadata |
| Validation | Required identity fields and metadata shape |

## Ownership and safety

- This package defines contracts only; it does not provision or mutate infrastructure.
- Persistence and migrations belong to `backend/database/`.
- Provider credentials belong in secret/environment configuration, never in model records.
- Infrastructure runtime services and repositories remain in their owning infrastructure package.
- Provider connectivity and live operations must be implemented and authorized separately.
