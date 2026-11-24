"""Canonical Python entry point for Global Integrations Core."""
from .orchestrator import GlobalIntegrationsCoreOrchestrator
from .service import GlobalIntegrationsCoreService
class GlobalIntegrationsCoreManager:
    NAME="GLOBAL INTEGRATIONS CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-INTEGRATIONS-CORE-ECOSYSTEM"
    def __init__(self):
        self._orchestrator=GlobalIntegrationsCoreOrchestrator()
        self._service=GlobalIntegrationsCoreService()
    def status(self): return self._service.status()
    def health(self): return self._orchestrator.health()
    def catalog(self): return self._orchestrator.catalog()
    def list_domains(self): return self._orchestrator.list_integrations()
    def get_domain(self,domain_id): return self._orchestrator.get_integration(domain_id)
    def list_providers(self): return self._orchestrator.list_providers()
    def get_provider(self,provider_id): return self._orchestrator.get_provider(provider_id)
    def search(self,query): return self._orchestrator.search(query)
    def dependency_map(self): return self._orchestrator.dependency_map()
    def get_domain_manager(self,domain_id): return self._orchestrator.get_domain_manager(domain_id)
def get_manager(): return GlobalIntegrationsCoreManager()
__all__=["GlobalIntegrationsCoreManager","get_manager"]
