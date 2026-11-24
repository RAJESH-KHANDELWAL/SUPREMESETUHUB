"""Public Global Tools Core service."""
from .catalog import get_catalog
from .orchestrator import GlobalToolsCoreOrchestrator
class GlobalToolsCoreService:
 def __init__(self): self.core=GlobalToolsCoreOrchestrator()
 def status(self):
  c=get_catalog(); h=self.core.health()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":c["name"],"status":c["status"],"provider_count":h["provider_count"],"product_family_count":h["product_family_count"],"domain_count":h["domain_count"],"live_connections_verified":False,"api_transport_in_core":False,"health":h}
