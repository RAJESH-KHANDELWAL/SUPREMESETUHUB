# STRIPE API ECOSYSTEM

Stripe provider package for payment acceptance, billing, subscriptions, customer
management, financial reporting and platform commerce workflows.

## Structure

- `stripe_api_ecosystem.py` — provider metadata and service-family registry
- `config.py` — environment-backed configuration and validation
- `auth.py` — Stripe API-key and restricted-key handling
- `client.py` — HTTPS API client, request IDs and bounded retries
- `services.py` — service-family exports and shared operations
- `webhooks.py` — webhook signature verification and event normalization
- `tests/` — unit tests using mocked HTTP/webhook payloads
- `stripe_*/` — dedicated service-family package folders

## Security

Never commit API secrets. Load keys from environment variables or a managed secret
store. Use least-privilege restricted keys where feasible. Verify webhook signatures
against the raw request body, use idempotency keys for write operations, and avoid
logging payment data or secrets.

## Connectivity status

This is an integration scaffold. `live_connection_verified` remains false until
valid credentials, authenticated API calls, webhook verification and tests succeed.
