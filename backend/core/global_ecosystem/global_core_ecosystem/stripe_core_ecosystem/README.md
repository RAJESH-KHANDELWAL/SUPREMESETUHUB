# STRIPE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/`

## Mission
Stripe Core is Stripe's provider control plane for product identity, capability registration, domain classification, tenant contracts, policy metadata, readiness and dependency discovery. It retains all 22 existing Stripe product families and adds a product-specific manager entry point for each, backed by shared code.

## Canonical shared files
- `manager.py`: stable Python entry point (`get_manager()`) for status, products, domains, offerings and dependency metadata.
- `manager.php`: PHP interoperability facade; no provider calls.
- `catalog.py`: existing canonical Stripe family registry; retained as source of truth.
- `product_catalog.py` and `domain_catalog.py`: product and 10-domain inventories.
- `contracts.py`: tenant context, opaque secret reference and result contracts.
- `policy.py`: sensitive capability classification and secret/payment-data sanitization.
- `module_service.py`: shared read-only implementation used by all product managers.
- `orchestrator.py`: product/domain discovery, health and dependency metadata.
- `stripe_php_core_ecosystem/StripeCoreContract.php`: sanitized PHP result contract.
- `tests/`, `tools/`: behavioral regression tests and structural validator.

## Product packages
- `stripe_accounts_core_ecosystem` — accounts (ACCOUNTS_AND_IDENTITY)
- `stripe_billing_core_ecosystem` — billing (BILLING_AND_SUBSCRIPTIONS)
- `stripe_checkout_core_ecosystem` — checkout (PAYMENTS_AND_CHECKOUT)
- `stripe_customers_core_ecosystem` — customers (ACCOUNTS_AND_IDENTITY)
- `stripe_disputes_core_ecosystem` — disputes (RISK_AND_DISPUTES)
- `stripe_events_core_ecosystem` — events (EVENTS_AND_WEBHOOKS)
- `stripe_fraud_core_ecosystem` — fraud (RISK_AND_DISPUTES)
- `stripe_issuing_core_ecosystem` — issuing (ISSUING_AND_CARDS)
- `stripe_payment_intents_core_ecosystem` — payment_intents (PAYMENTS_AND_CHECKOUT)
- `stripe_payment_links_core_ecosystem` — payment_links (PAYMENTS_AND_CHECKOUT)
- `stripe_payment_methods_core_ecosystem` — payment_methods (PAYMENTS_AND_CHECKOUT)
- `stripe_payouts_core_ecosystem` — payouts (FINANCIAL_OPERATIONS)
- `stripe_products_prices_core_ecosystem` — products_prices (PRODUCT_CATALOG)
- `stripe_refunds_core_ecosystem` — refunds (RISK_AND_DISPUTES)
- `stripe_reporting_core_ecosystem` — reporting (FINANCIAL_OPERATIONS)
- `stripe_subscriptions_core_ecosystem` — subscriptions (BILLING_AND_SUBSCRIPTIONS)
- `stripe_tax_core_ecosystem` — tax (BILLING_AND_SUBSCRIPTIONS)
- `stripe_terminal_core_ecosystem` — terminal (IN_PERSON_COMMERCE)
- `stripe_treasury_core_ecosystem` — treasury (FINANCIAL_OPERATIONS)
- `stripe_webhooks_core_ecosystem` — webhooks (EVENTS_AND_WEBHOOKS)
- `stripe_climate_core_ecosystem` — climate (CLIMATE_AND_EMERGING_RAILS)
- `stripe_crypto_onramp_core_ecosystem` — crypto_onramp (CLIMATE_AND_EMERGING_RAILS)

Each retains its existing `catalog.py`, `__init__.py` and README and adds one product-specific `manager.py`. No empty template folders are generated.

## Layer boundaries and security
- Stripe API Ecosystem owns HTTP transport, SDK clients, authentication, webhook signature verification and response normalization.
- Stripe Core owns metadata, capability classification, tenant contracts, policy and orchestration descriptors only.
- Storage/Database own durable records, tenant isolation, retention and transactions; Runtime/Engine own queues, retries and scheduling.
- Never store Stripe secret keys, OAuth tokens, PAN, CVC or raw payment credentials in Core catalogs or logs.
- Payment writes require API-layer authorization, idempotency keys, audit correlation and merchant eligibility checks.
- Verify webhook signatures in the API adapter before Core event routing.
- Catalog registration does not prove account activation, country/currency eligibility, entitlement, authorization or live connectivity.

## 2468 master catalog
This implementation is registered only under `implementation_registry` in `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`; it is excluded from the 2,468 taxonomy-topic count.
