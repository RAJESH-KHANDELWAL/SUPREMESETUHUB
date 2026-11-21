"""Thin metadata adapter for IBM API Connect and Gateway; transport/execution remain outside CORE."""
from ..module_service import IBMProductCoreService
class IBMApiConnectGatewayCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_api_connect_gateway"
