# META WEBHOOKS API ECOSYSTEM

Canonical service-family catalog under the Meta provider root in SUPREMESETUHUB.

## Scope
Webhook subscription setup, callback challenge verification, signature validation, event processing and bounded retries.

## Connection boundary
This directory documents the API family; it does not implement or prove a live connection. Use the shared server-side Meta provider adapter when implemented. Validate app mode, account and asset eligibility, currently approved permissions, product-specific rate limits and App Review requirements against official Meta documentation before enabling operations.

## Security
- Use least-privilege permissions and tenant-scoped authorization.
- Keep OAuth tokens and app secrets in encrypted server-side secret storage.
- Validate webhook signatures where applicable and redact credentials from logs.
- Separate read-only discovery from write operations; require explicit confirmation for destructive actions.

## Status
`CATALOG_ONLY` — documentation and service-family mapping only; no live connectivity is claimed.
