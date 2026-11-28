"""Read-only Core status surface for Marketo Engage; no provider API calls."""

from __future__ import annotations


def marketo_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "marketo",
        "product_name": "Marketo Engage",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
