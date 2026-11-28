"""Canonical Salesforce Core manager."""
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME
from .orchestrator import SalesforceCoreOrchestrator
from .service import SalesforceCoreService
class SalesforceCoreManager:
    NAME=ECOSYSTEM_NAME; ECOSYSTEM_ID=ECOSYSTEM_ID
    def __init__(self): self._orchestrator=SalesforceCoreOrchestrator(); self._service=SalesforceCoreService()
    def status(self): return self._service.status()
    def health(self): return self._orchestrator.health()
    def list_products(self,*,enabled_only=False): return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self,product_id): return self._orchestrator.get_product(product_id)
    def list_domains(self): return self._orchestrator.list_domains()
    def products_by_domain(self,domain_id): return self._orchestrator.products_by_domain(domain_id)
    def product_manager(self,product_id): return self._orchestrator.product_manager(product_id)
    def policy(self): return self._service.policy()
def get_manager(): return SalesforceCoreManager()
__all__=["SalesforceCoreManager","get_manager"]
