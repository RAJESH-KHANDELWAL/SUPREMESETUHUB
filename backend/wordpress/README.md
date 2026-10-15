# WordPress Integration — SUPREMESETUHUB

This folder contains the WordPress site registry, database connector, service, and the WordPress plugin bridge.

## Connection architecture

```text
SUPREMESETUHUB API (FastAPI)
  -> owner-only /api/v1/wordpress/* routes
  -> WordPressService / WordPressRegistry
  -> remote WordPress MySQL database (Hostinger or other host)
```

The WordPress database remains on the hosting provider. GitHub stores the connector code only; never commit real database passwords or WordPress application passwords.

## Connect to the existing live WordPress installation

The real WordPress site remains installed on its current WordPress/Hostinger hosting. The Python backend does not run WordPress PHP core itself; it connects to that real installation over HTTPS using WordPress REST API + an Application Password.

Configure these values in the backend host's private Environment/Secrets (not in GitHub):

- `WORDPRESS_SITE_URL=https://rajeshkhandelwalofficial.com`
- `WORDPRESS_USERNAME=<WordPress admin/editor username>`
- `WORDPRESS_APPLICATION_PASSWORD=<Application Password generated in WordPress profile>`
- `WORDPRESS_IBC_SITE_URL=https://drrajeshkhandelwalibc.com`
- `WORDPRESS_IBC_USERNAME=<WordPress username for the IBC site>`
- `WORDPRESS_IBC_APPLICATION_PASSWORD=<Application Password generated in that WordPress profile>`

Create Application Passwords in the respective WordPress admin user profile. Do not use the normal account password. Keep these values private and never commit them.

Live API endpoints (all require the SUPREME owner Bearer token):

- `GET /api/v1/wordpress/sites/{site_id}/live-health`
- `GET /api/v1/wordpress/sites/{site_id}/live-posts?per_page=10`
- `GET /api/v1/wordpress/sites/{site_id}/live-pages?per_page=10`

The `site_id` values are `rajeshkhandelwalofficial` and `drrajeshkhandelwalibc`. These endpoints query the existing WordPress installation. A successful GitHub commit alone does not prove the live connection; the backend must be deployed and the private environment variables configured.

## Registered WordPress sites

- `rajeshkhandelwalofficial` — `https://rajeshkhandelwalofficial.com`
- `drrajeshkhandelwalibc` — `https://drrajeshkhandelwalibc.com`

## Required runtime environment variables

Configure these in the backend hosting service's private Environment / Secrets settings (not in GitHub files).

For `rajeshkhandelwalofficial`:
- `WORDPRESS_DB_HOST`
- `WORDPRESS_DB_NAME`
- `WORDPRESS_DB_USER`
- `WORDPRESS_DB_PASSWORD`
- `WORDPRESS_DB_PORT` (usually `3306`)
- `WORDPRESS_TABLE_PREFIX` (usually `wp_`)

For `drrajeshkhandelwalibc`:
- `WORDPRESS_IBC_DB_HOST`
- `WORDPRESS_IBC_DB_NAME`
- `WORDPRESS_IBC_DB_USER`
- `WORDPRESS_IBC_DB_PASSWORD`
- `WORDPRESS_IBC_DB_PORT` (usually `3306`)
- `WORDPRESS_IBC_TABLE_PREFIX` (usually `wp_`)

Hostinger must allow remote MySQL access from the backend host. Use the exact database host shown in hPanel; the website domain is not necessarily the MySQL host.

## Owner-only API

Every endpoint requires the SUPREME owner's valid bearer token:

- `GET /api/v1/wordpress/status` — bridge and connection status
- `GET /api/v1/wordpress/sites` — registered site metadata
- `POST /api/v1/wordpress/sites/{site_id}/connect` — open and test database connection
- `GET /api/v1/wordpress/sites/{site_id}/health` — live connection health
- `GET /api/v1/wordpress/sites/{site_id}/tables` — verify essential WordPress tables
- `POST /api/v1/wordpress/sites/{site_id}/disconnect` — close the database connection

Allowed `site_id` values are `rajeshkhandelwalofficial` and `drrajeshkhandelwalibc`.

## SUPREME HOME WordPress plugin

The plugin shortcode remains `[dr_rajesh_supreme_home]`. It loads the canonical `home-html.html`, `home-css.css`, and `home-js.js` source files from GitHub Raw. The page source files themselves are intentionally unchanged by this integration work.

## What "connected" means

The API code is wired in GitHub, but a live database connection is only established after the backend is deployed, the required secrets are configured, and Hostinger permits the remote connection. A registered site alone is not proof of a live connection.
