"""Product entry point backed by the shared PayPal Core service."""
from ..module_service import PayPalProductCoreService
class PaypalOrdersCoreManager(PayPalProductCoreService):
    ECOSYSTEM_ID = "PAYPAL-ORDERS-CORE-ECOSYSTEM-CORE-ECOSYSTEM"
    def __init__(self) -> None: super().__init__(self.ECOSYSTEM_ID)
