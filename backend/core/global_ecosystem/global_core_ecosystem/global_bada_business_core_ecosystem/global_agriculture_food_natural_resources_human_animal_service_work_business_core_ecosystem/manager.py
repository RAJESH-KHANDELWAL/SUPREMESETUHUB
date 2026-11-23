"""Canonical manager for Bada Business Agriculture/Food capabilities."""
from .catalog import get_catalog
from .service import AgricultureBusinessService
from .orchestrator import AgricultureBusinessOrchestrator
class AgricultureFoodNaturalResourcesBusinessManager:
    NAME = "GLOBAL BADA BUSINESS AGRICULTURE FOOD & NATURAL RESOURCES HUMAN ANIMAL SERVICE WORK BUSINESS CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM"
    def __init__(self):
        self._service = AgricultureBusinessService()
        self._orchestrator = AgricultureBusinessOrchestrator()
    def status(self): return self._service.status()
    def list_domains(self): return self._service.list_domains()
    def get_domain(self, domain_id): return self._service.get_domain(domain_id)
    def inventory(self): return self._orchestrator.inventory()
    def dependencies(self): return self._orchestrator.dependencies()
    def health(self): return self._orchestrator.health()
    def catalog(self): return get_catalog()
def get_manager(): return AgricultureFoodNaturalResourcesBusinessManager()
__all__ = ["AgricultureFoodNaturalResourcesBusinessManager", "get_manager"]
