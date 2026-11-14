# Infrastructure Model

Infrastructure-owned model definitions and normalized global contracts.

- `resource.py` contains the existing master infrastructure resource and relationship models.
- `global_infrastructure_models/` contains provider-neutral cross-domain model contracts.
- Runtime services and persistence remain in `backend/infrastructure/service.py` and
  `backend/infrastructure/repository.py`.
- Database ownership remains in `backend/database/`.

The former `backend/infrastructure/model.py` implementation is preserved as
`backend/infrastructure/model/resource.py`. The package initializer re-exports its public
symbols, preserving existing `from .model import ...` imports.
