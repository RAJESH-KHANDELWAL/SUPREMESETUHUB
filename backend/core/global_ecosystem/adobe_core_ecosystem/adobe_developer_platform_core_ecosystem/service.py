"""Read-only Core status surface for Adobe Developer Platform; no provider API calls."""

from __future__ import annotations


def developer_platform_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "developer_platform",
        "product_name": "Adobe Developer Platform",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
