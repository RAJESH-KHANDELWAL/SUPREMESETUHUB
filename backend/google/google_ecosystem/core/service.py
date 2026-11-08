"""Shared, non-secret capability metadata for Google ecosystem modules."""
from __future__ import annotations

from typing import Any


def capability(
    subsystem: str,
    product: str,
    api: str | None,
    *,
    auth: str = "Google Cloud IAM / least-privilege identity where supported",
    status: str = "METADATA_ONLY",
    notes: str = "",
) -> dict[str, Any]:
    """Return descriptive metadata; never imply a live provider connection."""
    record: dict[str, Any] = {
        "provider": "google",
        "subsystem": subsystem,
        "product": product,
        "api": api,
        "auth": auth,
        "status": status,
        "connected": False,
    }
    if notes:
        record["notes"] = notes
    return record
