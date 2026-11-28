"""Shared read-only domain discovery manager."""
from .domain_catalog import DOMAIN_DEFINITIONS,list_domains,CATEGORY_TO_DOMAIN
from .product_catalog import list_products
class ToolsCoreDomainManager:
 def __init__(self,domain_id):
  self.domain_id=domain_id.strip().upper()
  if self.domain_id not in DOMAIN_DEFINITIONS: raise KeyError("UNKNOWN_TOOLS_CORE_DOMAIN")
 def status(self): return next(x for x in list_domains() if x["domain_id"]==self.domain_id)
 def list_offerings(self):
  r=[x for x in list_products() if CATEGORY_TO_DOMAIN.get(x["category"],"PROVIDER_GOVERNANCE")==self.domain_id]
  return {"success":True,"domain_id":self.domain_id,"count":len(r),"offerings":r}
