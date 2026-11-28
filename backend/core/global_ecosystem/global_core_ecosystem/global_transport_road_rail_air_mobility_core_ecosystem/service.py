"""Public service facade for transport CORE catalogue metadata."""
from __future__ import annotations

from typing import Any
from .catalog import ECOSYSTEM_ID, get_transport_catalog
from .orchestrator import GlobalTransportCoreOrchestrator

class GlobalTransportCoreService:
    def __init__(self) -> None:
        self._orchestrator = GlobalTransportCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            **get_transport_catalog(),
        }

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_domains(self) -> dict[str, Any]:
        domains = self._orchestrator.list_domains()
        return {"success": True, "count": len(domains), "domains": domains}

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_domain(domain_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()
