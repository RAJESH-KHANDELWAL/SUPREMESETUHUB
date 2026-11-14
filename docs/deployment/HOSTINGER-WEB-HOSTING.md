# Hostinger Web Hosting Deployment

## Deployment target

- Hostinger shared Web Hosting (not VPS).
- Website: `rajeshkhandelwalofficial.com`.
- Isolated destination: `public_html/supremesetuhub/`.
- Deployment transport: explicit FTPS on port 21.
- Canonical source: `frontend/`.
- Python/FastAPI backend is not uploaded to shared hosting. Existing API/backend hosting remains unchanged.

## GitHub Actions configuration

Repository secrets (the same account-specific FTP credentials already used by the Hostinger WordPress deployment):

- `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_SERVER`
- `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_USERNAME`
- `HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_PASSWORD`

Repository variable:

- `HOSTINGER_RAJESHKHANDELWALOFFICIAL_SUPREMESETUHUB_WEB_DIR`

Set the variable to the exact FTP-visible path for the isolated web directory, ending in `public_html/supremesetuhub/`. The workflow rejects the WordPress document root and other destinations.

## What gets deployed

The workflow builds a static website package from `frontend/`, generates the SUPREME home page from the canonical HTML/CSS/JS sources, validates the package, and uploads it using FTPS. It deploys only the generated `site/` artifact.

The workflow does not upload `backend/`, Docker files, Python dependencies, database files, environment files, or WordPress plugin directories. Existing WordPress and database content are not targeted. FTPS deployment uses `dangerous-clean-slate: false`.

## Run

- Push a change under `frontend/` to `main`, or
- Open GitHub Actions → **Deploy SUPREMESETUHUB to Hostinger Web Hosting** → **Run workflow**.

The workflow requires the production GitHub environment to permit deployment.
