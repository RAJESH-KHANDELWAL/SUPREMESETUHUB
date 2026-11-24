"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMDb2DatabaseCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_db2_database"
