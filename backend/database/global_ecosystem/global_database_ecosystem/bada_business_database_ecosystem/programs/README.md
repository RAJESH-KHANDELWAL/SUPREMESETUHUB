# BADA BUSINESS DATABASE PROGRAMS

This package owns persistence for owner-scoped snapshots of Bada Business
program records.

## Responsibilities

- Create and migrate the `bada_business_program_records` table.
- Upsert program snapshots with uniqueness on `(owner_user_id, program_id)`.
- Read and delete records within the supplied owner scope.
- Optionally import the current program list from the canonical resource catalog.

## Architecture boundary

- Canonical program descriptions, links, prices and provider facts remain in
  `backend/bada_business_ecosystem/platform_resources/programs/`.
- Business rules and program workflows belong in CORE.
- HTTP endpoints and request/response validation belong in API.
- This package does not register customers, process payments, call provider APIs
  or claim external synchronization.
- Database access is delegated to the central `backend.database.service.DatabaseService`.

## Quick start

```python
from backend.database.global_ecosystem.global_database_ecosystem.bada_business_database_ecosystem.programs import (
    BadaBusinessProgramDatabaseManager,
)

manager = BadaBusinessProgramDatabaseManager()
manager.sync_canonical_catalog("authenticated-owner-id")
```

The owner ID must come from the authenticated application context, never from
untrusted request input.
