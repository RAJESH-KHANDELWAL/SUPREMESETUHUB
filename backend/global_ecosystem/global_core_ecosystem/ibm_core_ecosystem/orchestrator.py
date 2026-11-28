"""IBM Core discovery, health and dependency orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .product_catalog import list_products,get_product
from .domain_catalog import list_domains,domain_summary
from .policy import IBMCorePolicy
class IBMCoreOrchestrator:
    def catalog(self) -> dict[str,Any]: return get_catalog()
    def products(self) -> list[dict[str,Any]]: return [IBMCorePolicy.sanitize(x) for x in list_products()]
    def product(self, product_id: str) -> dict[str,Any] | None:
        item=get_product(product_id)
        return IBMCorePolicy.sanitize(item) if item else None
    def domains(self) -> list[dict[str,Any]]: return list_domains()
    def health(self) -> dict[str,Any]:
        products=self.products()
        return {"success":True,"ecosystem_id":"IBM-CORE-ECOSYSTEM","status":"CORE_CATALOG_AVAILABLE","product_family_count":len(products),"domain_count":len(self.domains()),"enabled_product_family_count":sum(bool(x.get("enabled")) for x in products),"api_adapter_declared_count":sum(bool(x.get("api_path")) for x in products),"engine_boundary_declared_count":sum(bool(x.get("engine_path")) for x in products),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog metadata does not establish IBM account entitlement, credentials, regional availability or live connectivity."}
    def dependency_map(self) -> dict[str,Any]:
        return {"success":True,"edges":[{"core_module":x["core_module"],"api_path":x["api_path"],"engine_path":x["engine_path"],"relationship":"CORE_METADATA_DELEGATES_API_AND_ENGINE_EXECUTION_TO_SEPARATE_LAYERS"} for x in self.products()]}
