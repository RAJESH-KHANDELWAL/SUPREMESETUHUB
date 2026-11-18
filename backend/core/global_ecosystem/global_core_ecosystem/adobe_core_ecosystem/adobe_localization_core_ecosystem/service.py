"""Read-only Core status surface for Adobe Localization; no provider API calls."""

from __future__ import annotations


def localization_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "localization",
        "product_name": "Adobe Localization",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
