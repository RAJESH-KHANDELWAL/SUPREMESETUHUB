"""Shared read-only runtime for AWS Core domains."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS,aws_domain_summary,list_aws_domain_offerings
class AwsCoreDomainManager:
 DOMAIN_ID=""
 def __init__(self,domain_id:str|None=None)->None:
  if domain_id is not None:self.DOMAIN_ID=domain_id
  if self.DOMAIN_ID not in DOMAIN_DEFINITIONS:raise ValueError(f"UNKNOWN_AWS_CORE_DOMAIN: {self.DOMAIN_ID}")
  self._definition=DOMAIN_DEFINITIONS[self.DOMAIN_ID]
 def status(self)->dict[str,Any]:
  item=next(row for row in aws_domain_summary()["domains"] if row["domain_id"]==self.DOMAIN_ID)
  return {"success":True,"domain_id":self.DOMAIN_ID,"name":self._definition["name"],"purpose":self._definition["purpose"],"status":"CORE_DOMAIN_AVAILABLE","offering_count":item["offering_count"],"live_connections_verified":0,"api_calls_performed":0}
 def list_offerings(self)->dict[str,Any]:
  items=[item for item in list_aws_domain_offerings() if item["core_domain_id"]==self.DOMAIN_ID]
  return {"success":True,"domain_id":self.DOMAIN_ID,"count":len(items),"offerings":items}
 def get_offering(self,offering_id:str)->dict[str,Any]|None:
  needle=offering_id.strip().casefold()
  if not needle:return None
  return next((item for item in list_aws_domain_offerings() if item["core_domain_id"]==self.DOMAIN_ID and item["id"].casefold()==needle),None)
__all__=["AwsCoreDomainManager"]
