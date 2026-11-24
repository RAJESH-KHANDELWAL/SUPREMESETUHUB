"""Root service: status and policy views."""
from .catalog import list_products
from .domain_catalog import list_domains
from .policy import policy_snapshot
from .constants import ECOSYSTEM_ID,PROVIDER_ID
class SalesforceCoreService:
    def status(self): return {"ecosystem_id":ECOSYSTEM_ID,"provider_id":PROVIDER_ID,"product_count":len(list_products()),"domain_count":len(list_domains()),"catalog_available":True,"live_connections_verified":False,"api_transport_in_core":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY"}
    def policy(self): return policy_snapshot()
