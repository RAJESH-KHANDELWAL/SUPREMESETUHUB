"""Thin metadata adapter; Meta API and ENGINE work remain in their own layers."""
from ..module_service import MetaProductCoreService
class MetaAiCoreManager(MetaProductCoreService):
    PRODUCT_ID = "meta_meta_ai"
