"""Read-only provider discovery and readiness orchestration."""
from __future__ import annotations
from typing import Any
from .catalog import get_storage_core_catalog, list_storage_providers, get_storage_provider
from .policy import StorageCorePolicy

class GlobalStorageCoreOrchestrator:
    def catalog(self) -> dict[str, Any]:
        return get_storage_core_catalog()
    def list_providers(self, *, enabled_only: bool = False) -> dict[str, Any]:
        items = [StorageCorePolicy.safe_provider_summary(p) for p in list_storage_providers(enabled_only=enabled_only)]
        return {"success":True,"count":len(items),"providers":items}
    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        item = get_storage_provider(provider_id)
        return StorageCorePolicy.safe_provider_summary(item) if item else None
    def health(self) -> dict[str, Any]:
        providers = list_storage_providers()
        return {"success":True,"ecosystem_id":self.catalog()["ecosystem_id"],"status":"STORAGE_CORE_CATALOG_AVAILABLE","provider_count":len(providers),"enabled_provider_count":sum(bool(p.get("enabled",True)) for p in providers),"configured_adapter_count":sum(bool(p.get("adapter_ref")) for p in providers),"live_connections_verified":0,"storage_operations_performed":0,"warning":"Catalog availability does not prove provider credentials, permissions, deployment or live connectivity."}
    def dependency_map(self) -> dict[str, Any]:
        return {"success":True,"edges":[{"core_provider":p["ecosystem_id"],"adapter_ref":p.get("adapter_ref"),"relationship":"DELEGATES_TO_PROVIDER_STORAGE_ADAPTER"} for p in list_storage_providers()]}
