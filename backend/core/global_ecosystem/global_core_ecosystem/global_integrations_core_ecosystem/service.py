"""Public read-only service facade."""
from collections.abc import Mapping
from .catalog import get_catalog,get_integration
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME,MASTER_CATALOG_REF,STATUS
from .orchestrator import GlobalIntegrationsCoreOrchestrator
from .policy import redact_sensitive_metadata
class GlobalIntegrationsCoreService:
    NAME=ECOSYSTEM_NAME
    def __init__(self): self.orchestrator=GlobalIntegrationsCoreOrchestrator()
    def status(self):
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"name":self.NAME,"layer":"CORE",
          "status":STATUS,"health":self.orchestrator.health(),"master_catalog_ref":MASTER_CATALOG_REF,
          "provider_execution_enabled":False,"live_connection_verified":False}
    def health(self): return self.orchestrator.health()
    def catalog(self): return redact_sensitive_metadata(get_catalog())
    def list_domains(self): return self.orchestrator.list_integrations()
    def get_domain(self,domain_id): return get_integration(domain_id)
    def list_providers(self): return self.orchestrator.list_providers()
    def search(self,query): return self.orchestrator.search(query)
    def inspect_metadata(self,metadata):
        if not isinstance(metadata,Mapping): raise TypeError("metadata must be a mapping")
        return redact_sensitive_metadata(metadata)
    def dependency_map(self): return self.orchestrator.dependency_map()
