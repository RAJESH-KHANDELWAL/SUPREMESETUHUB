"""Payments API ecosystem catalog.

Catalog metadata only; no live PayPal API calls are made by this module.
"""
from __future__ import annotations

PAYPAL_PAYMENTS_API_ECOSYSTEM = {
    "provider_id": "paypal",
    "service_id": "payments",
    "name": "GLOBAL PAYPAL PAYMENTS API ECOSYSTEM",
    "description": "Payment captures, authorizations, refunds, and related payment lifecycle resources.",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "authentication": "PAYPAL_OAUTH_2_CLIENT_CREDENTIALS",
    "credential_source": "environment_or_managed_secret_store",
    "api_environment": "explicitly_configured_sandbox_or_production",
}


def get_ecosystem() -> dict[str, object]:
    """Return a copy of this PayPal service-family catalog."""
    return dict(PAYPAL_PAYMENTS_API_ECOSYSTEM)


__all__ = ["PAYPAL_PAYMENTS_API_ECOSYSTEM", "get_ecosystem"]
