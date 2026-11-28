"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMCloudPlatformCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_cloud_platform"
