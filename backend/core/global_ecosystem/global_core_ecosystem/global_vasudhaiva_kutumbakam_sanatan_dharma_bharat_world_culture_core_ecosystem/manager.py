"""Stable Python manager for the Global Cultural Core Ecosystem."""
from .orchestrator import CulturalCoreOrchestrator
from .service import GlobalCulturalCore
class CulturalCoreManager:
    NAME="GLOBAL VASUDHAIVA KUTUMBAKAM | SANATAN DHARMA | BHARAT SANSKRITI | WORLD CULTURE CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-VASUDHAIVA-KUTUMBAKAM-SANATAN-DHARMA-BHARAT-WORLD-CULTURE-CORE-ECOSYSTEM"
    def __init__(self): self._service=GlobalCulturalCore(); self._orchestrator=CulturalCoreOrchestrator()
    def status(self):
        result=self._service.status(); result["registry_status"]=self._service.manager_status()["registered"]; return result
    def describe(self): return self._service.describe()
    def health(self): return self._orchestrator.health()
    def list_domains(self): return self._orchestrator.list_domains()
    def get_domain(self,domain_id: str): return self._orchestrator.get_domain(domain_id)
    def get_domain_manager(self,domain_id: str): return self._service.get_domain_manager(domain_id)
    def list_offerings(self): return self._orchestrator.offerings()
    def knowledge(self): return self._service.knowledge()
    def search(self,query: str): return self._service.search_foundation(query)
    def dependency_map(self): return self._orchestrator.dependency_map()
def get_manager(): return CulturalCoreManager()
__all__=["CulturalCoreManager","get_manager"]
