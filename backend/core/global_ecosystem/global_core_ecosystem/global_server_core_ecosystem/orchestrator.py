"""Offline discovery and readiness orchestration for SERVER CORE."""
from __future__ import annotations
from .catalog import get_catalog
from .provider_catalog import get_provider,get_provider_catalog,provider_summary
from .constants import ECOSYSTEM_ID
class ServerCoreOrchestrator:
    def catalog(self): return get_catalog()
    def providers(self): return get_provider_catalog()
    def provider(self,provider_id): return get_provider(provider_id)
    def health(self):
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"status":"CORE_CATALOG_ONLY",**provider_summary(),"remote_operations_enabled":False,"api_calls_performed":0,"registry_persistence":"PROCESS_LOCAL_ONLY"}
    def dependency_map(self):
        return {"success":True,"edges":[{"provider_id":p["provider_id"],"core_module":f"backend/core/global_ecosystem/global_core_ecosystem/global_server_core_ecosystem/{p['folder']}","relationship":"SERVER_PROVIDER_METADATA","live_connection_verified":False} for p in get_provider_catalog()]}
