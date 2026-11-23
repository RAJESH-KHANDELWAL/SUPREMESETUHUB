"""Global AI Core read-only provider registry service."""
from __future__ import annotations

from typing import Any

from .catalog import ECOSYSTEM
from .orchestrator import GlobalAICoreOrchestrator


class GlobalAICoreEcosystemService:
    NAME = "GLOBAL AI CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = GlobalAICoreOrchestrator()

    def status(self) -> dict[str, Any]:
        health = self.orchestrator.health()
        registry = self.manager_status()
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM["ecosystem_id"],
            "name": self.NAME,
            "provider": "global_ai",
            "status": ECOSYSTEM["status"],
            "registry_status": registry["registered"],
            "module_count": health["provider_count"],
            "domain_count": health["domain_count"],
            "runtime_offering_count": health["runtime_offering_count"],
            "connected_modules": 0,
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "master_catalog_ref": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "master_catalog_target_unique_entries": 2468,
            "master_catalog_owner_layer": "GLOBAL_ENGINE_ECOSYSTEM",
            "health": health,
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
            record = GlobalEcosystemManager().get("GLOBAL-AI-CORE-ECOSYSTEM")
        except Exception as exc:
            return {
                "success": False,
                "registered": False,
                "ecosystem": None,
                "error": type(exc).__name__,
                "live_connection_verified": False,
            }
        return {
            "success": record is not None,
            "registered": record is not None,
            "ecosystem": record,
            "live_connection_verified": False,
        }

    def list_registered_modules(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            manager = GlobalEcosystemManager()
            modules = self.orchestrator.list_products()["products"]
            registered = [
                record for record in (
                    manager.get(module["ecosystem_id"]) for module in modules
                )
                if record is not None
            ]
            return {
                "success": len(registered) == len(modules),
                "count": len(registered),
                "expected_count": len(modules),
                "modules": registered,
            }
        except Exception as exc:
            return {
                "success": False,
                "count": 0,
                "modules": [],
                "error": type(exc).__name__,
            }

    def get_module(self, provider_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(provider_id)

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()


__all__ = ["GlobalAICoreEcosystemService"]
