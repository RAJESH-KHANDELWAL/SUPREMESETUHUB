"""Read-only manager for the global transport and mobility Core domain."""
from __future__ import annotations

from typing import Any

from .catalog import ECOSYSTEM_ID, get_transport_mode, list_transport_modes


class GlobalTransportMobilityCoreManager:
    """Expose transport-mode metadata without executing transport operations."""

    ecosystem_id = ECOSYSTEM_ID

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": self.ecosystem_id,
            "status": "CORE_CATALOG_ONLY",
            "transport_mode_count": len(list_transport_modes()),
            "live_transport_operations_verified": False,
            "api_calls_performed": 0,
            "business_services_owned_here": False,
        }

    def list_modes(self) -> dict[str, Any]:
        modes = list_transport_modes()
        return {"success": True, "count": len(modes), "modes": modes}

    def get_mode(self, mode_id: str) -> dict[str, Any] | None:
        return get_transport_mode(mode_id)


def get_manager() -> GlobalTransportMobilityCoreManager:
    return GlobalTransportMobilityCoreManager()


__all__ = ["GlobalTransportMobilityCoreManager", "get_manager"]
