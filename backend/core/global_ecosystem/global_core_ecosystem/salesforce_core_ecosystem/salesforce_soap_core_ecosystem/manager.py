"""SOAP API metadata facade; no API transport."""
from ..module_service import SalesforceProductCoreService
class ProductManager(SalesforceProductCoreService):
    PRODUCT_ID = "SALESFORCE_SOAP"
def get_manager(): return ProductManager(ProductManager.PRODUCT_ID)
