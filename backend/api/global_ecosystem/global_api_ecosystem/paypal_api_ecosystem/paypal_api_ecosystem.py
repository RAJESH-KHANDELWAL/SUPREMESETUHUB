"""PayPal provider API ecosystem catalog and service-family registry.

Metadata only. A catalog entry does not imply credentials, account approval,
webhook configuration, or live API connectivity.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


PROVIDER_ID = "paypal"
PROVIDER_NAME = "GLOBAL PAYPAL API ECOSYSTEM"
PROVIDER_VENDOR = "PayPal"
PROVIDER_CATALOG_PATH = (
    "backend/api/global_ecosystem/global_api_ecosystem/"
    "paypal_api_ecosystem"
)

PAYPAL_SERVICE_ECOSYSTEMS = [
    {"id": "checkout", "name": "GLOBAL PAYPAL CHECKOUT API ECOSYSTEM", "folder": "paypal_checkout_api_ecosystem", "status": "catalog_only"},
    {"id": "orders", "name": "GLOBAL PAYPAL ORDERS API ECOSYSTEM", "folder": "paypal_orders_api_ecosystem", "status": "catalog_only"},
    {"id": "payments", "name": "GLOBAL PAYPAL PAYMENTS API ECOSYSTEM", "folder": "paypal_payments_api_ecosystem", "status": "catalog_only"},
    {"id": "payouts", "name": "GLOBAL PAYPAL PAYOUTS API ECOSYSTEM", "folder": "paypal_payouts_api_ecosystem", "status": "catalog_only"},
    {"id": "subscriptions", "name": "GLOBAL PAYPAL SUBSCRIPTIONS API ECOSYSTEM", "folder": "paypal_subscriptions_api_ecosystem", "status": "catalog_only"},
    {"id": "invoicing", "name": "GLOBAL PAYPAL INVOICING API ECOSYSTEM", "folder": "paypal_invoicing_api_ecosystem", "status": "catalog_only"},
    {"id": "billing_plans", "name": "GLOBAL PAYPAL BILLING PLANS API ECOSYSTEM", "folder": "paypal_billing_plans_api_ecosystem", "status": "catalog_only"},
    {"id": "vault_payment_methods", "name": "GLOBAL PAYPAL VAULT PAYMENT METHODS API ECOSYSTEM", "folder": "paypal_vault_payment_methods_api_ecosystem", "status": "catalog_only"},
    {"id": "webhooks", "name": "GLOBAL PAYPAL WEBHOOKS API ECOSYSTEM", "folder": "paypal_webhooks_api_ecosystem", "status": "catalog_only"},
    {"id": "identity_oauth", "name": "GLOBAL PAYPAL IDENTITY AND OAUTH API ECOSYSTEM", "folder": "paypal_identity_oauth_api_ecosystem", "status": "catalog_only"},
    {"id": "disputes", "name": "GLOBAL PAYPAL DISPUTES API ECOSYSTEM", "folder": "paypal_disputes_api_ecosystem", "status": "catalog_only"},
    {"id": "transaction_search", "name": "GLOBAL PAYPAL TRANSACTION SEARCH API ECOSYSTEM", "folder": "paypal_transaction_search_api_ecosystem", "status": "catalog_only"},
    {"id": "merchant_onboarding", "name": "GLOBAL PAYPAL MERCHANT ONBOARDING API ECOSYSTEM", "folder": "paypal_merchant_onboarding_api_ecosystem", "status": "catalog_only"},
]

PROVIDER_API_ECOSYSTEM: dict[str, Any] = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "vendor": PROVIDER_VENDOR,
    "families": ["BUSINESS", "PAYMENT"],
    "scope": "Checkout, orders, payments, subscriptions, payouts, invoicing, disputes and merchant APIs subject to account eligibility and regional availability.",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "implementation_status": "CATALOG_EXPANDED_LIVE_API_UNVERIFIED",
    "live_connection_verified": False,
    "provider_catalog_path": PROVIDER_CATALOG_PATH,
    "authentication": {
        "method": "PAYPAL_OAUTH_2_CLIENT_CREDENTIALS",
        "credential_source": "environment_or_managed_secret_store",
        "required_environment": ["PAYPAL_CLIENT_ID", "PAYPAL_CLIENT_SECRET"],
        "token_endpoint": "https://api-m.paypal.com/v1/oauth2/token",
        "sandbox_token_endpoint": "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        "secrets_in_repository": False,
    },
    "endpoint_strategy": {
        "production_base_url": "https://api-m.paypal.com",
        "sandbox_base_url": "https://api-m.sandbox.paypal.com",
        "environment_selection": "explicit_configuration",
        "never_send_sandbox_credentials_to_production": True,
    },
    "service_ecosystems": PAYPAL_SERVICE_ECOSYSTEMS,
    "integration_requirements": [
        "official_api_reference_review",
        "environment_separated_credentials",
        "oauth_token_lifecycle_and_expiry_handling",
        "webhook_signature_verification",
        "idempotency_for_supported_mutations",
        "currency_and_country_capability_checks",
        "timeouts_retries_and_rate_limit_handling",
        "unit_tests_with_mocked_responses",
        "opt_in_sandbox_integration_tests",
    ],
    "security": {
        "never_log_client_secrets_or_access_tokens": True,
        "verify_webhook_signatures": True,
        "use_idempotency_for_supported_payment_requests": True,
        "live_connection_requires_successful_authenticated_api_test": True,
    },
    "documentation": [
        "https://developer.paypal.com/api/rest/",
        "https://developer.paypal.com/api/rest/authentication/",
        "https://developer.paypal.com/api/rest/webhooks/",
    ],
}

PAYPAL_API_ECOSYSTEM = PROVIDER_API_ECOSYSTEM


def get_paypal_api_ecosystem() -> dict[str, Any]:
    """Return an isolated copy of PayPal provider metadata."""
    return deepcopy(PROVIDER_API_ECOSYSTEM)


def list_paypal_api_ecosystems() -> dict[str, object]:
    """List PayPal service-family catalogs without claiming live connectivity."""
    children = [dict(item) for item in PAYPAL_SERVICE_ECOSYSTEMS]
    return {
        "success": True,
        "provider": PROVIDER_NAME,
        "status": PROVIDER_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


__all__ = [
    "PAYPAL_API_ECOSYSTEM",
    "PAYPAL_SERVICE_ECOSYSTEMS",
    "PROVIDER_API_ECOSYSTEM",
    "PROVIDER_CATALOG_PATH",
    "PROVIDER_ID",
    "PROVIDER_NAME",
    "PROVIDER_VENDOR",
    "get_paypal_api_ecosystem",
    "list_paypal_api_ecosystems",
]
