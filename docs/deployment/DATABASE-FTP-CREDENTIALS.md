# SUPREMESETUHUB Database & FTP Configuration

This document records the requested consistent naming convention for the main
system and all four brand identities. It is repository configuration scaffolding;
it does not claim that these Hostinger accounts or hostnames have been provisioned.

## 1. Five identity names

1. `SUPREMESETUHUB` — MAIN
2. `RAJESHKHANDELWALOFFICIAL` — BRAND 1
3. `RAJESHKHANDELWAL` — BRAND 2
4. `DRRAJESHKHANDELWALIBCOFFICIAL` — BRAND 3
5. `DRRAJESHKHANDELWALIBC` — BRAND 4

## 2. Database variables

Each identity has the same five-field naming pattern:

```env
<IDENTITY>_DB_HOST=<IDENTITY>
<IDENTITY>_DB_NAME=<IDENTITY>
<IDENTITY>_DB_USER=<IDENTITY>
<IDENTITY>_DB_PASSWORD=
<IDENTITY>_DB_PORT=
```

All 25 concrete variables (five identities × five fields) are listed in
`backend/database/SUPREMESETUHUB_DB.env.example`.

**Important architecture rule:** these are identity-specific naming slots. The
current database architecture remains ONE physical central SUPREMESETUHUB
database, with four logical `identity_code` scopes. The four brand-prefixed
variables do not create four databases or independently provision database
users. The active Python/PHP central connection continues to use
`SUPREMESETUHUB_DB_*`. Existing WordPress databases remain separate.

The requested HOST/NAME/USER values in the example are naming placeholders.
Before a real connection, replace them with the exact database host, database
name and database username shown in Hostinger hPanel. The live values may have
Hostinger account prefixes and need not literally equal the logical identity
name. Never commit the actual password.

## 3. FTP variables

FTP uses the same five-field naming pattern:

```env
<IDENTITY>_FTP_HOST=<IDENTITY>
<IDENTITY>_FTP_NAME=<IDENTITY>
<IDENTITY>_FTP_USER=<IDENTITY>
<IDENTITY>_FTP_PASSWORD=
<IDENTITY>_FTP_PORT=
```

All 25 concrete FTP variables are listed in the same example file.
`FTP_NAME` is a logical profile/account label used by this repository; it is
not a standard FTP wire-protocol credential. The runtime reads the five
identity-prefixed fields through `backend/infrastructure/ftp/profiles.py`.

Before connecting, replace FTP HOST, USER, PASSWORD and PORT with the exact
details of the corresponding account in Hostinger hPanel. Typical defaults are
FTP/FTPS port 21 and SFTP port 22, but use the port and protocol actually
provided by the host. Do not assume the FTP username is the brand name.

## 4. Security and live status

- Password fields intentionally remain blank in the example.
- Put real passwords in private runtime environment variables or GitHub Actions
  Secrets, never in this repository.
- No live database or FTP connection was attempted by this configuration update.
- No Hostinger account, database, password, port, or WordPress installation was
  created or changed.
- Do not enable a deployment until actual hPanel values are entered and a
  read-only connection test succeeds.
