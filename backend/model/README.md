# Backend Model

Central namespace for backend-wide shared model contracts.

Domain-specific implementations remain with their owning domains. Infrastructure models live in
`backend/infrastructure/model/`. Persistence remains owned by `backend/database/`, and API
transport schemas remain in `backend/schemas/` and the relevant API packages.

Use the singular `model` naming convention consistently.
