"""Stripe Tax product Core manager."""
from ..module_service import get_product_service
class StripeTaxCoreManager:
 API_FAMILY="tax"
 ECOSYSTEM_ID="STRIPE-TAX-CORE-ECOSYSTEM"
 def __init__(self):self._service=get_product_service(self.API_FAMILY)
 def status(self):return self._service.status()
 def metadata(self):return self._service.metadata()
 def capabilities(self):return self._service.capabilities()
 def validate_capability(self,capability):return self._service.validate_capability(capability)
def get_manager():return StripeTaxCoreManager()
__all__=["StripeTaxCoreManager","get_manager"]
