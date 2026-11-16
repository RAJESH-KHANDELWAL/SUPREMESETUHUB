from .catalog import get_catalog
from .service import DeepSeekCoreService
class DeepSeekCoreOrchestrator:
    def __init__(self): self.service=DeepSeekCoreService()
    def discover(self): return get_catalog()
    def validate(self,capability,payload): return self.service.validate(capability,payload)
