"""Read-only Core status surface for Adobe Stock; no provider API calls."""

from __future__ import annotations


def adobe_stock_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "adobe_stock",
        "product_name": "Adobe Stock",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
