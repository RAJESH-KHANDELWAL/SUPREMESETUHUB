"""Shared read-only service for Hugging Face product Core namespaces."""
from .product_catalog import get_product
class HuggingFaceProductCoreService:
    def __init__(self, product_id: str):
        self.product_id = str(product_id).strip().lower()
        if get_product(self.product_id) is None:
            raise ValueError(f"UNKNOWN_HUGGINGFACE_PRODUCT: {self.product_id}")
    def describe(self) -> dict:
        item = get_product(self.product_id)
        return {"success": True, "layer": "CORE", "provider_id": "huggingface", "product": item,
                "live_connection_verified": False, "remote_operations_enabled": False, "api_calls_performed": 0}
