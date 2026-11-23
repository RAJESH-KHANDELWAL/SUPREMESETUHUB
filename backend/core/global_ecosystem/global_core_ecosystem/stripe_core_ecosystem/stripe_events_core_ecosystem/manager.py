"""Stripe Events product Core manager."""
from ..module_service import get_product_service
class StripeEventsCoreManager:
 API_FAMILY="events"
 ECOSYSTEM_ID="STRIPE-EVENTS-CORE-ECOSYSTEM"
 def __init__(self):self._service=get_product_service(self.API_FAMILY)
 def status(self):return self._service.status()
 def metadata(self):return self._service.metadata()
 def capabilities(self):return self._service.capabilities()
 def validate_capability(self,capability):return self._service.validate_capability(capability)
def get_manager():return StripeEventsCoreManager()
__all__=["StripeEventsCoreManager","get_manager"]
