"""Read-only Core status surface for Adobe Identity and Access; no provider API calls."""

from __future__ import annotations


def identity_and_access_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "identity_and_access",
        "product_name": "Adobe Identity and Access",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
