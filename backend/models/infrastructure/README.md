# Infrastructure Models

Shared infrastructure model contracts are grouped here, separately from infrastructure runtime services.

- `global_infrastructure_models/` contains provider-neutral contracts for cross-domain catalog exchange.
- Operational domain models and services remain under `backend/infrastructure/`.
- Persistence remains under `backend/database/`.

Do not duplicate provider SDK models, database ORM models, or storage implementations here.
