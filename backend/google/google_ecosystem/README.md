# google ecosystem

The backend package is lowercase: `backend/google/google_ecosystem/`.

The catalog groups Google consumer, Workspace, Cloud, developer, AI, advertising,
analytics, maps, media, commerce, identity, and security products. It is designed as
a broad catalog of major products and API families, not a guarantee that every Google
product has a public API or that a user account is connected.

## Entry points

- `service.py`: canonical product catalog and status service.
- `google.py`: Python facade exposing `list_products()`, `get_product()`, and
  `get_status()`.
- `google.php`: read-only PHP client that calls the authenticated SUPREMESETUHUB API.
  It requires server-side `SUPREMESETUHUB_API_BASE_URL` and
  `SUPREMESETUHUB_ADMIN_TOKEN` environment variables and PHP cURL.

## API

- `GET /api/v1/google-ecosystem/status`
- `GET /api/v1/google-ecosystem/products`
- `GET /api/v1/google-ecosystem/products/{product_id}`

All endpoints require a SUPREMESETUHUB ADMIN/OWNER bearer session.

## Included catalog areas

The catalog includes Gmail, Drive, Calendar, Docs, Sheets, Slides, Meet, Contacts,
Tasks, Forms, Google Workspace Admin, Google Cloud, Firebase, Maps, Search Console,
Analytics, Tag Manager, Ads, Gemini, Vertex AI, BigQuery, Cloud Storage, YouTube,
Photos, Play, Business Profile, Translate, speech services, Vision, Document AI,
Identity, Wallet, Pay, and other Google products. The live catalog in `service.py`
is the source of truth.

## Connection and security boundary

The registry does not claim a live Google connection. OAuth callback/state validation,
encrypted per-user token storage, revocation, and provider API adapters must be
implemented and verified before live user data operations are enabled. Product API
availability, quotas, region, billing, account eligibility, and Google policy can vary.

Google One, consumer apps, and other products without a general public API are
catalog-only. Google Cloud credentials must use a separate least-privilege Cloud
identity rather than consumer Gmail permissions.

Set `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REDIRECT_URI` only in
private deployment secrets. Never commit actual values.
