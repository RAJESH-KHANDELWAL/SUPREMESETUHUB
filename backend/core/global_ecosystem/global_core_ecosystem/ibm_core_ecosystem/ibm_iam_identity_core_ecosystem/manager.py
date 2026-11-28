"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMIamIdentityCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_iam_identity"
