"""Read-only Core status surface for Adobe Licensing and Entitlements; no provider API calls."""

from __future__ import annotations


def licensing_and_entitlements_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "licensing_and_entitlements",
        "product_name": "Adobe Licensing and Entitlements",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
