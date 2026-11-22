"""Canonical PayPal provider and product Core inventory."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, PROVIDER, PARENT_ECOSYSTEM_ID
PAYPAL_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "PAYPAL-CORE-ECOSYSTEM",
    "name": "PAYPAL CORE ECOSYSTEM",
    "provider": "paypal",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": true,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem",
    "master_catalog_ref": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
    "master_catalog_access_mode": "READ_ONLY_ON_DEMAND",
    "capabilities": [
        "PAYPAL_PROVIDER_REGISTRY",
        "PAYPAL_PRODUCT_DISCOVERY",
        "PAYPAL_MERCHANT_GOVERNANCE",
        "PAYPAL_PAYMENT_LIFECYCLE_METADATA",
        "TENANT_SCOPED_CONNECTION_METADATA",
        "SECRET_REFERENCE_BOUNDARY",
        "WEBHOOK_POLICY_METADATA"
    ],
    "children": [
        {
            "ecosystem_id": "PAYPAL-BILLING-PLANS-CORE-ECOSYSTEM",
            "name": "PAYPAL BILLING PLANS CORE ECOSYSTEM",
            "package": "paypal_billing_plans_core_ecosystem",
            "manager_class": "PayPalBillingPlansCoreManager",
            "description": "Billing plans and pricing metadata",
            "domain_id": "BILLING_SUBSCRIPTIONS_AND_INVOICING",
            "capabilities": [
                "BILLING_PLAN_DISCOVERY",
                "BILLING_PLAN_METADATA"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_billing_plans_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_billing_plans_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-CHECKOUT-CORE-ECOSYSTEM",
            "name": "PAYPAL CHECKOUT CORE ECOSYSTEM",
            "package": "paypal_checkout_core_ecosystem",
            "manager_class": "PayPalCheckoutCoreManager",
            "description": "Checkout session and buyer approval metadata",
            "domain_id": "CHECKOUT_ORDERS_AND_PAYMENT_ACCEPTANCE",
            "capabilities": [
                "CHECKOUT_SESSION_METADATA",
                "BUYER_APPROVAL_BOUNDARY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_checkout_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_checkout_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-DISPUTES-CORE-ECOSYSTEM",
            "name": "PAYPAL DISPUTES CORE ECOSYSTEM",
            "package": "paypal_disputes_core_ecosystem",
            "manager_class": "PayPalDisputesCoreManager",
            "description": "Dispute, evidence and resolution metadata",
            "domain_id": "DISPUTES_AND_RISK",
            "capabilities": [
                "DISPUTE_CASE_METADATA",
                "EVIDENCE_SUBMISSION_BOUNDARY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_disputes_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_disputes_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-IDENTITY-OAUTH-CORE-ECOSYSTEM",
            "name": "PAYPAL IDENTITY OAUTH CORE ECOSYSTEM",
            "package": "paypal_identity_oauth_core_ecosystem",
            "manager_class": "PayPalIdentityOAuthCoreManager",
            "description": "PayPal identity and OAuth consent boundary",
            "domain_id": "IDENTITY_AND_MERCHANT_GOVERNANCE",
            "capabilities": [
                "OAUTH_CONFIGURATION_METADATA",
                "IDENTITY_CONNECTION_STATUS"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_identity_oauth_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_identity_oauth_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-INVOICING-CORE-ECOSYSTEM",
            "name": "PAYPAL INVOICING CORE ECOSYSTEM",
            "package": "paypal_invoicing_core_ecosystem",
            "manager_class": "PayPalInvoicingCoreManager",
            "description": "Invoice lifecycle and payment status metadata",
            "domain_id": "BILLING_SUBSCRIPTIONS_AND_INVOICING",
            "capabilities": [
                "INVOICE_METADATA",
                "INVOICE_STATUS_DISCOVERY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_invoicing_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_invoicing_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-MERCHANT-ONBOARDING-CORE-ECOSYSTEM",
            "name": "PAYPAL MERCHANT ONBOARDING CORE ECOSYSTEM",
            "package": "paypal_merchant_onboarding_core_ecosystem",
            "manager_class": "PayPalMerchantOnboardingCoreManager",
            "description": "Merchant eligibility and onboarding readiness metadata",
            "domain_id": "IDENTITY_AND_MERCHANT_GOVERNANCE",
            "capabilities": [
                "MERCHANT_ONBOARDING_STATUS",
                "MERCHANT_ELIGIBILITY_METADATA"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_merchant_onboarding_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_merchant_onboarding_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-ORDERS-CORE-ECOSYSTEM",
            "name": "PAYPAL ORDERS CORE ECOSYSTEM",
            "package": "paypal_orders_core_ecosystem",
            "manager_class": "PayPalOrdersCoreManager",
            "description": "Order identity and lifecycle metadata",
            "domain_id": "CHECKOUT_ORDERS_AND_PAYMENT_ACCEPTANCE",
            "capabilities": [
                "ORDER_METADATA",
                "ORDER_LIFECYCLE_DISCOVERY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_orders_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_orders_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-PAYMENTS-CORE-ECOSYSTEM",
            "name": "PAYPAL PAYMENTS CORE ECOSYSTEM",
            "package": "paypal_payments_core_ecosystem",
            "manager_class": "PayPalPaymentsCoreManager",
            "description": "Payment intent, capture and refund capability metadata",
            "domain_id": "CHECKOUT_ORDERS_AND_PAYMENT_ACCEPTANCE",
            "capabilities": [
                "PAYMENT_METADATA",
                "CAPTURE_BOUNDARY",
                "REFUND_BOUNDARY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_payments_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_payments_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-PAYOUTS-CORE-ECOSYSTEM",
            "name": "PAYPAL PAYOUTS CORE ECOSYSTEM",
            "package": "paypal_payouts_core_ecosystem",
            "manager_class": "PayPalPayoutsCoreManager",
            "description": "Payout batch and recipient metadata",
            "domain_id": "PAYOUTS_AND_SETTLEMENT",
            "capabilities": [
                "PAYOUT_BATCH_METADATA",
                "PAYOUT_RECIPIENT_METADATA"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_payouts_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_payouts_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-SUBSCRIPTIONS-CORE-ECOSYSTEM",
            "name": "PAYPAL SUBSCRIPTIONS CORE ECOSYSTEM",
            "package": "paypal_subscriptions_core_ecosystem",
            "manager_class": "PayPalSubscriptionsCoreManager",
            "description": "Subscription lifecycle and plan linkage metadata",
            "domain_id": "BILLING_SUBSCRIPTIONS_AND_INVOICING",
            "capabilities": [
                "SUBSCRIPTION_METADATA",
                "SUBSCRIPTION_LIFECYCLE"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_subscriptions_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_subscriptions_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-TRANSACTION-SEARCH-CORE-ECOSYSTEM",
            "name": "PAYPAL TRANSACTION SEARCH CORE ECOSYSTEM",
            "package": "paypal_transaction_search_core_ecosystem",
            "manager_class": "PayPalTransactionSearchCoreManager",
            "description": "Transaction search and reconciliation references",
            "domain_id": "PAYOUTS_AND_SETTLEMENT",
            "capabilities": [
                "TRANSACTION_SEARCH_METADATA",
                "RECONCILIATION_REFERENCE"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_transaction_search_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_transaction_search_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-VAULT-PAYMENT-METHODS-CORE-ECOSYSTEM",
            "name": "PAYPAL VAULT PAYMENT METHODS CORE ECOSYSTEM",
            "package": "paypal_vault_payment_methods_core_ecosystem",
            "manager_class": "PayPalVaultPaymentMethodsCoreManager",
            "description": "Vaulted payment method reference metadata",
            "domain_id": "VAULT_AND_WEBHOOKS",
            "capabilities": [
                "VAULT_REFERENCE_METADATA",
                "PAYMENT_METHOD_LIFECYCLE"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_vault_payment_methods_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_vault_payment_methods_core_ecosystem"
        },
        {
            "ecosystem_id": "PAYPAL-WEBHOOKS-CORE-ECOSYSTEM",
            "name": "PAYPAL WEBHOOKS CORE ECOSYSTEM",
            "package": "paypal_webhooks_core_ecosystem",
            "manager_class": "PayPalWebhooksCoreManager",
            "description": "Webhook event type and verification policy metadata",
            "domain_id": "VAULT_AND_WEBHOOKS",
            "capabilities": [
                "WEBHOOK_EVENT_CATALOG",
                "WEBHOOK_VERIFICATION_BOUNDARY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": true,
            "connected": false,
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/paypal_api_ecosystem/paypal_webhooks_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/paypal_core_ecosystem/paypal_webhooks_core_ecosystem"
        }
    ]
}
def get_paypal_core_catalog() -> dict[str, Any]:
    return deepcopy(PAYPAL_CORE_ECOSYSTEM)
