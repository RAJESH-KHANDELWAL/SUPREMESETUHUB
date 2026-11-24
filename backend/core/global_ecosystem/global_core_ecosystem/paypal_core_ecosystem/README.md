# PayPal Core Ecosystem

**Parent:** Global Core Ecosystem  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/`

## Purpose

PayPal Core is the provider-level control plane for product identity, capability inventory, domain ownership, policy metadata, readiness and discovery. It is not a payment processor and does not call PayPal APIs.

## Shared root architecture

- `manager.py`: canonical Python entry point and product manager factory.
- `manager.php`: PHP interoperability facade.
- `catalog.py` / `product_catalog.py`: provider and 13-product inventory.
- `domain_catalog.py`: six payment capability domains.
- `contracts.py`: tenant context, readiness and result contracts.
- `policy.py`: capability classification, tenant-context validation and safe metadata output.
- `module_service.py`: shared product-level Core behavior.
- `orchestrator.py`: product/domain discovery, health and dependency map.
- `service.py`: public status and registry integration.
- `master_catalog.py`: read-only lookup into the canonical 2468-target master catalogue.
- `paypal_php_core_ecosystem/PayPalCoreContract.php`: PHP result contract and secret-field sanitization.
- `tests/test_paypal_core.py`: structure, inventory, policy and master-catalog tests.

## Product packages

Each product folder contains only a real `__init__.py` and a thin `manager.py` bound to the shared service. Product-specific business logic and API transport belong to the PayPal API/runtime layers, not duplicated in Core.

- `paypal_billing_plans_core_ecosystem`: Billing plans and pricing metadata.
- `paypal_checkout_core_ecosystem`: Checkout session and buyer approval metadata.
- `paypal_disputes_core_ecosystem`: Dispute, evidence and resolution metadata.
- `paypal_identity_oauth_core_ecosystem`: PayPal identity and OAuth consent boundary.
- `paypal_invoicing_core_ecosystem`: Invoice lifecycle and payment status metadata.
- `paypal_merchant_onboarding_core_ecosystem`: Merchant eligibility and onboarding readiness metadata.
- `paypal_orders_core_ecosystem`: Order identity and lifecycle metadata.
- `paypal_payments_core_ecosystem`: Payment intent, capture and refund capability metadata.
- `paypal_payouts_core_ecosystem`: Payout batch and recipient metadata.
- `paypal_subscriptions_core_ecosystem`: Subscription lifecycle and plan linkage metadata.
- `paypal_transaction_search_core_ecosystem`: Transaction search and reconciliation references.
- `paypal_vault_payment_methods_core_ecosystem`: Vaulted payment method reference metadata.
- `paypal_webhooks_core_ecosystem`: Webhook event type and verification policy metadata.

## 2468 master catalogue

The canonical file `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` is read on demand and never modified by this package. The existing finance/payment-gateway registry already identifies `paypal_payment_core_ecosystem`. PayPal Core references that entry and the payment/billing domain metadata; it does not add numbered taxonomy entries or change the 2468 target.

## Security and layer boundaries

- OAuth consent, token exchange, SDK clients and HTTP requests belong to the PayPal API layer.
- Payment capture, refunds, payouts, billing changes and dispute actions require separate authenticated API authorization, idempotency and audit controls.
- Credentials and webhook signing secrets remain in an external secret manager; this Core stores only opaque references.
- Webhook signature verification and event processing belong to the API/runtime layer; Core catalogs event metadata only.
- Product registration does not prove merchant approval, account entitlement, API access or live connectivity.
- Report a live connection only after deployment authentication and provider smoke tests succeed.
