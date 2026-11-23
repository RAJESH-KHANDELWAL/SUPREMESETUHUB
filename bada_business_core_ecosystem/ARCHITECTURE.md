# BADA BUSINESS CORE — ARCHITECTURE

## Package layout
- `programs/` — program discovery and request validation.
- `courses/` — read-only course discovery facade.
- `events/` — read-only event snapshot facade.
- `links/` — canonical platform/referral destination discovery.
- `products/` — product facade; empty until canonical product records exist.
- `registration/` — input validation only; no provider submission or payment.
- `referrals/` — referral-code extraction only; no commission or conversion claims.
- `php/` — PHP 8+ contract interoperability; no provider API transport.
- `tests/` — CORE behavior and safety-boundary tests.

## Source of truth
All provider facts and URLs remain in `backend/global_ecosystem/global_bada_business_ecosystem/`. CORE reads the canonical catalog through `resource_adapter.py`; it must not create competing provider catalogs.

## Layer boundaries
- CORE: domain policies, contracts, discovery and orchestration.
- API: HTTP routes, request/response schemas and transport.
- PHP: PHP-side adapter and contract interoperability.
- ENGINE: external workflow execution and retries.
- DATABASE/STORAGE: persistence and retention.

## Security
No credentials, payment details, private account data or access tokens belong in this package. Provider operations remain disabled until official API access, authentication, authorization and provider terms are independently verified.
