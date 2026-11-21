"""Public read-only service for the Global System Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .catalog import get_system_core_catalog
from .orchestrator import SystemCoreOrchestrator


class SystemCoreEcosystemService:
    NAME = "GLOBAL SYSTEM CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = SystemCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_system_core_catalog()
        health = self.orchestrator.health()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "status": catalog["status"],
            "provider_count": health["provider_count"],
            "product_count": health["product_count"],
            "domain_count": health["domain_count"],
            "live_connections_verified": False,
            "host_operations_performed": 0,
            "master_catalog_ref": catalog["master_catalog_ref"],
            "master_catalog_access_mode": "READ_ONLY_VALIDATED_REFERENCES",
            "health": health,
        }

    def list_providers(self) -> dict[str, Any]:
        return self.orchestrator.list_providers()

    def list_products(self, *, provider_id: str | None = None) -> dict[str, Any]:
        return self.orchestrator.list_products(provider_id=provider_id)

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()
