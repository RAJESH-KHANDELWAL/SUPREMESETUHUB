# WordPress Integration — SUPREMESETUHUB

This module connects the SUPREMESETUHUB FastAPI backend directly to the **existing live WordPress MySQL databases**. WordPress/PHP stays on the existing WordPress hosting; the backend uses a separate, authenticated MySQL connection to each database. It does not copy WordPress core files into Python.

## Primary connection: backend to each live WordPress database

```text
SUPREMESETUHUB FastAPI
  -> owner-authenticated /api/v1/wordpress/* routes
  -> WordPressService
  -> WordPressDatabaseConnection (mysql.connector)
  -> existing Hostinger MySQL database
  -> WordPress tables (options, posts, users, usermeta, ...)
```

The two sites are isolated by an explicit site allow-list:

- `rajeshkhandelwalofficial` -> `WORDPRESS_DB_*` environment variables
- `drrajeshkhandelwalibc` -> `WORDPRESS_IBC_DB_*` environment variables

The connector reads credentials only from the backend host's private Environment/Secrets settings. Do not commit real database credentials to GitHub or paste them into chat.

Configure these values from the exact database details shown in Hostinger hPanel:

For `rajeshkhandelwalofficial.com`:
- `WORDPRESS_DB_HOST`
- `WORDPRESS_DB_NAME`
- `WORDPRESS_DB_USER`
- `WORDPRESS_DB_PASSWORD`
- `WORDPRESS_DB_PORT` (usually `3306`)
- `WORDPRESS_TABLE_PREFIX` (often `wp_`, verify in `wp-config.php`)

For `drrajeshkhandelwalibc.com`:
- `WORDPRESS_IBC_DB_HOST`
- `WORDPRESS_IBC_DB_NAME`
- `WORDPRESS_IBC_DB_USER`
- `WORDPRESS_IBC_DB_PASSWORD`
- `WORDPRESS_IBC_DB_PORT` (usually `3306`)
- `WORDPRESS_IBC_TABLE_PREFIX` (often `wp_`, verify in `wp-config.php`)

Hostinger must permit remote MySQL access from the backend server's outbound IP. Use the database host shown by Hostinger, not the website domain unless Hostinger explicitly documents it as the database host. Grant only the permissions required by the operations you intend to run. Current connector operations are connection health and read-only table existence checks; do not grant broad write privileges unnecessarily.

## Direct database endpoints

All endpoints below require the SUPREME owner Bearer token:

- `GET /api/v1/wordpress/status` — bridge and per-site connection status
- `GET /api/v1/wordpress/sites` — registered site metadata
- `POST /api/v1/wordpress/sites/{site_id}/connect` — connect and test the configured MySQL database
- `GET /api/v1/wordpress/sites/{site_id}/health` — database health check
- `GET /api/v1/wordpress/sites/{site_id}/tables` — check required WordPress tables
- `POST /api/v1/wordpress/sites/{site_id}/disconnect` — close the in-process connection

Allowed `site_id` values are `rajeshkhandelwalofficial` and `drrajeshkhandelwalibc`.

The legacy aliases `GET /api/v1/wordpress/health/{site_id}` and `GET /api/v1/wordpress/status/{site_id}` are also owner-protected.

## Optional WordPress REST API

For content-level operations, the backend also supports the existing WordPress REST API over HTTPS. This is separate from the direct MySQL connection and uses WordPress Application Passwords:

- `WORDPRESS_SITE_URL`, `WORDPRESS_USERNAME`, `WORDPRESS_APPLICATION_PASSWORD`
- `WORDPRESS_IBC_SITE_URL`, `WORDPRESS_IBC_USERNAME`, `WORDPRESS_IBC_APPLICATION_PASSWORD`

Endpoints:
- `GET /api/v1/wordpress/sites/{site_id}/live-health`
- `GET /api/v1/wordpress/sites/{site_id}/live-posts?per_page=10`
- `GET /api/v1/wordpress/sites/{site_id}/live-pages?per_page=10`

Create an Application Password in the relevant WordPress user profile. Do not use the normal account password.

## What is and is not connected

A registered site is only metadata. The real database connection is verified only after the backend is deployed, the private database environment variables are configured, Hostinger remote MySQL access is allowed, and the owner calls the connect/health endpoint successfully.

This integration connects the backend to each site's existing database; it does **not** automatically copy, merge, or synchronize data between the two WordPress databases. A cross-site migration/sync would require a separately specified, backed-up, explicitly authorized operation.

## SUPREME HOME WordPress plugin

The shortcode remains `[dr_rajesh_supreme_home]`. It loads the canonical `home-html.html`, `home-css.css`, and `home-js.js` source files from GitHub Raw. These frontend source files are intentionally untouched by the database integration.
