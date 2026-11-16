"""Read-only Core status surface for Adobe Assets and DAM; no provider API calls."""

from __future__ import annotations


def assets_and_dam_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "assets_and_dam",
        "product_name": "Adobe Assets and DAM",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
