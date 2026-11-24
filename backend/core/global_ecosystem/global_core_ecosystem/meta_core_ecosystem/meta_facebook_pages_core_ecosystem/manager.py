"""Thin metadata adapter; Meta API and ENGINE work remain in their own layers."""
from ..module_service import MetaProductCoreService
class MetaFacebookPagesCoreManager(MetaProductCoreService):
    PRODUCT_ID = "meta_facebook_pages"
