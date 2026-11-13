# SUPREMESETUHUB infrastructure management

## 1. Database ownership model

SUPREMESETUHUB uses one central platform database. The main identity is
`SUPREMESETUHUB`; the four identity gates are:

- `RAJESHKHANDELWALOFFICIAL`
- `RAJESHKHANDELWAL`
- `DRRAJESHKHANDELWALIBCOFFICIAL`
- `DRRAJESHKHANDELWALIBC`

These are authorization scopes in the same central database, not four extra
databases. The existing WordPress databases remain separate and are not
merged into the platform database.

## 2. Customer-owned infrastructure

Each customer is represented by a tenant. The customer remains the owner of
their domain, hosting account, FTP/SFTP account and application database.
SUPREMESETUHUB stores tenant-scoped metadata and revocable connection
references; it does not ingest or centralize the customer's WordPress content
or database records.

All customer resources must be queried with an authorized `tenant_id`.
Cross-tenant access is denied by default. A customer must explicitly authorize
each connection and can revoke it.

## 3. FTP model

The logical FTP registry is
`GITHUB-SUPREME/config/ftp-profiles.json`.

The Hostinger screenshot showed two existing FTP accounts on the same
`rajeshkhandelwalofficial.com/public_html` directory:

- `u664492673.SUPREMESETUHUB` — selected as the Main logical profile.
- `u664492673.RAJESHKHANDELWAL` — retained as an existing personal/legacy profile.

The second WordPress domain is known, but its FTP hostname, username and
directory have not been confirmed. No access is inferred for it.

The four identity-gate FTP profiles are logical placeholders only. They have
not been created in Hostinger. Do not create or deploy them until their
directory scopes and Hostinger account limits are confirmed.

Use FTPS or SFTP only. The Hostinger panel reports port 21, but the actual
FTPS handshake still needs a connection test. Never enable unencrypted FTP.
Never store passwords in JSON, source files or commit history.

## 4. Customer onboarding and secret handling

The customer onboarding policy is
`GITHUB-SUPREME/config/customer-management.json`.

Required sequence:

1. Create a tenant and identify its owner.
2. Verify domain ownership.
3. Register the customer's hosting provider.
4. Obtain explicit, scoped FTP/SFTP authorization.
5. Obtain explicit database authorization, preferably read-only for discovery.
6. Store credentials in an external secret manager and keep only secret
   references in platform metadata.
7. Run a read-only health check.
8. Register a deployment target and require customer approval before deploy.

GitHub Actions secrets are suitable for the platform's own fixed deployment
credentials. They are not a scalable per-customer credential vault.

## 5. MySQL migration artifact

The initial MySQL/MariaDB schema is
`backend/database/migrations/mysql/001_multi_tenant_infrastructure.sql`.
It creates only `ss_*` tables and seeds the five identity records
(main + four identity gates). It does not touch WordPress tables.

This is a migration file, not an automatic deployment. Review it, take a
backup, confirm Hostinger SQL compatibility, then execute it manually in
phpMyAdmin. Do not run it until the runtime adapter and rollback plan are
reviewed.

## 6. Runtime status and limitations

- PHP `supreme_main_foundation_config()` now describes one central database
  and four identity gates.
- The Python `backend/database/gde_connection.py` is a MySQL/MariaDB
  connection adapter driven by `SUPREME_DB_*` environment variables.
- The legacy `backend/database/service.py` still uses local SQLite by
  default. This change does not silently migrate that service or its existing
  data to Hostinger MySQL.
- Existing WordPress database access remains a separate, optional,
  read-only connector.
- No FTP connection, MySQL connection, schema migration, customer onboarding
  or live deployment is performed by adding these repository files.

A production cutover requires integration tests proving all modules use the
same intended central MySQL database, tenant isolation, least-privilege
credentials, backups and rollback.
