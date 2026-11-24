"""Composite Requests metadata facade; no API transport."""
from ..module_service import SalesforceProductCoreService
class ProductManager(SalesforceProductCoreService):
    PRODUCT_ID = "SALESFORCE_COMPOSITE"
def get_manager(): return ProductManager(ProductManager.PRODUCT_ID)
