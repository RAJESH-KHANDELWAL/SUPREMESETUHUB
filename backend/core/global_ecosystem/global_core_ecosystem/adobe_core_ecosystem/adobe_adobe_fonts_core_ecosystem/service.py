"""Read-only Core status surface for Adobe Fonts; no provider API calls."""

from __future__ import annotations


def adobe_fonts_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "adobe_fonts",
        "product_name": "Adobe Fonts",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
