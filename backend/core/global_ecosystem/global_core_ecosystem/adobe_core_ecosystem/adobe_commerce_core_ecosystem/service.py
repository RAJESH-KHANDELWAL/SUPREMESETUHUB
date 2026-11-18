"""Read-only Core status surface for Adobe Commerce; no provider API calls."""

from __future__ import annotations


def commerce_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "commerce",
        "product_name": "Adobe Commerce",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
