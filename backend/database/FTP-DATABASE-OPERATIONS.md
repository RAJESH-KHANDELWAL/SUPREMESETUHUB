# SUPREMESETUHUB Database + FTP Operations

These are five code-owned systems in the GitHub repository. GitHub stores the
implementation and migration history; it is not itself a MySQL database host or
an FTP server.

## Five systems

1. **Database Manager** — `control_plane.py`: validates `SUPREME_DB_*` and
   performs a read-only MySQL/MariaDB health check.
2. **FTP Manager** — `backend/infrastructure/ftp/deployer.py`: explicit FTPS
   upload beneath the approved `supremesetuhub/` directory. No clean-slate
   deletion. Existing GitHub Actions deployment remains the production frontend
   deployment path unless explicitly switched.
3. **Backup Manager** — `backup_manager.py`: runs `mysqldump`, stores a
   SHA-256 manifest, and requires the MySQL client to be installed on the runtime.
4. **Restore Manager** — `restore_manager.py`: validates backup manifest and
   requires the exact phrase `RESTORE SUPREMESETUHUB`. Restore is destructive.
5. **Migration Manager** — `migration_manager.py`: dry-run by default,
   checksum-tracked SQL migrations, and explicit apply mode.

## Database boundary

There is one physical central database for SUPREMESETUHUB and its logical
identity gates. Existing WordPress databases remain separate. All central
connection values are read from `SUPREME_DB_*`; do not copy production
credentials into tracked files.

## GitHub configuration

Configure these as repository Actions secrets or deployment environment secrets:

- `SUPREME_DB_HOST`
- `SUPREME_DB_NAME`
- `SUPREME_DB_USER`
- `SUPREME_DB_PASSWORD`
- `SUPREME_DB_PORT` (optional; defaults to 3306)
- `SUPREME_DB_CONNECT_TIMEOUT` (optional; defaults to 10)
- `SUPREME_DB_SSL_CA` and `SUPREME_DB_SSL_REQUIRED` when the provider requires verified TLS
- `SUPREME_DB_BACKUP_DIR` on the backend runtime

Existing FTP secrets are resolved through the named profile definitions in
`backend/infrastructure/ftp/profiles.py`. Never commit FTP passwords.

## Safety and deployment

- Hostinger hPanel must provision the database and user; repository code cannot
  create a Hostinger database merely by adding files.
- Run health checks before migration.
- Create and verify a backup before applying a production migration.
- Migration dry-run is the default.
- Restore is blocked unless an exact confirmation phrase is passed and the
  backup checksum matches.
- The restore manager only targets the configured SUPREME database and refuses
  a target matching `WORDPRESS_DB_NAME`.
- The FTP uploader is restricted to a relative site subdirectory and never
  performs a recursive remote clean.
- The current Hostinger workflow uses the existing FTPS secrets and remains
  the canonical frontend deploy path.

## Runtime requirements

- Python standard library.
- Existing `PyMySQL` dependency for MySQL/MariaDB connections.
- `mysqldump` for backup and `mysql` for restore, installed on the backend
  runtime. GitHub-hosted workflow runners may use their own installed clients.
- No credentials are required to run syntax checks or migration dry-run with
  injected test configuration.
