"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMResourceControllerCatalogCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_resource_controller_catalog"
