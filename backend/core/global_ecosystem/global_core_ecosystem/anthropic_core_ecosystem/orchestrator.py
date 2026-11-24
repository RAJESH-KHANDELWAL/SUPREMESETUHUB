"""Read-only discovery and health for Anthropic Core modules."""
from __future__ import annotations
from typing import Any
from .catalog import get_anthropic_core_catalog,list_anthropic_core_modules

class AnthropicCoreOrchestrator:
    def list_products(self) -> dict[str,Any]:
        items=list_anthropic_core_modules()
        return {"success":True,"count":len(items),"products":items}
    def get_product(self,ecosystem_id: str) -> dict[str,Any] | None:
        return next((x for x in list_anthropic_core_modules() if x["ecosystem_id"]==ecosystem_id),None)
    def health(self) -> dict[str,Any]:
        c=get_anthropic_core_catalog(); items=c["children"]
        return {"success":True,"provider":"anthropic","module_count":len(items),
                "catalog_only_count":sum(x["status"]=="CORE_CATALOG_ONLY" for x in items),
                "connected_count":sum(x.get("connected") is True for x in items),
                "live_connection_verified":False}
    def dependency_map(self) -> dict[str,Any]:
        c=get_anthropic_core_catalog()
        return {"provider":"anthropic","core_to_api":[{"ecosystem_id":x["ecosystem_id"],"api_catalog_ref":x["api_catalog_ref"]} for x in c["children"]]}
