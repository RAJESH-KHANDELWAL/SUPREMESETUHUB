# google ecosystem

The backend package is lowercase: `backend/google/google_ecosystem/`.

The catalog groups Google consumer, Workspace, Cloud, developer, AI, advertising,
analytics, maps, media, commerce, identity, and security products. It is designed as
a broad catalog of major products and API families, not a guarantee that every Google
product has a public API or that a user account is connected.

## API

- `GET /api/v1/google-ecosystem/status`
- `GET /api/v1/google-ecosystem/products`
- `GET /api/v1/google-ecosystem/products/{product_id}`

All endpoints require a SUPREMESETUHUB ADMIN/OWNER bearer session.

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
