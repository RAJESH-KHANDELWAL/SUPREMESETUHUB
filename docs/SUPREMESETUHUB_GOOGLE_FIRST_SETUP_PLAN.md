# SUPREMESETUHUB — Google-First Architecture and Safe Setup Plan

## 1. Purpose and naming

- **SUPREMESETUHUB** is the current name of the central Main Base Foundation (formerly called MAIN BASE FOUNDATION).
- It is the intended central control and integration layer for the ecosystem: identity, authorization, metadata, provider registry, service health, and defined platform APIs.
- GitHub is the source of truth for code, reviewed configuration templates, tests, and release workflows. GitHub is not the production database or uploaded-file store.
- This document records the intended architecture. It does not claim that any cloud account, provider, backup, database migration, or production connection is already active.

## 2. Intended provider hierarchy

The user's intended provider order is:

1. Google services — primary ecosystem/provider position.
2. Google Cloud — second infrastructure/provider layer.
3. Microsoft — third.
4. AWS — fourth.
5. Other providers — integrated through explicit SUPREMESETUHUB adapters and policies.

This order is a governance preference, not a statement that services are interchangeable. Gmail, Google Drive, Google Cloud Storage, and a managed database are different products with different capabilities. The exact production database and object-storage products must be selected only after inventory, account/billing verification, data requirements, and a cost/recovery comparison.

## 3. Core architecture boundaries

- **Central database:** SUPREMESETUHUB owns the logical central data contract and access rules. The current backend repository uses SQLite; a managed shared database requires a real adapter/schema migration and compatibility tests. Do not treat Google Drive as a relational database.
- **File bytes:** handled by an explicit storage interface and provider adapters.
- **GALLARY WOULT:** separate Drive-like product/workflow layer. It may use approved storage adapters but must not silently become the central database.
- **Google/Microsoft/AWS services:** separate adapters with least-privilege authorization, clear ownership, provider-specific error handling, and live end-to-end tests.
- **Existing domain and hosting sites:** keep running on their current hosts unless a separately approved migration is required.
- **Adult-content hosting:** AbeloHost, ViceTemple, Fap House, and related existing domain/hosting deployments remain separate hosting boundaries. They must not automatically share private files, credentials, customer records, or storage buckets with the general SUPREMESETUHUB ecosystem. Any future integration must be explicit, authorized, and isolated.
- **Render:** temporary/free runtime for testing only; not the permanent database or durable file-storage foundation.

## 4. Data protection requirements

Protect both database records and uploaded files.

- Inventory existing databases, tables, record counts, upload directories, file counts/sizes, current provider configuration, and existing backups before changing anything.
- Do not reset, overwrite, delete, or migrate production data during discovery.
- Create a consistent, encrypted backup outside the source runtime before any migration.
- Keep database backups and uploaded-file backups distinct but coordinated so metadata and files can be recovered together.
- Apply private-by-default access, least-privilege credentials, encryption in transit and at rest, retention rules, and audit logs where supported.
- Do not copy all data to every provider by default. Replication targets, data categories, regions, retention, user permissions, provider terms, and legal/privacy requirements must be explicit.
- Test backup integrity and a restore, not just backup-job success.
- Never commit secrets, live database files, user data, uploads, or backups to GitHub.

## 5. Safe staged rollout

### Phase 0 — Read-only discovery (no production changes)

1. Inspect the current GitHub code, configuration, migrations, storage adapters, and tests.
2. Inspect the actual Render service configuration and disk status in its dashboard.
3. Inventory existing data and backups using read-only methods where possible.
4. Record what is confirmed, missing, or inaccessible. Do not infer that data is absent because a repository does not contain a database file.

### Phase 1 — Choose concrete services

1. Confirm which Google account(s) and Google Cloud project(s) are available and who controls them.
2. Verify billing status and expected monthly budget before creating paid resources.
3. Select the database service based on relational needs, transactions, migration effort, regional requirements, backup/restore, and projected cost.
4. Select primary object storage and independent backup destination separately.
5. Define data classification, provider routing, retention, recovery objectives, and access policy.

### Phase 2 — Build in an isolated branch/staging environment

1. Add only the required adapter and migration changes on a separate branch/PR.
2. Keep current production behavior unchanged.
3. Add unit, integration, permission, failure/retry, and migration tests.
4. Test database records and file uploads/downloads in staging.
5. Verify file checksums and metadata relationships.
6. Test backup restoration and survival across service restart/redeploy.

### Phase 3 — Review and controlled cutover

1. Present test evidence, cost estimate, rollback plan, and data reconciliation report.
2. Obtain explicit approval before any production cutover.
3. Take a fresh verified backup immediately before cutover.
4. Migrate in a controlled window or use a tested parallel cutover strategy.
5. Verify critical records, authorization, uploads, downloads, checksums, health checks, and monitoring.
6. Keep the old system recoverable until acceptance checks pass.

## 6. Provider readiness must be evidence-based

A provider is not “connected” because it appears in a catalog or has environment variables. A provider can be marked connected only after authorized live checks for the required operations, including upload/read/list as appropriate, permission enforcement, checksum validation, error handling, and recovery tests.

## 7. Current known repository baseline

The repository's current persistence documentation says:
- the central database service uses SQLite;
- the Render blueprint uses the free plan and does not itself attach a persistent disk;
- a relative SQLite path or local upload directory is not proof of durable hosted storage;
- the Google Cloud Storage adapter is a scaffold, not a verified live connection;
- the storage catalog describes Google Drive and Microsoft OneDrive adapters as not implemented;
- an AWS S3 adapter exists, but live connection and production recovery remain unverified.

These are repository observations, not proof of the current live Render dashboard, account billing, or whether real production data exists. Those require separate verification.

## 8. Release gate

No production database/storage migration is approved by this document alone. Proceed only after Phase 0 data inventory, concrete service selection, backup verification, staging test evidence, rollback planning, and the owner's explicit approval.
