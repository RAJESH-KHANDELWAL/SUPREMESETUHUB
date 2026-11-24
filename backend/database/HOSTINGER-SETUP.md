# SUPREMESETUHUB central database setup

## Final database topology

This project uses ONE physical MySQL/MariaDB database:

- `SUPREMESETUHUB` — the single main database and storage location.

Inside that same database are four logical identity gates:

1. `RAJESHKHANDELWALOFFICIAL`
2. `RAJESHKHANDELWAL`
3. `DRRAJESHKHANDELWALIBCOFFICIAL`
4. `DRRAJESHKHANDELWALIBC`

The four gates are not separate Hostinger databases and do not need separate
database users or passwords. They are identity scopes in the central database.
Identity-owned records must carry an `identity_code` and every read/write
query must enforce the matching identity scope. The application must deny
unscoped access to identity-owned records.

The ten feature permission gates (GITHUB, WEBSITE, WORDPRESS, AI, API, APP,
BUSINESS, ADMIN, GLOBAL and SUPREME) are authorization capabilities, not
additional physical databases.

Existing WordPress website databases remain separate and untouched. This
central-database setup does not merge or overwrite either WordPress database.

## Hostinger configuration

Create or confirm only the `SUPREMESETUHUB` database and its database user in
Hostinger hPanel. Use the exact MySQL hostname, database name, username and
port shown by hPanel. Do not create four additional databases for the identity
gates.

## Private credentials

Set the `SUPREMESETUHUB_DB_*` values from `SUPREMESETUHUB_DB.env.example` as server-side
environment variables or in a private PHP config file outside the public web
root. Never commit real passwords or upload the completed private file to the
public repository.

Python services must receive the central connection values as server-side
environment variables; PHP private include values are not automatically
available to Python.

## Migration and verification

Configuration does not create the database, tables, or identity records.
Back up the central database before applying an approved migration. Verify
the central connection and then verify each of the four identity scopes with
tests that prove cross-identity reads and writes are denied.

A shared PDO connection does not by itself enforce tenant isolation. Every
identity-owned repository/query must apply and validate `identity_code`.
Do not claim full isolation until those query paths and tests are implemented.

No live Hostinger database creation, migration, or deployment is performed by
this repository configuration change.
