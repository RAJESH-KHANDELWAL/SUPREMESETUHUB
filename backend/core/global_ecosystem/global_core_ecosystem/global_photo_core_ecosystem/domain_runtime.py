"""Shared read-only Photo Core domain discovery manager."""
from .domain_catalog import DOMAIN_DEFINITIONS
from .catalog import PROVIDERS
class DomainManager:
    def __init__(self,domain_id:str):
        if domain_id not in DOMAIN_DEFINITIONS: raise ValueError("UNKNOWN_DOMAIN_ID")
        self.domain_id=domain_id
    def status(self)->dict:
        return {"success":True,"domain_id":self.domain_id,**DOMAIN_DEFINITIONS[self.domain_id],"provider_count":len(self.list_providers()),"live_connections_verified":0}
    def list_providers(self)->list[dict]:
        from .policy import safe_metadata
        return [safe_metadata(p) for p in PROVIDERS if p["domain_id"]==self.domain_id]
