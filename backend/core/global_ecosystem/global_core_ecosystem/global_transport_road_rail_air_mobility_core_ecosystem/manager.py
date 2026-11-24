"""Canonical manager for Global Transport Road Rail Air Mobility CORE."""
from __future__ import annotations

from typing import Any
from .catalog import ECOSYSTEM_ID
from .orchestrator import GlobalTransportCoreOrchestrator
from .service import GlobalTransportCoreService

class GlobalTransportCoreManager:
    NAME = "GLOBAL TRANSPORT ROAD RAIL AIR MOBILITY CORE ECOSYSTEM"
    ECOSYSTEM_ID = ECOSYSTEM_ID

    def __init__(self) -> None:
        self._orchestrator = GlobalTransportCoreOrchestrator()
        self._service = GlobalTransportCoreService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_domains(self) -> dict[str, Any]:
        return self._service.list_domains()

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_domain(domain_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

def get_manager() -> GlobalTransportCoreManager:
    return GlobalTransportCoreManager()

__all__ = ["GlobalTransportCoreManager", "get_manager"]
