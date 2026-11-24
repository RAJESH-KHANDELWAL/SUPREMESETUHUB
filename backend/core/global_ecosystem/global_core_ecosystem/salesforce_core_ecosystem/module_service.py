"""Shared metadata-only product service."""
from .catalog import get_product
class SalesforceProductCoreService:
    def __init__(self,product_id): self.product_id=str(product_id).strip().upper()
    def describe(self):
        item=get_product(self.product_id)
        if item is None: raise KeyError(f"Unknown Salesforce product: {self.product_id}")
        return item
    def status(self):
        item=self.describe(); return {"product_id":item["product_id"],"enabled":item["enabled"],"implementation_mode":item["implementation_mode"],"live_connection_verified":False}
