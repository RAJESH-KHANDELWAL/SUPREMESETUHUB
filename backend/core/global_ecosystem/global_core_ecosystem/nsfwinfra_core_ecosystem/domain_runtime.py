"""Read-only manager for a registered NSFWinfra domain."""
from __future__ import annotations
from .domain_catalog import get_domain_catalog
class NSFWinfraCoreDomainManager:
 def __init__(self,domain_id:str):
  self.domain=get_domain_catalog().get(domain_id)
  if self.domain is None:raise LookupError("NSFWINFRA_DOMAIN_NOT_REGISTERED")
 def inventory(self)->dict:return dict(self.domain)
