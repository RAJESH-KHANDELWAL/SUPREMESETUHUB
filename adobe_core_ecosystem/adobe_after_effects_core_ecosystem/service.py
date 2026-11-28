"""Read-only Core status surface for Adobe After Effects; no provider API calls."""

from __future__ import annotations


def after_effects_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "after_effects",
        "product_name": "Adobe After Effects",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
