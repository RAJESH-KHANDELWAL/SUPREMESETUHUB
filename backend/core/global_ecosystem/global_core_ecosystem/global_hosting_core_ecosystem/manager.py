"""Central manager for GLOBAL HOSTING CORE ECOSYSTEM."""
from .orchestrator import GlobalHostingCoreOrchestrator
from .service import GlobalHostingCoreService
from .module_service import HostingProviderCoreService
from .domain_catalog import get_hosting_domain
class GlobalHostingCoreManager:
 NAME="GLOBAL HOSTING CORE ECOSYSTEM";ECOSYSTEM_ID="GLOBAL-HOSTING-CORE-ECOSYSTEM"
 def __init__(self):self._orchestrator=GlobalHostingCoreOrchestrator();self._service=GlobalHostingCoreService()
 def status(self):return self._service.status()
 def health(self):return self._orchestrator.health()
 def list_providers(self,*,provider_records_only=False,category=None):return self._orchestrator.list_providers(provider_records_only=provider_records_only,category=category)
 def get_provider(self,key):return self._orchestrator.get_provider(key)
 def get_provider_manager(self,provider_id):return HostingProviderCoreService(provider_id)
 def list_domains(self):return self._orchestrator.domains()
 def list_domain_inventory(self):return self._orchestrator.domain_inventory()
 def get_domain(self,domain_id):return get_hosting_domain(domain_id)
 def dependency_map(self):return self._orchestrator.dependency_map()
def get_manager():return GlobalHostingCoreManager()
__all__=["GlobalHostingCoreManager","get_manager"]
