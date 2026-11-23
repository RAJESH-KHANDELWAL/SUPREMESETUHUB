"""Read-only Core status surface for Adobe Premiere Pro; no provider API calls."""

from __future__ import annotations


def premiere_pro_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "premiere_pro",
        "product_name": "Adobe Premiere Pro",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
