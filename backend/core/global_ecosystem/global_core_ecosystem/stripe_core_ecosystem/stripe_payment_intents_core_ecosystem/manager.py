"""Stripe Payment Intents product Core manager."""
from ..module_service import get_product_service
class StripePaymentIntentsCoreManager:
 API_FAMILY="payment_intents"
 ECOSYSTEM_ID="STRIPE-PAYMENT-INTENTS-CORE-ECOSYSTEM"
 def __init__(self):self._service=get_product_service(self.API_FAMILY)
 def status(self):return self._service.status()
 def metadata(self):return self._service.metadata()
 def capabilities(self):return self._service.capabilities()
 def validate_capability(self,capability):return self._service.validate_capability(capability)
def get_manager():return StripePaymentIntentsCoreManager()
__all__=["StripePaymentIntentsCoreManager","get_manager"]
