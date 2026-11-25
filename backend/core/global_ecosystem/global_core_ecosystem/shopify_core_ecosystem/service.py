"""Public Shopify Core status service."""
from .catalog import get_shopify_core_catalog
from .orchestrator import ShopifyCoreOrchestrator
class ShopifyCoreEcosystemService:
    def __init__(self): self.orchestrator=ShopifyCoreOrchestrator()
    def status(self):
        c=get_shopify_core_catalog()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":c["name"],"provider":c["provider"],"status":c["status"],"product_count":len(c["children"]),"domain_count":len(self.orchestrator.domains()["domains"]),"connected_products":0,"live_connection_verified":False,"api_calls_performed":0}
