"""Read-only public service for Microsoft Core metadata."""
from __future__ import annotations
from typing import Any
from .manager import get_microsoft_core_catalog
from .orchestrator import MicrosoftCoreOrchestrator

class MicrosoftCoreEcosystemService:
    NAME = "MICROSOFT CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = MicrosoftCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_microsoft_core_catalog()
        health = self.orchestrator.health()
        return {"success": True, "ecosystem_id": catalog["ecosystem_id"], "name": self.NAME,
                "provider": "microsoft", "status": catalog["status"], "module_count": len(catalog["children"]),
                "domain_count": health["domain_count"], "registered_product_domain_count": health["registered_product_domain_count"],
                "connected_modules": 0, "live_connection_verified": False, "api_calls_performed": 0,
                "health": health, "api_catalog_ref": catalog["api_catalog_ref"]}

    def list_modules(self) -> dict[str, Any]:
        return self.orchestrator.list_products()

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def get_module(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(ecosystem_id)

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()
