"""Shared read-only product service."""
from .product_catalog import get_product
from .contracts import CoreResult
from .policy import ShopifyCorePolicy
class ShopifyProductCoreService:
    PRODUCT_ID=""
    def __init__(self):
        if not self.PRODUCT_ID: raise NotImplementedError("PRODUCT_ID_REQUIRED")
        self.product=get_product(self.PRODUCT_ID)
        if self.product is None: raise LookupError("SHOPIFY_PRODUCT_NOT_REGISTERED")
    def status(self): return {**self.product,"core_layer":"SHOPIFY_CORE","api_transport_in_core":False,"live_connection_verified":False}
    def authorize_capability(self,capability,context):
        try: ShopifyCorePolicy.require_tenant_context(context)
        except (ValueError,PermissionError) as exc: return CoreResult(False,self.product["ecosystem_id"],"POLICY_DENIED",errors=[str(exc)]).to_dict()
        return CoreResult(False,self.product["ecosystem_id"],"API_ADAPTER_AND_CAPABILITY_REGISTRATION_REQUIRED",errors=["Core metadata does not authorize or execute Shopify API operations"]).to_dict()
