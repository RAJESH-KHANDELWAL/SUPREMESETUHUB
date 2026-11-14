# Backend Models

Central location for shared, provider-neutral model contracts used across backend domains.

## Layout

- `infrastructure/` — shared infrastructure resource vocabulary and contracts.
- Domain runtime behavior remains in its owning backend domain package.
- Database persistence remains owned by `backend/database/`.
- API request/response schemas remain in `backend/schemas/` and API packages.

This package is for model definitions and contracts; it is not a second database or service layer.
