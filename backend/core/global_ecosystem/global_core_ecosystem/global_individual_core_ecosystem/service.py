from .catalog import get_catalog
from .orchestrator import GlobalIndividualCoreOrchestrator
class GlobalIndividualCoreService:
    def __init__(self): self.orchestrator=GlobalIndividualCoreOrchestrator()
    def status(self): return {"ecosystem":get_catalog(),"health":self.orchestrator.health(),"master_catalog":self.orchestrator.master_catalog()}
