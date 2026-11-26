"""PayPal domain taxonomy derived from the registered product inventory."""
from __future__ import annotations
from collections import Counter
from typing import Any
from .product_catalog import list_paypal_products
DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
    "IDENTITY_AND_MERCHANT_GOVERNANCE": {
        "name": "Identity and Merchant Governance",
        "purpose": "Merchant identity, OAuth configuration metadata, onboarding eligibility and tenant-scoped connection references.",
        "package_ids": [
            "PAYPAL-IDENTITY-OAUTH-CORE-ECOSYSTEM",
            "PAYPAL-MERCHANT-ONBOARDING-CORE-ECOSYSTEM"
        ]
    },
    "CHECKOUT_ORDERS_AND_PAYMENT_ACCEPTANCE": {
        "name": "Checkout, Orders and Payment Acceptance",
        "purpose": "Checkout and order lifecycle metadata, payment capture and buyer approval boundaries.",
        "package_ids": [
            "PAYPAL-CHECKOUT-CORE-ECOSYSTEM",
            "PAYPAL-ORDERS-CORE-ECOSYSTEM",
            "PAYPAL-PAYMENTS-CORE-ECOSYSTEM"
        ]
    },
    "BILLING_SUBSCRIPTIONS_AND_INVOICING": {
        "name": "Billing, Subscriptions and Invoicing",
        "purpose": "Billing plan, recurring subscription and invoice metadata.",
        "package_ids": [
            "PAYPAL-BILLING-PLANS-CORE-ECOSYSTEM",
            "PAYPAL-SUBSCRIPTIONS-CORE-ECOSYSTEM",
            "PAYPAL-INVOICING-CORE-ECOSYSTEM"
        ]
    },
    "PAYOUTS_AND_SETTLEMENT": {
        "name": "Payouts and Settlement",
        "purpose": "Payout batches, transaction discovery and reconciliation references.",
        "package_ids": [
            "PAYPAL-PAYOUTS-CORE-ECOSYSTEM",
            "PAYPAL-TRANSACTION-SEARCH-CORE-ECOSYSTEM"
        ]
    },
    "DISPUTES_AND_RISK": {
        "name": "Disputes and Risk",
        "purpose": "Dispute lifecycle, evidence metadata and risk-sensitive operation boundaries.",
        "package_ids": [
            "PAYPAL-DISPUTES-CORE-ECOSYSTEM"
        ]
    },
    "VAULT_AND_WEBHOOKS": {
        "name": "Vault and Webhooks",
        "purpose": "Vaulted payment method references and webhook event verification metadata.",
        "package_ids": [
            "PAYPAL-VAULT-PAYMENT-METHODS-CORE-ECOSYSTEM",
            "PAYPAL-WEBHOOKS-CORE-ECOSYSTEM"
        ]
    }
}
def list_paypal_domain_inventory() -> list[dict[str, Any]]:
    counts = Counter(item["domain_id"] for item in list_paypal_products())
    return [{"domain_id": key, **value, "product_count": counts[key]} for key, value in DOMAIN_DEFINITIONS.items()]
def paypal_domain_summary() -> dict[str, Any]:
    inventory = list_paypal_domain_inventory()
    return {"count": len(inventory), "domains": inventory, "product_count": sum(item["product_count"] for item in inventory)}
