# SUPREMESETUHUB — Personal Control Step 01

## Scope committed in this branch

- SUPREME remains the single owner-control authority.
- SUPREME ECOSYSTEM exposes the same control status and delegates allowlisted read-only commands to the shared control service.
- Both route groups are protected by their existing owner-only router dependencies.
- `SUPREME_CONTROL_TOKEN`, when configured, is compared using a timing-safe comparison and is required for command requests.
- Only these read-only commands are exposed: `platform.status`, `modules.list`, and `ai.status`. Arbitrary shell execution is not exposed.

## Endpoints

- `GET /supreme/control/status`
- `POST /supreme/control/commands`
- `GET /api/v1/supreme-ecosystem/control/status`
- `POST /api/v1/supreme-ecosystem/control/commands`

## Verification required

This branch adds focused unit tests, but those tests and the complete project test suite must run in GitHub Actions before merge. No live deployment, production storage, cloud replication, or recovery test is claimed by this step.
