"""Canonical Bada Business transport/logistics capability manager."""
from __future__ import annotations

from typing import Any
from .service import GlobalTransportBusinessCoreService

class GlobalTransportBusinessCoreManager:
    NAME = "GLOBAL BADA BUSINESS TRANSPORT LOGISTICS SUPPLY CHAIN SERVICE WORK BUSINESS CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-TRANSPORT-LOGISTICS-SUPPLY-CHAIN-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._service = GlobalTransportBusinessCoreService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def list_capability_groups(self) -> dict[str, Any]:
        return self._service.list_capability_groups()

    def get_capability_group(self, group_id: str) -> dict[str, Any] | None:
        return self._service.get_capability_group(group_id)

def get_manager() -> GlobalTransportBusinessCoreManager:
    return GlobalTransportBusinessCoreManager()

__all__ = ["GlobalTransportBusinessCoreManager", "get_manager"]
