# BACKUP, RECOVERY AND RESTORE INFRASTRUCTURE

This package is the canonical INFRASTRUCTURE implementation for backup lifecycle orchestration. It is part of MAIN BASE FOUNDATION and must remain aligned with the repository's existing layer ownership.

## Canonical ownership

| Responsibility | Canonical location | Boundary |
|---|---|---|
| Backup lifecycle orchestration and backup metadata | `backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/backup/` | Infrastructure |
| Central database connection, schema, transactions and SQL | `backend/database/` | Database |
| Storage providers, object storage and storage contracts | `backend/storage/` | Storage |
| Backup/recovery domain definitions and capability catalogue | Existing GLOBAL STORAGE / GLOBAL DATABASE / GLOBAL SERVER CORE ecosystems | CORE/catalogue |
| HTTP endpoints and request routing | Existing API layer | API |
| Executable jobs and scheduled operations | Existing ENGINE layer | ENGINE |

Do not create a second database controller, second storage registry, or duplicate CORE catalogue inside this package.

## Lifecycle responsibilities

1. **BACKUP** — define a backup plan, identify the source, capture metadata, request a provider operation through an approved adapter, record the resulting artifact and verify its integrity.
2. **RECOVERY** — define recovery objectives (RPO/RTO), select a valid recovery point, check dependencies, permissions and target readiness, and record an approved recovery plan.
3. **RESTORE** — execute a specifically authorized restore into an explicitly selected target; validate the restored data before marking the operation successful.
4. **RESTORATION VALIDATION** — verify checksums, schema, record counts and application-level health; preserve the result and audit trail.
5. **RETENTION** — enforce documented retention and legal-hold rules only after policy, authorization and deletion safeguards are implemented.
6. **DATABASE BACKUP** — coordinate with the canonical `backend/database/` layer. Database snapshots, transaction-log/PITR support and consistency guarantees must be implemented and tested by database-specific adapters.
7. **STORAGE / RE-STORAGE** — store backup artifacts through the canonical `backend/storage/` layer. Track provider, bucket/container, object key, region, encryption and retention metadata; do not store backup binaries in the application database.

## Existing implementation status

- `model.py` defines `BackupInfo` metadata.
- `service.py` currently creates and reads rows in the `backups` metadata table through `DatabaseController`.
- `controller.py` exposes metadata operations.
- The current implementation does **not** create a physical database dump, upload a backup artifact, perform point-in-time recovery, restore data, verify a restored application, or prove a live cloud-provider connection.
- The database ecosystem's backup service and the GLOBAL STORAGE / SERVER CORE packages contain capability descriptions or contracts; those declarations are not proof of executable backup/restore operations.

## Required implementation sequence

1. Audit and test the current backup metadata service and its database dependency.
2. Define provider-neutral backup, recovery-point, restore-job and validation-result models.
3. Add explicit interfaces for database snapshot/export and storage artifact operations; keep provider SDKs behind adapters.
4. Implement backup creation with atomic metadata state transitions, checksums, encryption policy and audit events.
5. Implement restore as a separate, authorization-gated workflow; never overwrite a production target by default.
6. Add isolated test databases and fake storage adapters for unit/integration tests.
7. Add restore drills, corruption tests, retention tests and recovery objective measurements before enabling production execution.

## Safety requirements

- Never commit credentials, encryption keys, database dumps, customer data or production backup artifacts.
- Never report a backup as successful until the artifact exists and integrity verification passes.
- Never report a restore as successful until post-restore validation passes.
- Require explicit target identification, authorization, audit logging and a tested rollback/recovery plan before destructive restore operations.
- Keep production execution disabled until provider connectivity and end-to-end restore tests are verified.

**Status:** architecture boundary documented; existing metadata functionality is not a verified backup/restore system.
