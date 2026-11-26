"""Category entry point backed by shared Hosting Core runtime."""
from pathlib import Path
DOMAIN_ID=Path(__file__).resolve().parent.name.removeprefix("global_").removesuffix("_hosting_core_ecosystem").upper()
class HostingDomainManager:
 def status(self):return {"success":True,"domain_id":DOMAIN_ID,"status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_transport_in_core":False}
 def list_providers(self):
  from ..domain_catalog import get_hosting_domain
  return get_hosting_domain(DOMAIN_ID)
def get_manager():return HostingDomainManager()
