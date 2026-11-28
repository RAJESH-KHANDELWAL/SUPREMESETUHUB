"""Thin metadata adapter; Meta API and ENGINE work remain in their own layers."""
from ..module_service import MetaProductCoreService
class MetaGraphCoreManager(MetaProductCoreService):
    PRODUCT_ID = "meta_graph_core"
