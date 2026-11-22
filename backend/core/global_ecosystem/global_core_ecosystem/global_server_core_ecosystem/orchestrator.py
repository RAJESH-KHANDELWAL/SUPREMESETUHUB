"""Server Core discovery, policy-aware metadata and readiness orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .contracts import Readiness
from .domain_catalog import list_server_core_domain_inventory, server_core_domain_summary
from .policy import ServerCorePolicy
from .provider_catalog import get_provider, get_provider_catalog
from .scope_catalog import get_scope_catalog

class ServerCoreOrchestrator:
    """Coordinate local catalogs and contracts without provider API calls."""
    def catalog(self) -> dict[str, Any]:
        return get_catalog()
    def providers(self) -> dict[str, Any]:
        items=[ServerCorePolicy.safe_summary(x) for x in get_provider_catalog()]
        return {"success":True,"count":len(items),"providers":items}
    def provider(self, provider_id: str):
        item=get_provider(provider_id)
        return ServerCorePolicy.safe_summary(item) if item else None
    def domains(self):
        return server_core_domain_summary()
    def domain_inventory(self):
        return list_server_core_domain_inventory()
    def scopes(self):
        return get_scope_catalog()
    def health(self) -> dict[str, Any]:
        catalog=self.catalog()
        domains=self.domains()
        return {"success":True,"ecosystem_id":catalog["ecosystem_id"],
                "status":"CORE_CATALOG_AVAILABLE","provider_count":catalog["provider_count"],
                "core_domain_count":domains["domain_count"],
                "workload_domain_count":catalog["workload_domain_count"],
                "service_tier_count":len(catalog["service_tiers"]),
                "enabled_provider_count":sum(bool(p.get("enabled",True)) for p in catalog["providers"]),
                "live_provider_connections_verified":0,"api_calls_performed":0,
                "remote_operations_enabled":False,"registry_persistence":"PROCESS_LOCAL_ONLY",
                "readiness":Readiness.METADATA_AVAILABLE.value,
                "warning":"Catalog and readiness metadata do not prove provider connectivity, entitlement, provisioning or production readiness."}
    def dependency_map(self) -> dict[str, Any]:
        catalog=self.catalog()
        return {"success":True,"edges":[
            {"provider_id":item["provider_id"],
             "core_module":f"backend/core/global_ecosystem/global_core_ecosystem/global_server_core_ecosystem/{item['folder']}",
             "relationship":"SERVER_PROVIDER_METADATA","api_calls_performed":0,
             "live_connection_verified":False} for item in catalog["providers"]],
            "layer_boundaries":{"api":"authentication, consent and provider API transport",
             "engine":"provider SDKs, adapters, provisioning and remote execution",
             "database":"durable persistence and transactions",
             "storage":"object, file, backup and artifact persistence"}}
