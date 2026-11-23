from .catalog import get_catalog
from .service import EducationDomainService
from .orchestrator import EducationCoreOrchestrator
class EducationLearningTrainingCoreManager:
 NAME="GLOBAL EDUCATION LEARNING TRAINING CORE ECOSYSTEM"
 ECOSYSTEM_ID="GLOBAL-EDUCATION-LEARNING-TRAINING-CORE-ECOSYSTEM"
 def __init__(self): self.service=EducationDomainService(); self.orchestrator=EducationCoreOrchestrator()
 def status(self): return self.service.status()
 def list_domains(self): return self.service.list_domains()
 def get_domain(self,domain_id): return self.service.get_domain(domain_id)
 def search(self,keyword): return self.service.search(keyword)
 def dependency_map(self): return self.orchestrator.dependency_map()
 def health(self): return self.orchestrator.health()
 def catalog(self): return get_catalog()
def get_manager(): return EducationLearningTrainingCoreManager()
__all__=["EducationLearningTrainingCoreManager","get_manager"]
