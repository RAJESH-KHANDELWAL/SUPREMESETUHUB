# SUPREMESETUHUB database deployment

## Database topology

SUPREMESETUHUB is the main foundation and owns four identity gates. Each gate
has its own dedicated MySQL/MariaDB database and credentials. All five
databases may live under the same Hostinger MySQL server/account, but they are
five distinct databases:

1. `SUPREMESETUHUB` — main/foundation database.
2. `RAJESHKHANDELWALOFFICIAL` — dedicated identity database.
3. `RAJESHKHANDELWAL` — dedicated identity database.
4. `DRRAJESHKHANDELWALIBCOFFICIAL` — dedicated identity database.
5. `DRRAJESHKHANDELWALIBC` — dedicated identity database.

The main foundation controls the identity registry and routes each identity
to its own database. GE and GDE are compatibility/application layers; their
configuration files expose the same five-database topology. They must not
silently route every identity to the main database.

Existing WordPress website databases remain separate and are not included in
these five identity databases. Do not rename, import, drop, or overwrite them.

## Hostinger setup

1. In hPanel, create/confirm the main database and its database user.
2. Create one separate database and dedicated database user for each of the
   four identity gates.
3. Grant each identity's application user access only to its corresponding
   identity database. Grant the main service only the permissions it needs
   on the main database and identity registry/control functions.
4. Use the exact Hostinger MySQL hostname and port shown in hPanel for each
   connection. Do not assume the port if the panel shows another value.
5. Put real passwords only in private server environment variables or the
   private PHP config file outside the public web root.

## Environment variables

Use `SUPREME_DB_*` for the main database. Each identity database uses its
matching prefix:

- `RAJESHKHANDELWALOFFICIAL_DB_*`
- `RAJESHKHANDELWAL_DB_*`
- `DRRAJESHKHANDELWALIBCOFFICIAL_DB_*`
- `DRRAJESHKHANDELWALIBC_DB_*`

See `SUPREME_DB.env.example` for the required variable names. Its identity
database names and usernames are placeholders until Hostinger confirms them.

## Private PHP credentials

The PHP foundation can load a private array from a file outside the public
web root. Set `SUPREME_DB_PRIVATE_CONFIG` to its absolute path. Store the
same exact environment variable names in that private array. Never commit
real credentials or upload the completed private file into the repository.

Python services must receive the same values as server-side environment
variables; PHP private include values are not automatically available to Python.

## Migration and verification

Configuration does not create databases or tables. Before running any schema
migration, back up each target database and confirm the migration is intended
for that specific database. Do not run identity migrations against an existing
WordPress database.

Verify each connection independently using a health check that reports the
identity name, selected database name, server version and connection status,
without exposing passwords. A matching folder structure is not proof of a
live connection. No live database creation or migration is performed by this
repository configuration change.
