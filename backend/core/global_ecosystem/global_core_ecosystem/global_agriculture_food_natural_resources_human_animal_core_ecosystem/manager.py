"""Canonical manager for the global Agriculture/Food/Natural Resources CORE."""
from __future__ import annotations
from .catalog import get_catalog
from .module_service import AgricultureDomainService
from .orchestrator import AgricultureCoreOrchestrator
from .service import AgricultureCoreService

class AgricultureFoodNaturalResourcesHumanAnimalCoreManager:
    NAME = "GLOBAL AGRICULTURE FOOD & NATURAL RESOURCES HUMAN ANIMAL CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM"

    def __init__(self):
        self._orchestrator = AgricultureCoreOrchestrator()
        self._domains = AgricultureDomainService()
        self._service = AgricultureCoreService()

    def status(self):
        return self._service.status()

    def health(self):
        return self._orchestrator.health()

    def list_domains(self):
        return self._domains.list_domains()

    def get_domain(self, domain_id: str):
        return self._domains.get_domain(domain_id)

    def dependency_map(self):
        return self._orchestrator.dependency_map()

    def catalog(self):
        return get_catalog()

def get_manager():
    return AgricultureFoodNaturalResourcesHumanAnimalCoreManager()

__all__ = ["AgricultureFoodNaturalResourcesHumanAnimalCoreManager", "get_manager"]
