"""OpenAI Core read-only control-plane service."""
from __future__ import annotations

from typing import Any

from .catalog import get_openai_core_catalog
from .orchestrator import OpenAICoreOrchestrator


class OpenAICoreEcosystemService:
    NAME = "OPENAI CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = OpenAICoreOrchestrator()

    def manager_status(self) -> dict[str, Any]:
        try:
            from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
            manager = GlobalEcosystemManager()
            record = manager.get("OPENAI-CORE-ECOSYSTEM")
        except Exception as exc:
            return {
                "success": False,
                "registered": False,
                "ecosystem": None,
                "error": type(exc).__name__,
            }
        return {
            "success": record is not None,
            "registered": record is not None,
            "ecosystem": record,
            "live_connection_verified": False,
        }

    def status(self) -> dict[str, Any]:
        catalog = get_openai_core_catalog()
        health = self.orchestrator.health()
        registry = self.manager_status()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "provider": "openai",
            "status": catalog["status"],
            "registry_status": registry["registered"],
            "module_count": len(catalog["children"]),
            "domain_count": health["domain_count"],
            "api_capability_count": catalog["api_capability_count"],
            "connected_modules": 0,
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": health,
            "registry": registry,
            "api_catalog_ref": catalog["api_catalog_ref"],
            "master_catalog": catalog["master_catalog"],
        }

    def list_modules(self) -> dict[str, Any]:
        return self.orchestrator.list_products()

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def list_offerings(self) -> dict[str, Any]:
        return self.orchestrator.offerings()

    def get_module(self, product_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(product_id)

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()


__all__ = ["OpenAICoreEcosystemService"]
