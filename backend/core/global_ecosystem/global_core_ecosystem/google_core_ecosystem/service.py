"""Google Core Ecosystem read-only control-plane service."""
from __future__ import annotations

from typing import Any

from .catalog import get_google_core_catalog
from .orchestrator import GoogleCoreOrchestrator


class GoogleCoreEcosystemService:
    NAME = "GOOGLE CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = GoogleCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_google_core_catalog()
        children = catalog["children"]
        health = self.orchestrator.health()
        registry = self.manager_status()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "provider": "google",
            "status": catalog["status"],
            "registry_status": registry["registered"],
            "module_count": len(children),
            "domain_count": health["domain_count"],
            "runtime_offering_count": health["runtime_offering_count"],
            "connected_modules": sum(1 for child in children if child.get("connected") is True),
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": health,
            "api_catalog_ref": catalog["api_catalog_ref"],
            "existing_google_core_ref": catalog["existing_google_core_ref"],
        }

    def list_modules(self) -> dict[str, Any]:
        return self.orchestrator.list_products()

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def list_offerings(self) -> dict[str, Any]:
        return self.orchestrator.offerings()

    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            manager = GlobalEcosystemManager()
            record = manager.get("GOOGLE-CORE-ECOSYSTEM")
        except Exception as exc:
            return {"success": False, "registered": False, "ecosystem": None, "error": type(exc).__name__}
        return {
            "success": record is not None,
            "registered": record is not None,
            "ecosystem": record,
            "live_connection_verified": False,
        }

    def list_registered_modules(self) -> dict[str, Any]:
        from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
        manager = GlobalEcosystemManager()
        modules = self.orchestrator.list_products()["products"]
        registered = [manager.get(module["ecosystem_id"]) for module in modules]
        registered = [item for item in registered if item is not None]
        return {"success": len(registered) == len(modules), "count": len(registered), "modules": registered}

    def get_module(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(ecosystem_id)

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()
