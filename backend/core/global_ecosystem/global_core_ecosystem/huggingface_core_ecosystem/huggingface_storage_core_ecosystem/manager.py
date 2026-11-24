"""Thin Storage CORE adapter; shared catalog/service owns common behavior."""
from ..module_service import HuggingFaceProductCoreService
class HuggingFaceStorageCoreManager:
    PRODUCT_ID = "huggingface_storage"
    def __init__(self) -> None:
        self._service = HuggingFaceProductCoreService(self.PRODUCT_ID)
    def describe(self) -> dict:
        return self._service.describe()
