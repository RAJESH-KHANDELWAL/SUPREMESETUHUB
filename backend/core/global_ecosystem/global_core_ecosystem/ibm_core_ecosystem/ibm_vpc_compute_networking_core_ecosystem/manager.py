"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMVpcComputeNetworkingCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_vpc_compute_networking"
