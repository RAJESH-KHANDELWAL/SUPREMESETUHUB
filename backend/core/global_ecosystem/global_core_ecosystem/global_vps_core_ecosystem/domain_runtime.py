"""Read-only domain manager shared by VPS capability domains."""
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS
class VPSCoreDomainManager:
 def __init__(self,domain_id:str):
  if domain_id not in DOMAIN_DEFINITIONS:raise KeyError("UNKNOWN_VPS_DOMAIN")
  self.domain_id=domain_id
 def status(self)->dict[str,Any]:return {"success":True,"ecosystem_id":"GLOBAL-VPS-CORE-ECOSYSTEM","domain_id":self.domain_id,**DOMAIN_DEFINITIONS[self.domain_id],"live_execution_enabled":False}
 def list_offerings(self)->dict[str,Any]:
  from .catalog import PROVIDERS
  return {"success":True,"domain_id":self.domain_id,"count":len(PROVIDERS),"provider_ids":[p["provider_id"] for p in PROVIDERS],"catalog_only":True}
