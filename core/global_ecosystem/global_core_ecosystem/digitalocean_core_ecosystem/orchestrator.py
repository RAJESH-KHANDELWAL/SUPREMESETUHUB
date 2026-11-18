from .catalog import get_catalog
from .service import DigitalOceanCoreService
class DigitalOceanCoreOrchestrator:
    def __init__(self): self.service=DigitalOceanCoreService()
    def discover(self): return get_catalog()
    def validate(self,capability,payload): return self.service.validate(capability,payload)
