"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMSecretsManagerCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_secrets_manager"
