"""Thin metadata adapter; Meta API and ENGINE work remain in their own layers."""
from ..module_service import MetaProductCoreService
class MetaWebhooksCoreManager(MetaProductCoreService):
    PRODUCT_ID = "meta_webhooks"
