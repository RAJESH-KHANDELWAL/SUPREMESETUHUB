# google ecosystem

The Google domain directory is `backend/google/`. The Google Ecosystem directory
is `backend/google/google_ecosystem/`.

## Requested file layout

```text
backend/
├── google.py                 # alongside the google/ directory
├── google.php                # alongside the google/ directory
└── google/
    ├── google_ecosystem.py   # alongside the google_ecosystem/ directory
    ├── google_ecosystem.php  # alongside the google_ecosystem/ directory
    └── google_ecosystem/
        ├── __init__.py
        ├── service.py        # canonical Google product catalog
        └── README.md
```

The Python facades expose `list_products()`, `get_product()`, and `get_status()`.
The PHP client calls the authenticated SUPREMESETUHUB catalog API. The root-level
`backend/google.php` loads the PHP client from the Google domain folder.

**Python naming note:** a sibling file `backend/google.py` and package directory
`backend/google/` share a basename. Python package imports resolve to the directory
package, so use `backend.google.google_ecosystem` for imports; `backend/google.py`
is intended as a script/facade entry point, not as the import path for the package.

## API

- `GET /api/v1/google-ecosystem/status`
- `GET /api/v1/google-ecosystem/products`
- `GET /api/v1/google-ecosystem/products/{product_id}`

All endpoints require a SUPREMESETUHUB ADMIN/OWNER bearer session.

## Catalog coverage

The catalog includes Gmail, Drive, Calendar, Docs, Sheets, Slides, Meet, Contacts,
Tasks, Forms, Google Workspace Admin, Google Cloud, Firebase, Maps, Search Console,
Analytics, Tag Manager, Ads, Gemini, Vertex AI, BigQuery, Cloud Storage, YouTube,
Photos, Play, Business Profile, Translate, speech services, Vision, Document AI,
Identity, Wallet, Pay, and other Google products. The live catalog in `service.py`
is the source of truth.

## Connection and security boundary

The registry is catalog metadata, not proof of a live Google account connection.
OAuth callback/state validation, encrypted per-user token storage, revocation, and
provider API adapters must be implemented and verified before live user-data
operations are enabled. Product API availability, quotas, region, billing, account
eligibility, and Google policy can vary.

The PHP client requires server-side `SUPREMESETUHUB_API_BASE_URL` and
`SUPREMESETUHUB_ADMIN_TOKEN` environment variables, HTTPS, and PHP cURL. Never
expose bearer tokens in browser code or commit credentials.

Google One, consumer apps, and products without a general public API are catalog-only.
Google Cloud credentials must use a separate least-privilege Cloud identity rather
than consumer Gmail permissions. Store `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`,
and `GOOGLE_REDIRECT_URI` only in private deployment secrets.
