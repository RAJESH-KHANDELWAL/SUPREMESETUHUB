"""Read-only Core status surface for Adobe Substance 3D; no provider API calls."""

from __future__ import annotations


def substance_3d_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "substance_3d",
        "product_name": "Adobe Substance 3D",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
