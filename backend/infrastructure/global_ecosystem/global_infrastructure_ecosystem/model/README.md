# Infrastructure Model

Infrastructure-owned model definitions and normalized global contracts.

- `resource.py` preserves the master infrastructure resource and relationship models.
- `global_ecosystem/global_model_ecosystem/` contains the cross-domain global model ecosystem.
- Every contract in that ecosystem has a Python `.py` implementation for the current backend and a PHP `.php` counterpart for PHP applications/integrations.
- PHP files are separate PHP source; they are not loaded by the Python runtime.
- Runtime services and persistence remain in `backend/infrastructure/service.py` and
  `backend/infrastructure/repository.py`. Database ownership remains in `backend/database/`.
