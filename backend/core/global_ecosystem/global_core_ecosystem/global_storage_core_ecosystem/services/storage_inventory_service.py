"""Read-only service facade for storage inventory."""
from __future__ import annotations
from typing import Any
from ..product_catalog import list_storage_products,storage_product_summary
class StorageInventoryService:
 def list_products(self,*,provider_id:str|None=None,domain_id:str|None=None)->dict[str,Any]:
  items=list_storage_products(provider_id=provider_id,domain_id=domain_id)
  return {"success":True,"count":len(items),"products":items}
 def summary(self)->dict[str,Any]: return storage_product_summary()
