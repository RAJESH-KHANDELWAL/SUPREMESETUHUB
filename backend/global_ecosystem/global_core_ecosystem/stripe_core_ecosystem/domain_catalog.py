"""Stripe Core domain taxonomy derived from the canonical 22-family catalog."""
from __future__ import annotations

from collections import Counter
from typing import Any

from .catalog import list_stripe_core_modules

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "PROVIDER_GOVERNANCE_AND_ACCOUNTS": {
        "name": "Provider Governance and Accounts",
        "purpose": "Stripe provider identity, connected-account metadata and onboarding readiness.",
    },
    "CUSTOMER_AND_PAYMENT_ACCEPTANCE": {
        "name": "Customers and Payment Acceptance",
        "purpose": "Customer references, checkout, payment intents, payment links and payment methods.",
    },
    "BILLING_AND_COMMERCE": {
        "name": "Billing, Subscriptions and Commerce",
        "purpose": "Invoices, subscriptions, products, prices and tax metadata.",
    },
    "FINANCIAL_OPERATIONS": {
        "name": "Financial Operations and Reconciliation",
        "purpose": "Payouts, treasury, reporting and reconciliation metadata.",
    },
    "RISK_AND_FINANCIAL_PROTECTION": {
        "name": "Risk, Disputes and Financial Protection",
        "purpose": "Fraud signals, disputes, refunds and issuing eligibility boundaries.",
    },
    "EVENTS_AND_INTEGRATION_GOVERNANCE": {
        "name": "Events and Integration Governance",
        "purpose": "Event discovery, webhook routing metadata and integration lifecycle boundaries.",
    },
    "SPECIALTY_AND_EMERGING_SERVICES": {
        "name": "Specialty and Emerging Services",
        "purpose": "Climate and crypto onramp eligibility and service metadata.",
    },
}

FAMILY_TO_DOMAIN = {
    "accounts": "PROVIDER_GOVERNANCE_AND_ACCOUNTS",
    "customers": "CUSTOMER_AND_PAYMENT_ACCEPTANCE",
    "checkout": "CUSTOMER_AND_PAYMENT_ACCEPTANCE",
    "payment_intents": "CUSTOMER_AND_PAYMENT_ACCEPTANCE",
    "payment_links": "CUSTOMER_AND_PAYMENT_ACCEPTANCE",
    "payment_methods": "CUSTOMER_AND_PAYMENT_ACCEPTANCE",
    "billing": "BILLING_AND_COMMERCE",
    "subscriptions": "BILLING_AND_COMMERCE",
    "products_prices": "BILLING_AND_COMMERCE",
    "tax": "BILLING_AND_COMMERCE",
    "payouts": "FINANCIAL_OPERATIONS",
    "treasury": "FINANCIAL_OPERATIONS",
    "reporting": "FINANCIAL_OPERATIONS",
    "fraud": "RISK_AND_FINANCIAL_PROTECTION",
    "disputes": "RISK_AND_FINANCIAL_PROTECTION",
    "refunds": "RISK_AND_FINANCIAL_PROTECTION",
    "issuing": "RISK_AND_FINANCIAL_PROTECTION",
    "events": "EVENTS_AND_INTEGRATION_GOVERNANCE",
    "webhooks": "EVENTS_AND_INTEGRATION_GOVERNANCE",
    "climate": "SPECIALTY_AND_EMERGING_SERVICES",
    "crypto_onramp": "SPECIALTY_AND_EMERGING_SERVICES",
}


def list_stripe_domain_inventory() -> list[dict[str, Any]]:
    inventory = []
    for module in list_stripe_core_modules(include_disabled=True):
        domain_id = FAMILY_TO_DOMAIN.get(module.get("api_family", ""), "SPECIALTY_AND_EMERGING_SERVICES")
        inventory.append({
            **module,
            "core_domain_id": domain_id,
            "core_domain_name": DOMAIN_DEFINITIONS[domain_id]["name"],
            "domain_assignment": "EXPLICIT_API_FAMILY_RULE" if module.get("api_family") in FAMILY_TO_DOMAIN else "REVIEW_REQUIRED",
        })
    return inventory


def stripe_domain_summary() -> dict[str, Any]:
    inventory = list_stripe_domain_inventory()
    counts = Counter(item["core_domain_id"] for item in inventory)
    return {
        "success": True,
        "domain_count": len(DOMAIN_DEFINITIONS),
        "service_family_count": len(inventory),
        "assigned_service_family_count": sum(item["domain_assignment"] == "EXPLICIT_API_FAMILY_RULE" for item in inventory),
        "domains": [
            {"domain_id": domain_id, **definition, "service_family_count": counts.get(domain_id, 0)}
            for domain_id, definition in DOMAIN_DEFINITIONS.items()
        ],
        "live_connections_verified": 0,
        "note": "Domain classification is metadata only; it does not establish Stripe API availability, account eligibility or live connectivity.",
    }


__all__ = ["DOMAIN_DEFINITIONS", "FAMILY_TO_DOMAIN", "list_stripe_domain_inventory", "stripe_domain_summary"]
