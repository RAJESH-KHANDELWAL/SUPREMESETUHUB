"""Read-only Core status surface for Adobe Experience Cloud; no provider API calls."""

from __future__ import annotations


def experience_cloud_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "experience_cloud",
        "product_name": "Adobe Experience Cloud",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
