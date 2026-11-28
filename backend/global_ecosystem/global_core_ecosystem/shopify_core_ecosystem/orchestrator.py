"""Read-only Shopify discovery and health metadata."""
from .catalog import get_shopify_core_catalog
from .product_catalog import list_products,get_product
from .domain_catalog import list_domains
from .policy import ShopifyCorePolicy
class ShopifyCoreOrchestrator:
    def catalog(self): return get_shopify_core_catalog()
    def list_products(self,*,enabled_only=False):
        items=ShopifyCorePolicy.sanitize(list_products(enabled_only=enabled_only)); return {"success":True,"count":len(items),"products":items}
    def get_product(self,key):
        item=get_product(key); return ShopifyCorePolicy.sanitize(item) if item else None
    def domains(self):
        items=list_domains(); return {"success":True,"domain_count":len(items),"domains":items}
    def health(self): return {"success":True,"ecosystem_id":"SHOPIFY-CORE-ECOSYSTEM","status":"CORE_CATALOG_AVAILABLE","product_count":len(list_products()),"domain_count":len(list_domains()),"live_connections_verified":0,"api_calls_performed":0}
