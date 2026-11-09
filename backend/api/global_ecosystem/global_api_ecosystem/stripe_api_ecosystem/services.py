"""Stripe service-family registry and common API operations."""
from __future__ import annotations

from typing import Any

from .client import StripeClient

SERVICE_PATHS = {
    "accounts": "/v1/accounts",
    "account_links": "/v1/account_links",
    "balance": "/v1/balance",
    "balance_transactions": "/v1/balance_transactions",
    "charges": "/v1/charges",
    "checkout_sessions": "/v1/checkout/sessions",
    "coupons": "/v1/coupons",
    "credit_notes": "/v1/credit_notes",
    "customers": "/v1/customers",
    "disputes": "/v1/disputes",
    "events": "/v1/events",
    "files": "/v1/files",
    "invoices": "/v1/invoices",
    "payment_intents": "/v1/payment_intents",
    "payment_links": "/v1/payment_links",
    "payment_methods": "/v1/payment_methods",
    "payouts": "/v1/payouts",
    "prices": "/v1/prices",
    "products": "/v1/products",
    "refunds": "/v1/refunds",
    "reviews": "/v1/reviews",
    "setup_intents": "/v1/setup_intents",
    "subscriptions": "/v1/subscriptions",
    "tax_rates": "/v1/tax_rates",
    "tokens": "/v1/tokens",
    "transfers": "/v1/transfers",
    "webhook_endpoints": "/v1/webhook_endpoints",
}


def list_service_families() -> list[dict[str, str]]:
    return [{"id": key, "endpoint": value} for key, value in SERVICE_PATHS.items()]


def list_resource(client: StripeClient, family: str, *, limit: int = 10, **params: Any) -> dict[str, Any]:
    """List a resource using its registered endpoint."""
    if family not in SERVICE_PATHS:
        raise ValueError(f"Unsupported Stripe service family: {family}")
    bounded_limit = max(1, min(int(limit), 100))
    return client.request("GET", SERVICE_PATHS[family], params={"limit": bounded_limit, **params})


__all__ = ["SERVICE_PATHS", "list_service_families", "list_resource"]
