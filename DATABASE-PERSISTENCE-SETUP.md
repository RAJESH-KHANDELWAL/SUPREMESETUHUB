# SUPREMESETUHUB Database Persistence Setup

## Current behavior

The backend uses SQLite through `backend.database.service.DatabaseService`.
The database path is selected in this order:

1. Explicit `db_path` passed to `DatabaseService`.
2. `SUPREME_DB_PATH` environment variable.
3. Relative local-development default `data/supreme.db`.

A relative path is relative to the process working directory and must not be treated as persistent storage in a hosted deployment by itself.

## Local development

Set `SUPREME_DB_PATH` to a local file path excluded from version control, for example:

```dotenv
SUPREME_DB_PATH=data/supreme.db
SUPREME_FILE_STORAGE_DIR=data/shared_storage
GALLERY_WOULT_STORAGE_ROOT=data/shared_storage
GALLERY_WOULT_MAX_UPLOAD_BYTES=104857600
```

Keep database files, uploads, backups, and credentials out of Git.

## Render deployment

A Render service's ordinary filesystem may be ephemeral. If this application is deployed on Render and uses SQLite, attach a persistent disk to the service and set:

```dotenv
SUPREME_DB_PATH=/var/data/supreme.db
SUPREME_DB_PERSISTENCE_ACKNOWLEDGED=true
SUPREME_FILE_STORAGE_DIR=/var/data/files
SUPREME_FILE_STORAGE_DURABILITY_ACKNOWLEDGED=true
GALLERY_WOULT_STORAGE_ROOT=/var/data/files
GALLERY_WOULT_STORAGE_DURABILITY_ACKNOWLEDGED=true
GALLERY_WOULT_MAX_UPLOAD_BYTES=104857600
```

Only set the acknowledgement variables after checking that the actual persistent disk is attached and mounted at the configured path. These variables are operator assertions, not proof that a volume exists. The application reports persistence as unverified; confirm it with a staging upload, restart/redeploy, checksum check, and restore test.

The current Render blueprint uses the free plan and does not attach a persistent disk. The blueprint alone therefore does not guarantee durable database or file storage. This repository's current database service uses SQLite; setting a database URL does not convert it to PostgreSQL. A managed database requires an explicit adapter/migration.

## Important scaling limitation

SQLite and the current database-backed rate limiter are intended for a single application instance with modest write concurrency. Do not run multiple instances against separate local SQLite files and expect shared accounts, sessions, metadata, or rate limits. For horizontal scale, migrate to a shared managed database and a distributed atomic rate-limit store, and configure backups, migrations, and connection pooling.

## Verification checklist

- [ ] `SUPREME_DB_PATH` points to the actual mounted persistent volume.
- [ ] `SUPREME_FILE_STORAGE_DIR` and `GALLERY_WOULT_STORAGE_ROOT` point to the intended persistent storage path.
- [ ] Persistence acknowledgement is enabled only after verifying the host's mounted volume.
- [ ] A test database record survives service restart/recreation.
- [ ] A test file survives application restart and redeployment with matching checksum.
- [ ] Backup restore has been tested before production launch.
- [ ] Production database files, uploaded files, and secrets are not committed to Git.

Passing local tests does not prove a hosted deployment has a persistent disk attached. Verify the hosting configuration and run a staging recovery test.
