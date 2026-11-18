# STRIPE CORE ECOSYSTEM

Provider-specific Core registry and orchestration boundary for Stripe.

## Responsibility

This package belongs under `backend/core`. It owns the Stripe Core identity,
capability registry, service-family discovery, readiness metadata and policy
boundaries. It does not implement payment HTTP transport or store Stripe secrets.

The Stripe API implementation remains separate under:

`backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem`

## Structure

- `catalog.py` — provider Core catalog and 22 child Core registrations
- `service.py` — read-only status, module discovery and health surface
- `stripe_core_ecosystem.py` — public Core entry point
- `stripe_*_core_ecosystem/` — 22 dedicated child Core packages, each with
  `catalog.py` and `__init__.py`
- `tests/` — structural catalog tests

## API-to-Core mapping

All 22 family folders in the Stripe API ecosystem have corresponding Core
family packages. Core packages reference their API family; they do not copy
API transport, authentication, HTTP clients, webhook signature handlers or
credential configuration into the Core layer.

## Security and operational boundaries

- API keys belong in environment variables or a managed secret store in the API/runtime layer.
- Core stores no secret key, PAN, CVC, refresh token or raw payment credentials.
- Payment writes require idempotency and auditable request correlation.
- Webhook signatures must be verified in the API adapter before Core event routing.
- Tenant/account context must be isolated.
- Do not treat registry status as a successful Stripe connection.
- Stripe account, country, currency and product eligibility must be verified per merchant.

## Connectivity

All child modules start as `CORE_CATALOG_ONLY`. A provider's API access is not
claimed as live until the adapter, credentials, webhook flow and applicable tests
have been verified.
