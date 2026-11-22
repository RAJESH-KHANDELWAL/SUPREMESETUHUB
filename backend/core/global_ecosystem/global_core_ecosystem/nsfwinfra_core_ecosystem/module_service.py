"""Shared read-only product module service."""
from __future__ import annotations
from typing import Any
from .product_catalog import get_product
class NSFWinfraProductCoreService:
 def __init__(self,product_id:str):
  self.product=get_product(product_id)
  if self.product is None:raise LookupError("NSFWINFRA_PRODUCT_NOT_REGISTERED")
 def status(self)->dict[str,Any]:return {"ecosystem_id":self.product["ecosystem_id"],"status":self.product["status"],"connected":False,"live_connection_verified":False,"api_calls_performed":0}
 def capabilities(self)->dict[str,Any]:return {"ecosystem_id":self.product["ecosystem_id"],"capabilities":list(self.product["capabilities"]),"domains":list(self.product["domains"])}
 def authorize_capability(self,capability:str,context:Any)->dict[str,Any]:
  from .policy import NSFWinfraCorePolicy
  try:
   NSFWinfraCorePolicy.require_tenant_context(context);NSFWinfraCorePolicy.validate_capability(self.product,capability)
   return {"success":True,"status":"METADATA_POLICY_ACCEPTED","data":{"capability":capability,"classification":NSFWinfraCorePolicy.classify_capability(capability),"execution_performed":False}}
  except (ValueError,PermissionError) as exc:return {"success":False,"status":"POLICY_REJECTED","errors":[str(exc)]}
