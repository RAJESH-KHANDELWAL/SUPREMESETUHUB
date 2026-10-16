# SUPREMESETUHUB Database Persistence Setup

## Current behavior

The backend uses SQLite through `backend.database.service.DatabaseService`.
The database path is selected in this order:

1. Explicit `db_path` passed to `DatabaseService`.
2. `SUPREME_DB_PATH` environment variable.
3. Relative local-development default `data/supreme.db`.

The service creates the parent directory when opening the database. A relative path is relative to the process working directory, so it must not be treated as persistent storage in a hosted deployment by itself.

## Local development

Set `SUPREME_DB_PATH` to a local file path that is excluded from version control, for example:

```dotenv
SUPREME_DB_PATH=data/supreme.db
```

Keep database files and backups out of Git. Do not commit real user data, credentials, or production database files.

## Render deployment

A Render service's ordinary filesystem may be ephemeral. If this application is deployed on Render and uses SQLite, attach a persistent disk to the service and set:

```dotenv
SUPREME_DB_PATH=/var/data/supreme.db
```

The mount path must match the actual persistent-disk mount path configured for that service. Do not set this value unless that disk is attached and mounted. If a persistent disk is not available, this repository's current DatabaseService does not automatically switch to a managed database: it currently implements SQLite. A PostgreSQL or other managed database requires an explicit database adapter/migration before it can be used. Do not assume that setting a database URL alone is supported.

The Render blueprint in this repository keeps the free plan and does not attach a persistent disk. Therefore, the blueprint by itself does not guarantee durable database storage.

## Important scaling limitation

SQLite is suitable for a single-instance deployment with modest write concurrency. Do not run multiple application instances against independent local SQLite files and expect shared accounts/sessions. For multiple instances or higher write concurrency, migrate to a managed server database (for example PostgreSQL) and configure backups, migrations, and connection pooling.

## Verification checklist

- [ ] `SUPREME_DB_PATH` points to the intended persistent volume.
- [ ] On Render, `SUPREME_DB_PERSISTENCE_ACKNOWLEDGED=true` is set only after verifying the actual `/var/data` persistent disk mount.
- [ ] The application process can create/open the configured database file.
- [ ] A test record remains available after closing and reopening a new `DatabaseService` instance.
- [ ] A staging redeploy/restart confirms that data persists on the configured storage.
- [ ] Backup restore has been tested before production launch.
- [ ] Production database files and secrets are not committed to Git.

Passing local tests verifies SQLite file persistence across service instances. It does **not** prove that a hosted deployment has a persistent disk attached; that must be verified in the hosting dashboard and by a staging redeploy.
