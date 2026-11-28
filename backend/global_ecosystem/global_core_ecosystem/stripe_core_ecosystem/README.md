# STRIPE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Provider:** Stripe  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/`

## Mission

Stripe Core is the provider control plane for Stripe identity, service-family
registration, capability metadata, domain classification, policy boundaries,
readiness, dependency discovery and health reporting. It is metadata and
orchestration infrastructure; it is not a payment processor or API transport.

## Canonical architecture

- `manager.py` — canonical Python entry point and `get_manager()`.
- `manager.php` — PHP interoperability facade with recursive sensitive-field sanitization.
- `catalog.py` — canonical Stripe provider identity and the existing 22 service-family registrations.
- `contracts.py` — tenant context, secret references, readiness and result contracts.
- `policy.py` — capability, tenant, idempotency and verified-webhook guardrails.
- `domain_catalog.py` — seven Stripe-specific domain groups and family coverage.
- `module_service.py` — shared read-only service for all child Core packages; avoids 22 duplicate managers.
- `orchestrator.py` — service discovery, domain inventory, dependency mapping and health metadata.
- `service.py` — public status and registry surface.
- `master_catalog.py` — read-only bridge to the canonical 2,468-target master catalog.
- `stripe_core_ecosystem.py` and `__init__.py` — stable public exports.
- `stripe_*_core_ecosystem/` — 22 existing provider service-family packages.
- `tests/test_catalog.py` — structural, policy and behavior checks.

Child packages retain their own catalog identity. Shared cross-family behavior
belongs in the root infrastructure; do not create empty Google-style subfolders
or duplicate shared managers in every child package.

## Domain coverage

1. Provider Governance and Accounts
2. Customers and Payment Acceptance
3. Billing, Subscriptions and Commerce
4. Financial Operations and Reconciliation
5. Risk, Disputes and Financial Protection
6. Events and Integration Governance
7. Specialty and Emerging Services

Every registered API family maps to one Stripe Core domain. Domain assignment
is classification metadata, not a claim of provider availability.

## Layer ownership

| Layer | Responsibility |
|---|---|
| Stripe Core | Provider identity, capability metadata, policy, lifecycle, readiness and discovery |
| Stripe API Ecosystem | HTTP transport, Stripe SDK/client, authentication, request/response normalization and webhook signature verification |
| Stripe Storage/Database | Durable records, tenant isolation, retention and transactions |
| Stripe Engine/Runtime | Queues, retries, scheduling, reconciliation execution and background jobs |
| Application/UI | Checkout experience, customer consent, authenticated sessions and user workflows |

Core must not duplicate API clients, execute charges/refunds/payouts, store payment
credentials, persist PAN/CVC, or perform webhook signature verification.

## Security and operational rules

- Secret values stay in environment variables or a managed secret store in the API/runtime layer. Core may carry opaque secret references only.
- Tenant and actor context must be supplied by the authenticated application layer.
- Registered capabilities do not grant caller authorization, merchant entitlement, Stripe account access or country/currency eligibility.
- Payment writes require API-layer authorization, idempotency, request correlation and audit.
- Webhook signatures must be verified by the API adapter before event metadata is routed to Core.
- Never expose API keys, client secrets, webhook secrets, access tokens, PAN or CVC in status output.
- Live connectivity is reported only after deployed credentials, adapter, webhook flow and provider smoke tests have been verified.

## Master catalog relationship

`backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` remains the sole canonical
planning taxonomy owned by its source layer. Stripe Core reads its current
target/counts and related existing references on demand. The bridge is
read-only: it does not copy, modify, manufacture or increment numbered entries.
The 2,468 figure is a target, not the current completed count.

## Readiness

All 22 service families remain `CORE_CATALOG_ONLY` until the corresponding API
adapter, account configuration, authorization and tests are independently
verified. A healthy Core catalog is not a live Stripe connection.
