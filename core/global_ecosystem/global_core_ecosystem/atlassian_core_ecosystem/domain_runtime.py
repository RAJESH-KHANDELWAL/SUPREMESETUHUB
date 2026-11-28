"""Read-only shared runtime for Atlassian Core domains."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS,atlassian_domain_summary,list_atlassian_domain_inventory
class AtlassianCoreDomainManager:
 DOMAIN_ID=""
 def __init__(self,domain_id:str|None=None)->None:
  if domain_id is not None:self.DOMAIN_ID=domain_id
  if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:raise ValueError(f"UNKNOWN_ATLASSIAN_CORE_DOMAIN: {self.DOMAIN_ID}")
  self._definition=DOMAIN_DEFINITIONS[self.DOMAIN_ID]
 def status(self)->dict[str,Any]:
  row=next(item for item in atlassian_domain_summary()["domains"] if item["domain_id"]==self.DOMAIN_ID)
  return {"success":True,"domain_id":self.DOMAIN_ID,"name":self._definition["name"],"purpose":self._definition["purpose"],"status":"CORE_DOMAIN_AVAILABLE","offering_count":row["offering_count"],"live_connections_verified":0,"api_calls_performed":0}
 def list_offerings(self)->dict[str,Any]:
  rows=[item for item in list_atlassian_domain_inventory() if item["core_domain_id"]==self.DOMAIN_ID]
  return {"success":True,"domain_id":self.DOMAIN_ID,"count":len(rows),"offerings":rows}
 def get_offering(self,offering_id:str)->dict[str,Any]|None:
  needle=offering_id.strip().casefold()
  if not needle:return None
  return next((item for item in list_atlassian_domain_inventory() if item["core_domain_id"]==self.DOMAIN_ID and item["id"].casefold()==needle),None)
__all__=["AtlassianCoreDomainManager"]
