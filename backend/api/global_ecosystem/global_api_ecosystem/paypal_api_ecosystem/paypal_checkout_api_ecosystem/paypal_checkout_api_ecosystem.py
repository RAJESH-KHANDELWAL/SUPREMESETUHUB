"""Checkout API ecosystem catalog.

Catalog metadata only; no live PayPal API calls are made by this module.
"""
from __future__ import annotations

PAYPAL_CHECKOUT_API_ECOSYSTEM = {
    "provider_id": "paypal",
    "service_id": "checkout",
    "name": "GLOBAL PAYPAL CHECKOUT API ECOSYSTEM",
    "description": "Payment button and checkout flows, order approval, capture orchestration, and buyer return flows.",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "authentication": "PAYPAL_OAUTH_2_CLIENT_CREDENTIALS",
    "credential_source": "environment_or_managed_secret_store",
    "api_environment": "explicitly_configured_sandbox_or_production",
}


def get_ecosystem() -> dict[str, object]:
    """Return a copy of this PayPal service-family catalog."""
    return dict(PAYPAL_CHECKOUT_API_ECOSYSTEM)


__all__ = ["PAYPAL_CHECKOUT_API_ECOSYSTEM", "get_ecosystem"]
