# GOOGLE ECOSYSTEM

The Google domain is registered under `backend/GOOGLE/GOOGLE_ECOSYSTEM/`.
Its central catalog covers Gmail, Drive, Google One, Google Cloud, Meet, Calendar,
Docs, Sheets, Contacts, Tasks, Photos, YouTube, Analytics, and Maps Platform.

## API

- `GET /api/v1/google-ecosystem/status`
- `GET /api/v1/google-ecosystem/products`
- `GET /api/v1/google-ecosystem/products/{product_id}`

All endpoints currently require a SUPREMESETUHUB ADMIN/OWNER bearer session.

## Important status boundary

This commit establishes the backend registry only. It does **not** claim that a Google
account is connected. OAuth callback/state validation, encrypted per-user token storage,
revocation, and provider API adapters remain to be implemented and tested before live
Gmail/Drive/Meet operations can be enabled.

Google One is listed for product-level awareness only; this backend does not claim a
general public Google One API. Google Cloud credentials must use a separate least-privilege
Cloud identity rather than reusing consumer Gmail permissions.

Configure `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REDIRECT_URI`
only in the backend deployment's private environment/secrets. Never commit actual values.
