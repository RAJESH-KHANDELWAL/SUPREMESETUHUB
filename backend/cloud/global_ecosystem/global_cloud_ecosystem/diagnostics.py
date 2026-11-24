"""Read-only diagnostics for GLOBAL CLOUD ECOSYSTEM."""
from __future__ import annotations
from typing import Any

def cloud_diagnostics(service: Any) -> dict[str, Any]:
    status = service.status()
    return {
        "ecosystem": "GLOBAL_CLOUD_ECOSYSTEM",
        "layer": "CLOUD",
        "catalog_provider_count": status["provider_count"],
        "configured_adapters": status["configured_adapters"],
        "live_provider_connectivity_verified": False,
    }
