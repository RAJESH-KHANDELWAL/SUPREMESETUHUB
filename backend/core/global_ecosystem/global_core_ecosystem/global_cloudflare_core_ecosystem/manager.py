"""Stable public manager for the Global Cloudflare Core Ecosystem."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from .orchestrator import CloudflareCoreOrchestrator
from .service import CloudflareCoreEcosystemService

class CloudflareCoreManager:
    NAME = "GLOBAL CLOUDFLARE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM"
    def __init__(self) -> None:
        self._orchestrator = CloudflareCoreOrchestrator()
        self._service = CloudflareCoreEcosystemService()
    def status(self) -> dict[str, Any]:
        return self._service.status()
    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()
    def list_products(self, *, domain_id: str | None = None) -> dict[str, Any]:
        return self._orchestrator.list_products(domain_id=domain_id)
    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(product_id)
    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()
    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()
    def directory_audit(self) -> list[dict[str, Any]]:
        return self._orchestrator.directory_audit()
    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()
    def master_catalog_snapshot(self) -> dict[str, Any]:
        """Read the existing 2468 master catalog; never copy or expand it here."""
        path = Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
        if not path.is_file():
            return {"available": False, "error": "MASTER_CATALOG_NOT_FOUND"}
        data = json.loads(path.read_text(encoding="utf-8"))
        expansion = data.get("expansion", {})
        counts = data.get("counts", {})
        return {"available": True, "catalogue_id": data.get("catalogue_id"),
                "target_unique_entries": expansion.get("target_unique_entries"),
                "current_unique_entries": expansion.get("current_unique_entries"),
                "remaining_unique_entries": expansion.get("remaining_unique_entries"),
                "source_numbered_entries": counts.get("source_numbered_entries"),
                "cross_reference_entries": counts.get("cross_reference_entries"),
                "status": expansion.get("status"),
                "policy": expansion.get("policy")}
def get_manager() -> CloudflareCoreManager:
    return CloudflareCoreManager()
__all__ = ["CloudflareCoreManager", "get_manager"]
