"""Provider-level Shopify Core catalog."""
from copy import deepcopy
from .constants import ECOSYSTEM_ID, PROVIDER, API_CATALOG_REF
from .product_catalog import list_products
SHOPIFY_CORE_ECOSYSTEM={"ecosystem_id":ECOSYSTEM_ID,"name":"SHOPIFY CORE ECOSYSTEM","provider":PROVIDER,"ecosystem_type":"PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"REGISTERED","enabled":True,"api_catalog_ref":API_CATALOG_REF,"live_connection_verified":False,"api_transport_in_core":False}
def get_shopify_core_catalog():
    result=deepcopy(SHOPIFY_CORE_ECOSYSTEM); result["children"]=list_products(); return result
