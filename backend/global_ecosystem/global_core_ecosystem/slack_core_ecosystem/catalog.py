"""Slack provider-level Core catalog."""
from copy import deepcopy
from .constants import API_CATALOG_REF,ECOSYSTEM_ID,PROVIDER
from .product_catalog import list_products
SLACK_CORE_ECOSYSTEM={"ecosystem_id":ECOSYSTEM_ID,"name":"SLACK CORE ECOSYSTEM","provider":PROVIDER,"ecosystem_type":"PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"REGISTERED","enabled":True,"api_catalog_ref":API_CATALOG_REF,"api_transport_in_core":False,"oauth_exchange_in_core":False,"live_connection_verified":False}
def get_slack_core_catalog():
 result=deepcopy(SLACK_CORE_ECOSYSTEM);result["children"]=list_products();return result
