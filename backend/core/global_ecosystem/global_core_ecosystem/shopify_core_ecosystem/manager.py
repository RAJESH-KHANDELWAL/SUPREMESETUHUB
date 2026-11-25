"""Canonical Shopify Core entry point."""
from .orchestrator import ShopifyCoreOrchestrator
from .service import ShopifyCoreEcosystemService
class ShopifyCoreManager:
    NAME="SHOPIFY CORE ECOSYSTEM"
    ECOSYSTEM_ID="SHOPIFY-CORE-ECOSYSTEM"
    def __init__(self): self._orchestrator=ShopifyCoreOrchestrator(); self._service=ShopifyCoreEcosystemService()
    def status(self): return self._service.status()
    def health(self): return self._orchestrator.health()
    def list_products(self,*,enabled_only=False): return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self,key): return self._orchestrator.get_product(key)
    def list_domains(self): return self._orchestrator.domains()
def get_manager(): return ShopifyCoreManager()
__all__=["ShopifyCoreManager","get_manager"]
