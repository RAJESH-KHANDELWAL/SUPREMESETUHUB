# SUPREMESETUHUB Database & FTP Configuration

This document records the existing central database and shared FTP runtime
configuration for the main system and four logical brand identities. It is
configuration guidance; it does not claim that a live Hostinger connection has
been tested.

## 1. Five logical identity names

1. `SUPREMESETUHUB` — MAIN
2. `RAJESHKHANDELWALOFFICIAL` — BRAND 1
3. `RAJESHKHANDELWAL` — BRAND 2
4. `DRRAJESHKHANDELWALIBCOFFICIAL` — BRAND 3
5. `DRRAJESHKHANDELWALIBC` — BRAND 4

## 2. One central database

The runtime uses one physical central database through these environment
variables:

```env
SUPREMESETUHUB_DB_HOST=
SUPREMESETUHUB_DB_NAME=
SUPREMESETUHUB_DB_USER=
SUPREMESETUHUB_DB_PASSWORD=
SUPREMESETUHUB_DB_PORT=3306
SUPREMESETUHUB_DB_CONNECT_TIMEOUT=10
```

All five identities are logical scopes in that central database. The four
brand identities do not create separate physical databases. Identity-owned
records must carry an `identity_code` and every repository query must enforce
the authenticated identity scope. Existing WordPress databases remain
separate and must not be overwritten.

## 3. One shared FTP account, five logical profiles

The default deployment uses one physical FTP account for all five logical
profiles. Configure the shared runtime credentials once:

```env
FTP_SERVER=
FTP_NAME=
FTP_USERNAME=
FTP_PASSWORD=
FTP_PORT=21
FTP_TIMEOUT=15
```

The profile resolver maps this shared account to each of the five logical
identity profiles. Identity-specific variables such as
`RAJESHKHANDELWALOFFICIAL_FTP_HOST` and
`RAJESHKHANDELWALOFFICIAL_FTP_USER` are optional overrides only; use them
only if a separate account is actually provisioned later. Profile-specific
settings take precedence over the shared values.

At present the FTP service performs an explicit-FTPS login and a read-only
starting-directory check. It does not upload, delete, rename, create folders,
or enforce separate remote directory roots. Therefore these five profiles
are identity labels, not five isolated FTP accounts or proven directory ACLs.
Do not treat them as file-level isolation until a separately reviewed
directory-confinement layer is implemented.

## 4. Secrets and verification

- Put real passwords in private runtime environment variables or deployment
  secrets, never in Git-tracked files.
- Do not paste database or FTP passwords into chat or source code.
- The shared FTP resolver defaults to port 21 and a 15-second timeout; use the
  actual protocol and port supported by the Hostinger account.
- The FTP health check is read-only and reports whether the configured
  account can authenticate and read its starting directory.
- A successful configuration test is not proof that the live Hostinger
  connection works. No live database or FTP connection is claimed by this
  repository configuration alone.
