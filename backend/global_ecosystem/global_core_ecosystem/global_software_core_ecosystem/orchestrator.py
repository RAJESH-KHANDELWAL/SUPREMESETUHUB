"""Provider and domain metadata discovery for Global Software Core."""
from __future__ import annotations
from typing import Any
from .catalog import get_software_core_catalog, list_software_providers
from .domain_catalog import software_domain_summary, list_software_domain_inventory
from .policy import SoftwareCorePolicy
class GlobalSoftwareCoreOrchestrator:
    def catalog(self): return get_software_core_catalog()
    def list_providers(self, *, enabled_only: bool=False) -> dict[str, Any]:
        items=[SoftwareCorePolicy.safe_provider_summary(p) for p in list_software_providers(enabled_only=enabled_only)]
        return {"success":True,"count":len(items),"providers":items}
    def get_provider(self, provider_id: str):
        key=provider_id.strip().casefold()
        return next((SoftwareCorePolicy.safe_provider_summary(p) for p in list_software_providers() if p["provider"].casefold()==key or p["ecosystem_id"].casefold()==key),None) if key else None
    def domains(self): return software_domain_summary()
    def domain_inventory(self): return list_software_domain_inventory()
    def health(self):
        c=self.catalog()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":"CORE_CATALOG_AVAILABLE","provider_count":len(c["providers"]),"domain_count":len(c["domains"]),"live_connections_verified":0,"api_calls_performed":0,"warning":"Catalog entries do not prove installation, license entitlement, deployment or live provider connectivity."}
