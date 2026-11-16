# BADA BUSINESS DATABASE PROGRAMS

This package owns persistence for owner-scoped snapshots of Bada Business
program records.

## Responsibilities
- Create and migrate `bada_business_program_records`.
- Upsert snapshots unique on `(owner_user_id, program_id)`.
- Read and delete within the supplied owner scope.
- Import the program list from the canonical resource catalog on explicit request.

## Architecture boundary
- Canonical program descriptions, links, prices and provider facts remain in
  `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/programs/`.
- Business rules and program workflows belong in CORE.
- HTTP endpoints and request/response validation belong in API.
- No customer registration, payment processing, provider API calls or external
  synchronization are implemented here.
- Database access uses the central `backend.database.service.DatabaseService`.

## Usage
```python
from backend.database.global_ecosystem.global_database_ecosystem.bada_business_database_ecosystem.programs import (
    BadaBusinessProgramDatabaseManager,
)
manager = BadaBusinessProgramDatabaseManager()
manager.sync_canonical_catalog("authenticated-owner-id")
```

The owner ID must come from authenticated application context, never untrusted
request input.
