"""Read-only Core status surface for Adobe Experience Manager; no provider API calls."""

from __future__ import annotations


def aem_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "aem",
        "product_name": "Adobe Experience Manager",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
