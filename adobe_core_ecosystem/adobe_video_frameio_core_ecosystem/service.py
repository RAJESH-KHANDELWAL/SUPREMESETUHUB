"""Read-only Core status surface for Frame.io; no provider API calls."""

from __future__ import annotations


def frame_io_core_status() -> dict[str, object]:
    return {
        "provider": "adobe",
        "product_key": "frame_io",
        "product_name": "Frame.io",
        "package_status": "SCAFFOLDED",
        "live_connection_verified": False,
        "credentials_configured": False,
        "implementation_note": "Metadata scaffold only; product capabilities and API entitlements require verification.",
    }
