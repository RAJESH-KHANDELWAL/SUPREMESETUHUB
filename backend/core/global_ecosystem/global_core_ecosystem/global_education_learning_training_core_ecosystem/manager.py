from .catalog import get_catalog
from .service import EducationDomainService
from .orchestrator import EducationCoreOrchestrator
from .region_catalog import list_regional_frameworks, get_regional_framework

class EducationLearningTrainingCoreManager:
    NAME = "GLOBAL EDUCATION LEARNING TRAINING CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-EDUCATION-LEARNING-TRAINING-CORE-ECOSYSTEM"

    def __init__(self):
        self.service = EducationDomainService()
        self.orchestrator = EducationCoreOrchestrator()

    def status(self): return self.service.status()
    def list_domains(self): return self.service.list_domains()
    def get_domain(self, domain_id): return self.service.get_domain(domain_id)
    def search(self, keyword): return self.service.search(keyword)
    def regional_frameworks(self): return list_regional_frameworks()
    def get_regional_framework(self, region_id): return get_regional_framework(region_id)
    def dependency_map(self): return self.orchestrator.dependency_map()
    def health(self): return self.orchestrator.health()
    def catalog(self): return get_catalog()

def get_manager(): return EducationLearningTrainingCoreManager()
__all__ = ["EducationLearningTrainingCoreManager", "get_manager"]
