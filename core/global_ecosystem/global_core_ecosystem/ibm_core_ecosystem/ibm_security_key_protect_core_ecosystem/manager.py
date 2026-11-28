"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMSecurityKeyProtectCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_security_key_protect"
