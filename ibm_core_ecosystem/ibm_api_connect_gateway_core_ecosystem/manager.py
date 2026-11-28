"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMApiConnectGatewayCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_api_connect_gateway"
