"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMCodeEngineServerlessCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_code_engine_serverless"
