"""Read-only Core status surface for Adobe Publishing and Delivery; no provider API calls."""

from __future__ import annotations


def publishing_and_delivery_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "publishing_and_delivery",
        "product_name": "Adobe Publishing and Delivery",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
