"""Read-only Core status surface for Adobe Security and Compliance; no provider API calls."""

from __future__ import annotations


def security_and_compliance_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "security_and_compliance",
        "product_name": "Adobe Security and Compliance",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
