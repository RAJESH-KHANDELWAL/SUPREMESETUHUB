# BADA BUSINESS PROGRAMS — ENGINE

This package dispatches execution operations for Bada Business program records.

## Operations
- `LIST_PROGRAMS`: read program entries from the canonical Bada Business catalog.
- `GET_PROGRAM`: fetch one canonical program by `program_id`.
- `PREPARE_PROGRAM`: prepare an execution payload without side effects; CORE
  approval is still required before an enrollment workflow may proceed.
- `EXECUTE_PROGRAM`: call an explicitly injected execution handler.

## Architecture
- ENGINE owns runtime operation dispatch and injected handler execution.
- Canonical program descriptions, URLs and provider facts stay exclusively in
  `backend/bada_business_ecosystem/platform_resources/catalog.py`.
- Eligibility, enrollment policy, approval decisions and business workflow
  orchestration belong in CORE.
- HTTP routes, authentication transport and request schemas belong in API.
- Database persistence belongs in DATABASE.
- Payment, registration, external provider API and connectivity are not
  implemented by this execution engine unless a separately configured handler
  performs an explicitly authorized operation.

## Safety and connection status
- No handler means `EXECUTE_PROGRAM` fails closed.
- `dry_run=True` never calls an execution handler.
- Program catalog availability does not mean provider API connectivity.
- This package does not claim a Bada Business official public API or live
  provider connection.
