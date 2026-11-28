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
    def canonical_product_catalog(self) -> dict[str, Any]:
        """Project canonical products from runtime source; former catalog.py is consolidated here."""
        from backend.global_ecosystem.global_cloudflare_ecosystem.catalog import (
            get_cloudflare_catalog, validate_cloudflare_catalog,
        )
        source = get_cloudflare_catalog()
        products = []
        for item in source["products"]:
            product = dict(item)
            product["core_path"] = (
                "backend/core/global_ecosystem/global_core_ecosystem/"
                f"global_cloudflare_core_ecosystem/{item['id']}_cloudflare_core_ecosystem"
            )
            product["ecosystem_id"] = f"CLOUDFLARE-{item['id'].upper()}-CORE-ECOSYSTEM"
            product["status"] = "CORE_CATALOG_ONLY"
            product["live_connection"] = False
            products.append(product)
        return {
            "ecosystem_id": self.ECOSYSTEM_ID, "name": self.NAME,
            "provider": "cloudflare", "status": "REGISTERED",
            "integration_status": source["integration_status"],
            "live_connection_verified": False,
            "runtime_source_of_record": "backend/global_ecosystem/global_cloudflare_ecosystem/catalog.py",
            "catalog_validation": list(validate_cloudflare_catalog()),
            "products": products,
        }
    def master_catalog_snapshot(self) -> dict[str, Any]:
        """Read the existing master catalog; never copy or expand it here."""
        path = Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
        if not path.is_file():
            return {"available": False, "error": "MASTER_CATALOG_NOT_FOUND"}
        data = json.loads(path.read_text(encoding="utf-8"))
        expansion, counts = data.get("expansion", {}), data.get("counts", {})
        return {
            "available": True, "catalogue_id": data.get("catalogue_id"),
            "target_unique_entries": expansion.get("target_unique_entries"),
            "current_unique_entries": expansion.get("current_unique_entries"),
            "remaining_unique_entries": expansion.get("remaining_unique_entries"),
            "source_numbered_entries": counts.get("source_numbered_entries"),
            "cross_reference_entries": counts.get("cross_reference_entries"),
            "status": expansion.get("status"), "policy": expansion.get("policy"),
        }

def get_manager() -> CloudflareCoreManager:
    return CloudflareCoreManager()

__all__ = ["CloudflareCoreManager", "get_manager"]
