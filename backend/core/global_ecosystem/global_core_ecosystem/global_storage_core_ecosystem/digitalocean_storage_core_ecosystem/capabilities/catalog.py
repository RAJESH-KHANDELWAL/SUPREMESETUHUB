"""DigitalOcean storage capability catalog."""
from ..ecosystem_config import PROVIDER_ID,PROVIDER_NAME,DOMAINS,CAPABILITIES
def list_capabilities():
 return [{"provider_id":PROVIDER_ID,"provider_name":PROVIDER_NAME,"capability_id":c,"domains":list(DOMAINS),"status":"CATALOG_ONLY","live_connection_verified":False} for c in CAPABILITIES]
