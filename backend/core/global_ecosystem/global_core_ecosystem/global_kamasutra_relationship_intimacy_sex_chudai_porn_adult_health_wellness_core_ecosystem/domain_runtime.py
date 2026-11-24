"""Shared read-only domain manager for Kamasutra Core domain packages."""
from __future__ import annotations
from typing import Any
from .catalog import list_products
from .domain_catalog import get_domain
class GlobalKamasutraDomainManager:
    def __init__(self, domain_id: str) -> None:
        if get_domain(domain_id) is None:
            raise ValueError(f"Unknown Kamasutra Core domain: {domain_id}")
        self.domain_id = domain_id
    def status(self) -> dict[str, Any]:
        domain = get_domain(self.domain_id)
        products = self.list_products()
        return {"domain_id": self.domain_id, "name": domain["name"], "status": "CATALOG_ONLY", "connected": False, "package_count": len(products)}
    def list_products(self) -> list[dict[str, Any]]:
        return [item for item in list_products() if item["domain_id"] == self.domain_id]
def get_domain_manager(domain_id: str) -> GlobalKamasutraDomainManager:
    return GlobalKamasutraDomainManager(domain_id)
__all__ = ["GlobalKamasutraDomainManager", "get_domain_manager"]
