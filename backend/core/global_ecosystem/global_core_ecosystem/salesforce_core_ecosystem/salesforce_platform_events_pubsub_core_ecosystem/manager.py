"""Platform Events and Pub/Sub metadata facade; no API transport."""
from ..module_service import SalesforceProductCoreService
class ProductManager(SalesforceProductCoreService):
    PRODUCT_ID = "SALESFORCE_PLATFORM_EVENTS_PUBSUB"
def get_manager(): return ProductManager(ProductManager.PRODUCT_ID)
