"""Stripe provider API ecosystem catalog and service-family registry."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER_ID = "stripe"
PROVIDER_NAME = "STRIPE API ECOSYSTEM"
PROVIDER_VENDOR = "Stripe"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem"

STRIPE_SERVICE_ECOSYSTEMS = [
    {"id":"accounts","name":"STRIPE ACCOUNTS API ECOSYSTEM","folder":"stripe_accounts_api_ecosystem","status":"catalog_only"},
    {"id":"billing","name":"STRIPE BILLING API ECOSYSTEM","folder":"stripe_billing_api_ecosystem","status":"catalog_only"},
    {"id":"checkout","name":"STRIPE CHECKOUT API ECOSYSTEM","folder":"stripe_checkout_api_ecosystem","status":"catalog_only"},
    {"id":"customers","name":"STRIPE CUSTOMERS API ECOSYSTEM","folder":"stripe_customers_api_ecosystem","status":"catalog_only"},
    {"id":"disputes","name":"STRIPE DISPUTES API ECOSYSTEM","folder":"stripe_disputes_api_ecosystem","status":"catalog_only"},
    {"id":"events","name":"STRIPE EVENTS API ECOSYSTEM","folder":"stripe_events_api_ecosystem","status":"catalog_only"},
    {"id":"fraud","name":"STRIPE FRAUD / RADAR API ECOSYSTEM","folder":"stripe_fraud_api_ecosystem","status":"catalog_only"},
    {"id":"issuing","name":"STRIPE ISSUING API ECOSYSTEM","folder":"stripe_issuing_api_ecosystem","status":"catalog_only"},
    {"id":"payment_intents","name":"STRIPE PAYMENT INTENTS API ECOSYSTEM","folder":"stripe_payment_intents_api_ecosystem","status":"catalog_only"},
    {"id":"payment_links","name":"STRIPE PAYMENT LINKS API ECOSYSTEM","folder":"stripe_payment_links_api_ecosystem","status":"catalog_only"},
    {"id":"payment_methods","name":"STRIPE PAYMENT METHODS API ECOSYSTEM","folder":"stripe_payment_methods_api_ecosystem","status":"catalog_only"},
    {"id":"payouts","name":"STRIPE PAYOUTS API ECOSYSTEM","folder":"stripe_payouts_api_ecosystem","status":"catalog_only"},
    {"id":"products_prices","name":"STRIPE PRODUCTS AND PRICES API ECOSYSTEM","folder":"stripe_products_prices_api_ecosystem","status":"catalog_only"},
    {"id":"refunds","name":"STRIPE REFUNDS API ECOSYSTEM","folder":"stripe_refunds_api_ecosystem","status":"catalog_only"},
    {"id":"reporting","name":"STRIPE REPORTING API ECOSYSTEM","folder":"stripe_reporting_api_ecosystem","status":"catalog_only"},
    {"id":"subscriptions","name":"STRIPE SUBSCRIPTIONS API ECOSYSTEM","folder":"stripe_subscriptions_api_ecosystem","status":"catalog_only"},
    {"id":"tax","name":"STRIPE TAX API ECOSYSTEM","folder":"stripe_tax_api_ecosystem","status":"catalog_only"},
    {"id":"terminal","name":"STRIPE TERMINAL API ECOSYSTEM","folder":"stripe_terminal_api_ecosystem","status":"catalog_only"},
    {"id":"treasury","name":"STRIPE TREASURY API ECOSYSTEM","folder":"stripe_treasury_api_ecosystem","status":"catalog_only"},
    {"id":"webhooks","name":"STRIPE WEBHOOKS API ECOSYSTEM","folder":"stripe_webhooks_api_ecosystem","status":"catalog_only"},
    {"id":"climate","name":"STRIPE CLIMATE API ECOSYSTEM","folder":"stripe_climate_api_ecosystem","status":"catalog_only"},
    {"id":"crypto_onramp","name":"STRIPE CRYPTO ONRAMP API ECOSYSTEM","folder":"stripe_crypto_onramp_api_ecosystem","status":"catalog_only"},
]

PROVIDER_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "vendor": PROVIDER_VENDOR,
    "families": ["BUSINESS", "PAYMENT"],
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "SCAFFOLD_BUILT_LIVE_API_UNVERIFIED",
    "authentication": {
        "method": "BEARER_SECRET_KEY",
        "credential_source": "environment_or_managed_secret_store",
        "environment": ["STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET", "STRIPE_API_VERSION"],
        "secrets_in_repository": False,
    },
    "endpoints": {
        "api_base_url": "https://api.stripe.com",
        "test_mode": "Use Stripe test-mode secret keys",
        "live_mode": "Use live keys only after business, account and compliance checks",
    },
    "service_ecosystems": STRIPE_SERVICE_ECOSYSTEMS,
    "security": {
        "verify_webhook_signatures": True,
        "use_idempotency_keys_for_writes": True,
        "never_log_secrets_or_payment_credentials": True,
        "require_https": True,
    },
    "live_connection_verified": False,
    "documentation": [
        "https://docs.stripe.com/api",
        "https://docs.stripe.com/keys",
        "https://docs.stripe.com/webhooks",
    ],
}

def get_stripe_api_ecosystem() -> dict[str, Any]:
    return deepcopy(PROVIDER_API_ECOSYSTEM)

def list_stripe_service_ecosystems() -> dict[str, object]:
    items = [dict(item) for item in STRIPE_SERVICE_ECOSYSTEMS]
    return {
        "success": True,
        "provider": PROVIDER_NAME,
        "count": len(items),
        "live_connection_verified": False,
        "ecosystems": items,
    }

__all__ = [
    "PROVIDER_ID", "PROVIDER_NAME", "PROVIDER_VENDOR", "PROVIDER_CATALOG_PATH",
    "PROVIDER_API_ECOSYSTEM", "STRIPE_SERVICE_ECOSYSTEMS",
    "get_stripe_api_ecosystem", "list_stripe_service_ecosystems",
]
