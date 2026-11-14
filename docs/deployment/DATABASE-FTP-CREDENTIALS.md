# SUPREMESETUHUB Database & FTP Credentials

This repository uses one central database for the main system and four logical
brand identities. FTP accounts are separate deployment credentials and may be
configured per brand only when that Hostinger FTP account actually exists.

## 1. Central database

Use Hostinger hPanel → Databases → Management to read the exact database host,
database name, database username, and password.

| Setting | Environment variable | Value |
|---|---|---|
| System / database label | `SUPREME_DB_NAME` | `u664492673_SUPREMESETUHUB` (confirm in hPanel) |
| Database username | `SUPREME_DB_USER` | `u664492673_SUPREMESETUHUB` (confirm in hPanel) |
| Database host | `SUPREME_DB_HOST` | Exact MySQL host shown by Hostinger |
| Port | `SUPREME_DB_PORT` | `3306`, unless hPanel specifies otherwise |
| Database password | `SUPREME_DB_PASSWORD` | The password of this exact MySQL user |

The example intentionally uses the same proposed label for database name and
username, but Hostinger's displayed values are authoritative. If hPanel shows
different values, use those exact values; do not rename a live database or user
just to make the strings match. All five identities share this central DB;
they do not need separate database usernames/passwords.

### Where to store the central DB password

- **Render/backend runtime:** open the backend service → Environment → add
  `SUPREME_DB_PASSWORD` with the actual MySQL user's password. Add the other
  `SUPREME_DB_*` values there too.
- **GitHub Actions (only if a workflow needs DB access):** repository →
  Settings → Secrets and variables → Actions → New repository secret →
  `SUPREME_DB_PASSWORD`. Add `SUPREME_DB_HOST`, `SUPREME_DB_NAME`, and
  `SUPREME_DB_USER` as secrets as well if the workflow requires them.

Do not put the real password in this document, `.env.example`, PHP, Python,
YAML, frontend code, or a chat message.

## 2. Four brand identity gates

These are logical identities inside the central database:

- `RAJESHKHANDELWALOFFICIAL`
- `RAJESHKHANDELWAL`
- `DRRAJESHKHANDELWALIBCOFFICIAL`
- `DRRAJESHKHANDELWALIBC`

They use `identity_code` for data scoping. Do not create four duplicate
physical databases merely to represent the four brand names.

## 3. FTP accounts

FTP username and password are not database credentials. In Hostinger hPanel →
Websites → Manage → FTP Accounts, copy the exact FTP server, account username,
and password for each actual account. The FTP username may not equal the brand
name; do not invent or rename it in code.

For each account that exists, create these GitHub repository secrets:

| Identity | Server secret | Username secret | Password secret |
|---|---|---|---|
| SUPREMESETUHUB | Reuses `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_SERVER` | Reuses `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_USERNAME` | Reuses `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_PASSWORD` |
| RAJESHKHANDELWALOFFICIAL | `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_SERVER` | `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_USERNAME` | `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_PASSWORD` |
| RAJESHKHANDELWAL | `HOSTINGER_RAJESHKHANDELWAL_FTP_SERVER` | `HOSTINGER_RAJESHKHANDELWAL_FTP_USERNAME` | `HOSTINGER_RAJESHKHANDELWAL_FTP_PASSWORD` |
| DRRAJESHKHANDELWALIBCOFFICIAL | `HOSTINGER_DRRAJESHKHANDELWALIBCOFFICIAL_FTP_SERVER` | `HOSTINGER_DRRAJESHKHANDELWALIBCOFFICIAL_FTP_USERNAME` | `HOSTINGER_DRRAJESHKHANDELWALIBCOFFICIAL_FTP_PASSWORD` |
| DRRAJESHKHANDELWALIBC | `HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_SERVER` | `HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_USERNAME` | `HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_PASSWORD` |

SUPREMESETUHUB currently deploys inside the existing RAJESHKHANDELWALOFFICIAL Hostinger account, so its FTP profile deliberately reuses those already-configured secrets. Do not create a duplicate SUPREMESETUHUB FTP password unless a separate FTP account is actually provisioned.

Only add a profile's secrets after that FTP account is created and verified.
An unconfigured profile is reported as incomplete; it must not silently borrow
another brand's password.

### Where to store each FTP password

GitHub repository → Settings → Secrets and variables → Actions → New repository
secret. Enter the exact secret name from the table and paste that FTP account's
password as its value. Never put it under Actions Variables; passwords belong
in Secrets.

## 4. Existing WordPress database credentials

The existing WordPress database remains separate. Keep its existing variables
(`WORDPRESS_DB_HOST`, `WORDPRESS_DB_NAME`,
`WORDPRESS_READONLY_DB_USER`, `WORDPRESS_READONLY_DB_PASSWORD`, and
`WORDPRESS_PRIMARY_DB_USER`) separate from `SUPREME_DB_*`.

Do not change the live WordPress database name/user/password as part of this
identity-gate work.

## 5. Current status

Repository code and example names are configuration scaffolding only. This PR
does not read GitHub secrets, provision Hostinger accounts, change live
passwords, or verify FTP/database connectivity. After secrets are entered,
run the appropriate read-only health checks before enabling deployments.
