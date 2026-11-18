"""Read-only taxonomy for provider-neutral infrastructure capabilities."""
from copy import deepcopy
from .constants import INFRASTRUCTURE_DOMAINS,STATUS
PROVIDER_CATALOG=(
 {"provider_id":"aws","display_name":"Amazon Web Services"},
 {"provider_id":"google","display_name":"Google Cloud"},
 {"provider_id":"microsoft","display_name":"Microsoft Azure"},
 {"provider_id":"cloudflare","display_name":"Cloudflare"},
 {"provider_id":"digitalocean","display_name":"DigitalOcean"},
 {"provider_id":"other","display_name":"Other / Self-hosted"},
)
DOMAIN_CATALOG=tuple({"domain_id":x.lower().replace("_","-"),"name":x.replace("_"," "),"status":STATUS,"provider_operations_enabled":False} for x in INFRASTRUCTURE_DOMAINS)
def get_domain_catalog(): return deepcopy(list(DOMAIN_CATALOG))
def get_provider_catalog(): return [{**deepcopy(x),"status":"CATALOG_ONLY","live_connection_verified":False} for x in PROVIDER_CATALOG]
def get_infrastructure_catalog():
 return {"ecosystem_id":"GLOBAL-INFRASTRUCTURE-CORE-ECOSYSTEM","status":STATUS,"domains":get_domain_catalog(),"providers":get_provider_catalog(),"live_connection_verified":False}
