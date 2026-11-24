from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME
from .catalog import get_catalog
from .orchestrator import NvidiaCoreOrchestrator
from .service import NvidiaCoreService
class NvidiaCoreManager:
 NAME=ECOSYSTEM_NAME;ECOSYSTEM_ID=ECOSYSTEM_ID
 def __init__(self):self.o=NvidiaCoreOrchestrator();self.s=NvidiaCoreService()
 def status(self):return self.s.status()
 def health(self):return self.o.health()
 def catalog(self):return get_catalog()
 def list_products(self,enabled_only=False):return self.o.products(enabled_only)
 def get_product(self,k):return self.o.product(k)
 def list_domains(self):return self.o.domains()
 def dependency_map(self):return self.o.dependency_map()
def get_manager():return NvidiaCoreManager()
