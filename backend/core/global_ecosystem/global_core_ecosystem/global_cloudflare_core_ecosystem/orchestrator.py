"""Cloudflare product and domain discovery orchestration; no provider API calls."""
from __future__ import annotations
from typing import Any
from .product_catalog import list_products, get_product, product_summary, list_directory_audit
from .domain_catalog import domain_summary, list_domain_inventory
from .policy import CloudflareCorePolicy

class CloudflareCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return product_summary()
    def list_products(self, *, domain_id: str | None = None) -> dict[str, Any]:
        products = list_products()
        if domain_id:
            products = [p for p in products if p["domain_id"] == domain_id.strip().upper()]
        safe = [CloudflareCorePolicy.safe_product_summary(p) for p in products]
        return {"success": True, "count": len(safe), "products": safe}
    def get_product(self, product_id: str) -> dict[str, Any] | None:
        product = get_product(product_id)
        return CloudflareCorePolicy.safe_product_summary(product) if product else None
    def domains(self) -> dict[str, Any]:
        return domain_summary()
    def domain_inventory(self) -> list[dict[str, Any]]:
        return list_domain_inventory()
    def directory_audit(self) -> list[dict[str, Any]]:
        return list_directory_audit()
    def health(self) -> dict[str, Any]:
        summary = domain_summary()
        catalog = product_summary()
        return {"success": True, "ecosystem_id": "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM",
                "status": "CATALOG_AVAILABLE", "product_count": catalog["product_count"],
                "domain_count": summary["domain_count"],
                "directory_audit_count": catalog["directory_audit_count"],
                "implemented_product_count": 0, "live_connections_verified": 0,
                "api_calls_performed": 0,
                "warning": "Directory presence and catalog metadata do not mean a product adapter is implemented or Cloudflare connectivity is live."}
    def dependency_map(self) -> dict[str, Any]:
        return {"success": True, "edges": [
            {"core_module": p["product_id"], "domain_id": p["domain_id"],
             "relationship": "ROUTED_TO_CLOUDFLARE_CORE_DOMAIN"} for p in list_products()
        ]}
