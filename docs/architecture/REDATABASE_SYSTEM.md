# Redatabase System

Status: **design documentation; secondary database recovery execution is not established by this document.**

Purpose: define a controlled secondary path to reconstruct or re-establish a database when the primary database recovery path is unavailable, incomplete, or untrusted.

## Scope
- Secondary database recovery plans
- Re-provisioning an isolated database target
- Replaying approved schema migrations
- Rehydrating data from verified backup sources
- Schema, referential-integrity, and application validation
- Controlled connection cutover and rollback readiness

## Suggested modules
- `secondary-plans/`
- `targets/`
- `schema-rebuild/`
- `data-rehydration/`
- `integrity-checks/`
- `cutover/`
- `audit/`

## Boundary
REDATABASE is the fallback/reconstruction path for database-specific recovery. DATABASE remains the owner of database engines, schemas, migrations, and transaction semantics. RESTORE executes the selected restore operation; RECOVERY coordinates the broader incident.

## Safety
Never treat a schema migration or data import as proof of a valid recovery. Rebuild in isolation, verify schema and data integrity, test application compatibility, and obtain explicit approval before production cutover. Never commit production dumps, credentials, or connection strings to Git.
