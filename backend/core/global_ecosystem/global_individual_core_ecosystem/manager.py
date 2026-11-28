"""Stable manager for Global Individual Core, matching Google Core's facade pattern."""
from .orchestrator import GlobalIndividualCoreOrchestrator
from .service import GlobalIndividualCoreService
class GlobalIndividualCoreManager:
    NAME="GLOBAL INDIVIDUAL CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM"
    def __init__(self): self._orchestrator=GlobalIndividualCoreOrchestrator(); self._service=GlobalIndividualCoreService()
    def status(self): return self._service.status()
    def health(self): return self._orchestrator.health()
    def list_modules(self): return self._orchestrator.modules()
    def get_module(self,module_id): return self._orchestrator.get_module(module_id)
    def list_domains(self): return self._orchestrator.domains()
    def domain_summary(self): return self._orchestrator.domain_summary()
    def master_catalog(self): return self._orchestrator.master_catalog()
def get_manager(): return GlobalIndividualCoreManager()
__all__=["GlobalIndividualCoreManager","get_manager"]
