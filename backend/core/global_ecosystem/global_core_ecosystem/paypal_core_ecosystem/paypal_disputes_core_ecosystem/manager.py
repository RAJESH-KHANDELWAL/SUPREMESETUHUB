"""Product entry point backed by the shared PayPal Core service."""
from ..module_service import PayPalProductCoreService

class PayPalDisputesCoreManager(PayPalProductCoreService):
    ECOSYSTEM_ID = "PAYPAL-DISPUTES-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        super().__init__(self.ECOSYSTEM_ID)
