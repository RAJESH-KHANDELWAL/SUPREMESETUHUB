"""DeepSeek Core discovery and lifecycle metadata orchestration."""
from __future__ import annotations

from typing import Any

from .catalog import get_catalog, list_capabilities
from .service import DeepSeekCoreService


class DeepSeekCoreOrchestrator:
    """Coordinate capability metadata without provider API calls."""

    def __init__(self) -> None:
        self.service = DeepSeekCoreService()

    def discover(self) -> dict[str, Any]:
        return get_catalog()

    def capabilities(self) -> dict[str, Any]:
        items = list_capabilities()
        return {"success": True, "count": len(items), "capabilities": items}

    def health(self) -> dict[str, Any]:
        catalog = get_catalog()
        capabilities = list_capabilities()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "CORE_CATALOG_AVAILABLE",
            "capability_count": len(capabilities),
            "enabled_capability_count": sum(bool(item.get("live_enabled")) for item in capabilities.values()),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "warning": "Capability registration and contract validation do not prove provider connectivity.",
        }

    def validate(self, capability: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.service.validate(capability, payload)

    def dependency_map(self) -> dict[str, Any]:
        catalog = get_catalog()
        return {
            "success": True,
            "edges": [
                {
                    "capability": capability,
                    "core_package": metadata["package"],
                    "api_ecosystem_ref": catalog["api_ecosystem_ref"],
                    "relationship": "DELEGATES_TO_API_LAYER",
                }
                for capability, metadata in catalog["capabilities"].items()
            ],
        }
}
