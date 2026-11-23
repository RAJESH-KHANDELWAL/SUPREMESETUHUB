"""Product discovery and manager routing."""
from .catalog import list_products,get_product
from .domain_catalog import list_domains
from .module_service import SalesforceProductCoreService
class SalesforceCoreOrchestrator:
    def list_products(self,enabled_only=False): return list_products(enabled_only=enabled_only)
    def get_product(self,product_id): return get_product(product_id)
    def list_domains(self): return list_domains()
    def products_by_domain(self,domain_id): return [p for p in list_products() if p["domain_id"]==str(domain_id).strip().upper()]
    def product_manager(self,product_id): return SalesforceProductCoreService(product_id)
    def health(self): return {"status":"catalog_ready","product_count":len(list_products()),"live_connections_verified":False}
