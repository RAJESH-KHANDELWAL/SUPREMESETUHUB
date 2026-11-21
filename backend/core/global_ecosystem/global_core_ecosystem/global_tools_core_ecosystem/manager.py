"""Stable public Python entry point."""
from .orchestrator import GlobalToolsCoreOrchestrator
from .service import GlobalToolsCoreService
from .domain_runtime import ToolsCoreDomainManager
class GlobalToolsCoreManager:
 NAME="GLOBAL TOOLS CORE ECOSYSTEM"; ECOSYSTEM_ID="GLOBAL-TOOLS-CORE-ECOSYSTEM"
 def __init__(self): self.core=GlobalToolsCoreOrchestrator(); self.service=GlobalToolsCoreService()
 def status(self): return self.service.status()
 def health(self): return self.core.health()
 def list_providers(self): return self.core.providers()
 def get_provider(self,key):
  from .catalog import get_provider
  return get_provider(key)
 def list_products(self,provider_id=None,category=None): return self.core.products(provider_id,category)
 def get_product(self,key): return self.core.products()["products"] and __import__(__package__+".product_catalog",fromlist=["get_product"]).get_product(key)
 def list_domains(self): return self.core.domains()
 def get_domain_manager(self,key): return ToolsCoreDomainManager(key)
 def dependency_map(self): return self.core.dependency_map()
def get_manager(): return GlobalToolsCoreManager()
__all__=["GlobalToolsCoreManager","get_manager"]
