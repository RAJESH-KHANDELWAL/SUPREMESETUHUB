"""Shared provider-scoped, read-only Core service."""
from __future__ import annotations
from typing import Any
from .catalog import get_storage_provider
from .policy import StorageCorePolicy
class StorageProviderCoreService:
 PROVIDER_ID=""
 def __init__(self):
  if not self.PROVIDER_ID: raise NotImplementedError("PROVIDER_ID_REQUIRED")
  self.provider=get_storage_provider(self.PROVIDER_ID)
  if self.provider is None: raise LookupError(f"STORAGE_PROVIDER_NOT_REGISTERED: {self.PROVIDER_ID}")
 def status(self)->dict[str,Any]:
  return {"success":True,**StorageCorePolicy.safe_provider_summary(self.provider),"api_transport_in_core":False,"live_connection_verified":False,"storage_operations_performed":0}
 def list_products(self)->dict[str,Any]:
  from .product_catalog import list_storage_products
  items=list_storage_products(provider_id=self.PROVIDER_ID)
  return {"success":True,"provider_id":self.PROVIDER_ID,"count":len(items),"products":items}
