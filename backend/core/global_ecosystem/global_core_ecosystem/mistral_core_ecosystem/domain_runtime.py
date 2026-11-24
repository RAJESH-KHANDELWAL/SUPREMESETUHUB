"""Shared read-only domain manager for Mistral capability domains."""
from __future__ import annotations
from typing import Any
from .domain_catalog import list_mistral_domain_inventory

class MistralCoreDomainManager:
 def __init__(self,domain_id:str)->None:
  key=domain_id.strip().upper()
  self.domain=next((x for x in list_mistral_domain_inventory() if x["domain_id"]==key),None)
  if self.domain is None: raise LookupError(f"MISTRAL_DOMAIN_NOT_REGISTERED: {key}")
 def status(self)->dict[str,Any]:
  return {"success":True,**self.domain,"live_connection_verified":False}
 def list_products(self)->dict[str,Any]:
  return {"success":True,"domain_id":self.domain["domain_id"],
   "count":self.domain["product_count"],"products":self.domain["product_ecosystem_ids"]}

__all__=["MistralCoreDomainManager"]
