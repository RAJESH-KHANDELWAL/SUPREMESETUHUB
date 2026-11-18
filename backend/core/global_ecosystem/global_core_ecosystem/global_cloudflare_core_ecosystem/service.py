"""Global Cloudflare Core read-only service facade."""
from __future__ import annotations

from typing import Any

from .catalog import get_cloudflare_core_catalog
from .contracts import CloudflareCoreResult
from .orchestrator import CloudflareCoreOrchestrator


class CloudflareCoreEcosystemService:
    NAME = "GLOBAL CLOUDFLARE CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = CloudflareCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_cloudflare_core_catalog()
        health = self.orchestrator.health()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "provider": "cloudflare",
            "status": catalog["status"],
            "product_count": len(catalog["products"]),
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "health": health,
        }

    def list_products(self, *, category: str | None = None) -> dict[str, Any]:
        return self.orchestrator.list_products(category=category)

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(product_id)

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, str]:
        return self.orchestrator.dependency_map()

    @staticmethod
    def result(data: dict[str, Any]) -> CloudflareCoreResult:
        return CloudflareCoreResult(
            success=True,
            ecosystem_id="GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM",
            data=data,
            execution_performed=False,
            persistence_performed=False,
            live_connection_verified=False,
        )


__all__ = ["CloudflareCoreEcosystemService"]
