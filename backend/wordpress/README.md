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
