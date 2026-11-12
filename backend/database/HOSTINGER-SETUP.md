# SUPREMESETUHUB database deployment

## Canonical database

All PHP database entry points in this package resolve to the one central
SUPREMESETUHUB PDO connection. GE and GDE folders are compatibility entry
points; they do not create separate databases or credentials.

- Database: `u664492673_SUPREMESETUHUB`
- Database user: `u664492673_SUPREMESETUHUB`
- Host: copy the exact MySQL hostname from Hostinger hPanel
- Port: confirm the port shown by Hostinger; the code template defaults to 3306
- Password: set privately in Hostinger; never commit it

## Private PHP credentials

1. Copy `deployment/private/supreme-database.php.example` to a location outside
   `public_html`, for example `/home/ACCOUNT/domains/DOMAIN/private/supreme-database.php`.
2. Rename it to `supreme-database.php` and enter the exact host, confirmed port,
   database name, database user, and database password.
3. Configure the PHP environment variable `SUPREME_DB_PRIVATE_CONFIG` with the
   absolute path to that private file.
4. If your hosting panel cannot set PHP environment variables, configure the
   private include path using your host-supported PHP bootstrap mechanism.
   Do not place the private file under a publicly accessible directory.

The PHP config reads values from the private array first when environment
variables are absent. Python services use the `SUPREME_DB_*` environment
variables directly.

## Deploy

Upload the contents of this `backend/database` package to the matching
`backend/database` directory in your application. Keep the folder and file
names exactly as shown. Do not upload the private completed credential file.

## Validation

After setting credentials, run the application's approved database health
check. A matching file structure is not proof of a live connection. No schema
or data is created by loading the configuration files.
