from .catalog import get_catalog
from .service import EducationBusinessService
from .orchestrator import EducationBusinessOrchestrator
class EducationLearningTrainingBusinessManager:
 NAME="GLOBAL EDUCATION LEARNING TRAINING SERVICE WORK BUSINESS CORE ECOSYSTEM"
 ECOSYSTEM_ID="GLOBAL-BADA-BUSINESS-EDUCATION-LEARNING-TRAINING-CORE-ECOSYSTEM"
 def __init__(self): self.service=EducationBusinessService(); self.orchestrator=EducationBusinessOrchestrator()
 def status(self): return self.service.status()
 def list_domains(self): return self.service.list_domains()
 def get_domain(self,domain_id): return self.service.get_domain(domain_id)
 def filter_by_capability(self,capability): return self.service.filter_by_capability(capability)
 def search(self,keyword): return self.service.search(keyword)
 def validation(self): return self.service.validation()
 def inventory(self): return self.orchestrator.inventory()
 def dependencies(self): return self.orchestrator.dependencies()
 def health(self): return self.orchestrator.health()
 def catalog(self): return get_catalog()
def get_manager(): return EducationLearningTrainingBusinessManager()
__all__=["EducationLearningTrainingBusinessManager","get_manager"]
