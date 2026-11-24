from .catalog import get_catalog
from .service import IndependentWorkService
from .orchestrator import IndependentWorkOrchestrator
from .region_catalog import list_regions,get_region
from .policy import policy_summary
class IndependentWorkEcosystemManager:
 NAME="GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID WORK ECOSYSTEM"
 ECOSYSTEM_ID="GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-WORK-ECOSYSTEM"
 def __init__(self): self.service=IndependentWorkService(); self.orchestrator=IndependentWorkOrchestrator()
 def status(self): return self.service.status()
 def list_domains(self): return self.service.list_domains()
 def get_domain(self,domain_id): return self.service.get_domain(domain_id)
 def search(self,keyword): return self.service.search(keyword)
 def catalog(self): return get_catalog()
 def regions(self): return list_regions()
 def get_region(self,region_id): return get_region(region_id)
 def policy(self): return policy_summary()
 def health(self): return self.orchestrator.health()
 def dependencies(self): return self.orchestrator.dependency_map()
def get_manager(): return IndependentWorkEcosystemManager()
__all__=["IndependentWorkEcosystemManager","get_manager"]
