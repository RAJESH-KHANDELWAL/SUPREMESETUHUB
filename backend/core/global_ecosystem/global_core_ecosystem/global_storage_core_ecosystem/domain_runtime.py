"""Shared read-only manager for storage domain packages."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS
from .product_catalog import list_storage_products
class StorageCoreDomainManager:
    DOMAIN_ID=""
    def __init__(self,domain_id: str|None=None):
        if domain_id is not None: self.DOMAIN_ID=domain_id
        if self.DOMAIN_ID not in DOMAIN_DEFINITIONS: raise ValueError(f"UNKNOWN_STORAGE_DOMAIN: {self.DOMAIN_ID}")
    def status(self) -> dict[str,Any]:
        item=DOMAIN_DEFINITIONS[self.DOMAIN_ID]
        products=list_storage_products(domain_id=self.DOMAIN_ID)
        return {"success":True,"domain_id":self.DOMAIN_ID,"name":item["name"],"purpose":item["purpose"],"status":"STORAGE_DOMAIN_AVAILABLE","product_count":len(products),"live_connections_verified":0}
    def list_products(self) -> dict[str,Any]:
        items=list_storage_products(domain_id=self.DOMAIN_ID)
        return {"success":True,"domain_id":self.DOMAIN_ID,"count":len(items),"products":items}
