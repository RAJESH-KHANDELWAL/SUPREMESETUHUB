"""Thin Webhooks CORE adapter; shared catalog/service owns common behavior."""
from ..module_service import HuggingFaceProductCoreService
class HuggingFaceWebhooksCoreManager:
    PRODUCT_ID = "huggingface_webhooks"
    def __init__(self) -> None:
        self._service = HuggingFaceProductCoreService(self.PRODUCT_ID)
    def describe(self) -> dict:
        return self._service.describe()
