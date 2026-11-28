"""Photo provider and domain discovery orchestration."""
from .catalog import get_catalog,get_provider
from .domain_catalog import domain_summary,list_domains
from .master_catalog import master_catalog_status
from .policy import safe_metadata
class CoreOrchestrator:
    def status(self)->dict:
        c=get_catalog(); d=domain_summary()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"status":c["status"],"provider_count":c["provider_count"],"domain_count":d["domain_count"],"master_catalog":master_catalog_status(),"live_connections_verified":0,"api_calls_performed":0}
    def list_providers(self,enabled_only:bool=False)->dict:
        items=[safe_metadata(p) for p in get_catalog()["providers"] if not enabled_only or p.get("enabled",True)]
        return {"success":True,"count":len(items),"providers":items}
    def get_provider(self,provider_id:str):
        item=get_provider(provider_id); return safe_metadata(item) if item else None
    def domains(self)->dict: return domain_summary()
    def list_domains(self)->list[dict]: return list_domains()
    def dependency_map(self)->dict:
        return {"success":True,"edges":[{"provider_id":p["provider_id"],"core_path":p["core_path"],"api_adapter_declared":False,"relationship":"API_ADAPTER_MUST_REMAIN_IN_API_LAYER"} for p in get_catalog()["providers"]]}
