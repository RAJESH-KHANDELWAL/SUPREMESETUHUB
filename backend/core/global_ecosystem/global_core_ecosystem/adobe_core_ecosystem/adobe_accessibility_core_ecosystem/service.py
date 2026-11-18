"""Read-only Core status surface for Adobe Accessibility; no provider API calls."""

from __future__ import annotations


def accessibility_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "accessibility",
        "product_name": "Adobe Accessibility",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
