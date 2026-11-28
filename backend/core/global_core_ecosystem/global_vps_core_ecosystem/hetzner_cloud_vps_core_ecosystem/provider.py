"""Provider metadata adapter for Hetzner Cloud; no live API calls are made."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from ..catalog import get_provider as _get_provider
PROVIDER_ID = "hetzner_cloud"
PROVIDER_NAME = "Hetzner Cloud"
def get_provider() -> dict[str, Any]:
    record = _get_provider(PROVIDER_ID)
    if record is None:
        raise RuntimeError("PROVIDER_NOT_REGISTERED")
    return deepcopy(record)
def health() -> dict[str, Any]:
    return {"success": True, "provider_id": PROVIDER_ID, "status": "CATALOG_ONLY", "api_transport_verified": False, "live_connection_verified": False}
__all__ = ["PROVIDER_ID", "PROVIDER_NAME", "get_provider", "health"]
