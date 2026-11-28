"""Read-only Core status surface for Adobe Acrobat and PDF; no provider API calls."""

from __future__ import annotations


def acrobat_pdf_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "acrobat_pdf",
        "product_name": "Adobe Acrobat and PDF",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
