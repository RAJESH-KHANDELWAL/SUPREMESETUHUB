"""Stripe Core catalog: orchestration metadata and API-layer boundaries.

The Core layer registers capabilities and delegates transport to the API layer.
It does not hold secret keys, create charges directly, or claim live connectivity.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

STRIPE_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "STRIPE-CORE-ECOSYSTEM",
    "name": "STRIPE CORE ECOSYSTEM",
    "provider": "stripe",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
    "capabilities": [
        "STRIPE_PROVIDER_REGISTRY",
        "PAYMENT_LIFECYCLE_ORCHESTRATION",
        "BILLING_AND_SUBSCRIPTION_ORCHESTRATION",
        "CUSTOMER_AND_PAYMENT_METHOD_REFERENCES",
        "PAYOUT_AND_RECONCILIATION_METADATA",
        "DISPUTE_AND_REFUND_WORKFLOWS",
        "WEBHOOK_EVENT_ROUTING",
        "IDEMPOTENCY_POLICY",
        "TENANT_SCOPED_CONFIGURATION",
        "SECRET_REFERENCE_BOUNDARY",
        "AUDIT_AND_HEALTH_METADATA",
    ],
    "security": {
        "secret_management": "API layer reads secret from environment/managed secret store; Core stores references only",
        "never_store_secret_key_in_catalog": True,
        "webhook_signature_verification_required": True,
        "idempotency_required_for_payment_writes": True,
        "pci_scope_minimization": True,
        "tenant_isolation_required": True,
    },
    "children": [
        {"ecosystem_id":"STRIPE-ACCOUNTS-CORE-ECOSYSTEM","name":"STRIPE ACCOUNTS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_accounts_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_accounts_core_ecosystem","module":"stripe_accounts_core_ecosystem","api_family":"accounts","capabilities":["CONNECT_ACCOUNT_METADATA","ONBOARDING_STATUS"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-BILLING-CORE-ECOSYSTEM","name":"STRIPE BILLING CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_billing_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_billing_core_ecosystem","module":"stripe_billing_core_ecosystem","api_family":"billing","capabilities":["INVOICE_LIFECYCLE","BILLING_CONFIGURATION"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-CHECKOUT-CORE-ECOSYSTEM","name":"STRIPE CHECKOUT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_checkout_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_checkout_core_ecosystem","module":"stripe_checkout_core_ecosystem","api_family":"checkout","capabilities":["CHECKOUT_SESSION_ORCHESTRATION","SUCCESS_CANCEL_RETURN_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-CUSTOMERS-CORE-ECOSYSTEM","name":"STRIPE CUSTOMERS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_customers_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_customers_core_ecosystem","module":"stripe_customers_core_ecosystem","api_family":"customers","capabilities":["CUSTOMER_REFERENCE","CUSTOMER_LIFECYCLE"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-DISPUTES-CORE-ECOSYSTEM","name":"STRIPE DISPUTES CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_disputes_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_disputes_core_ecosystem","module":"stripe_disputes_core_ecosystem","api_family":"disputes","capabilities":["DISPUTE_STATUS","EVIDENCE_WORKFLOW_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-EVENTS-CORE-ECOSYSTEM","name":"STRIPE EVENTS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_events_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_events_core_ecosystem","module":"stripe_events_core_ecosystem","api_family":"events","capabilities":["EVENT_DISCOVERY","EVENT_DEDUPLICATION"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-FRAUD-CORE-ECOSYSTEM","name":"STRIPE FRAUD CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_fraud_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_fraud_core_ecosystem","module":"stripe_fraud_core_ecosystem","api_family":"fraud","capabilities":["RISK_METADATA","REVIEW_WORKFLOW_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-ISSUING-CORE-ECOSYSTEM","name":"STRIPE ISSUING CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_issuing_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_issuing_core_ecosystem","module":"stripe_issuing_core_ecosystem","api_family":"issuing","capabilities":["ISSUING_ELIGIBILITY_METADATA","CARDHOLDER_LIFECYCLE_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-PAYMENT-INTENTS-CORE-ECOSYSTEM","name":"STRIPE PAYMENT INTENTS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_payment_intents_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_payment_intents_core_ecosystem","module":"stripe_payment_intents_core_ecosystem","api_family":"payment_intents","capabilities":["PAYMENT_INTENT_STATE","PAYMENT_CONFIRMATION_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-PAYMENT-LINKS-CORE-ECOSYSTEM","name":"STRIPE PAYMENT LINKS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_payment_links_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_payment_links_core_ecosystem","module":"stripe_payment_links_core_ecosystem","api_family":"payment_links","capabilities":["PAYMENT_LINK_METADATA","LINK_STATUS"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-PAYMENT-METHODS-CORE-ECOSYSTEM","name":"STRIPE PAYMENT METHODS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_payment_methods_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_payment_methods_core_ecosystem","module":"stripe_payment_methods_core_ecosystem","api_family":"payment_methods","capabilities":["PAYMENT_METHOD_REFERENCE","SETUP_INTENT_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-PAYOUTS-CORE-ECOSYSTEM","name":"STRIPE PAYOUTS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_payouts_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_payouts_core_ecosystem","module":"stripe_payouts_core_ecosystem","api_family":"payouts","capabilities":["PAYOUT_STATUS","BALANCE_RECONCILIATION_REFERENCE"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-PRODUCTS-PRICES-CORE-ECOSYSTEM","name":"STRIPE PRODUCTS AND PRICES CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_products_prices_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_products_prices_core_ecosystem","module":"stripe_products_prices_core_ecosystem","api_family":"products_prices","capabilities":["PRODUCT_CATALOG_METADATA","PRICE_REFERENCE"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-REFUNDS-CORE-ECOSYSTEM","name":"STRIPE REFUNDS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_refunds_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_refunds_core_ecosystem","module":"stripe_refunds_core_ecosystem","api_family":"refunds","capabilities":["REFUND_ELIGIBILITY_METADATA","REFUND_LIFECYCLE"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-REPORTING-CORE-ECOSYSTEM","name":"STRIPE REPORTING CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_reporting_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_reporting_core_ecosystem","module":"stripe_reporting_core_ecosystem","api_family":"reporting","capabilities":["REPORTING_CONFIGURATION","RECONCILIATION_METADATA"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-SUBSCRIPTIONS-CORE-ECOSYSTEM","name":"STRIPE SUBSCRIPTIONS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_subscriptions_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_subscriptions_core_ecosystem","module":"stripe_subscriptions_core_ecosystem","api_family":"subscriptions","capabilities":["SUBSCRIPTION_LIFECYCLE","RENEWAL_STATUS"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-TAX-CORE-ECOSYSTEM","name":"STRIPE TAX CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_tax_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_tax_core_ecosystem","module":"stripe_tax_core_ecosystem","api_family":"tax","capabilities":["TAX_CALCULATION_BOUNDARY","TAX_CONFIGURATION_METADATA"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-TERMINAL-CORE-ECOSYSTEM","name":"STRIPE TERMINAL CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_terminal_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_terminal_core_ecosystem","module":"stripe_terminal_core_ecosystem","api_family":"terminal","capabilities":["READER_LOCATION_METADATA","IN_PERSON_PAYMENT_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-TREASURY-CORE-ECOSYSTEM","name":"STRIPE TREASURY CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_treasury_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_treasury_core_ecosystem","module":"stripe_treasury_core_ecosystem","api_family":"treasury","capabilities":["FINANCIAL_ACCOUNT_METADATA","TREASURY_ELIGIBILITY_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-WEBHOOKS-CORE-ECOSYSTEM","name":"STRIPE WEBHOOKS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_webhooks_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_webhooks_core_ecosystem","module":"stripe_webhooks_core_ecosystem","api_family":"webhooks","capabilities":["WEBHOOK_EVENT_ROUTING","SIGNATURE_STATUS_METADATA"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-CLIMATE-CORE-ECOSYSTEM","name":"STRIPE CLIMATE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_climate_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_climate_core_ecosystem","module":"stripe_climate_core_ecosystem","api_family":"climate","capabilities":["CLIMATE_ORDER_METADATA"],"status":"CORE_CATALOG_ONLY","connected":False},
        {"ecosystem_id":"STRIPE-CRYPTO-ONRAMP-CORE-ECOSYSTEM","name":"STRIPE CRYPTO ONRAMP CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"STRIPE-CORE-ECOSYSTEM","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem/stripe_crypto_onramp_api_ecosystem","core_module":"backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem/stripe_crypto_onramp_core_ecosystem","module":"stripe_crypto_onramp_core_ecosystem","api_family":"crypto_onramp","capabilities":["ONRAMP_ELIGIBILITY_METADATA","TRANSACTION_STATUS_BOUNDARY"],"status":"CORE_CATALOG_ONLY","connected":False},
    ],
    "live_connection_verified": False,
}

def get_stripe_core_catalog() -> dict[str, Any]:
    """Return an independent copy of the Stripe Core registry catalog."""
    return deepcopy(STRIPE_CORE_ECOSYSTEM)

def list_stripe_core_modules(include_disabled: bool = False) -> list[dict[str, Any]]:
    """Return provider-specific Core modules without secrets or payment data."""
    modules = deepcopy(STRIPE_CORE_ECOSYSTEM["children"])
    if include_disabled:
        return modules
    return [module for module in modules if module.get("status") != "DISABLED"]

__all__ = ["STRIPE_CORE_ECOSYSTEM", "get_stripe_core_catalog", "list_stripe_core_modules"]
