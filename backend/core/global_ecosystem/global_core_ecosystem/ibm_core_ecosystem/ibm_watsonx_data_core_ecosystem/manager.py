"""Thin metadata adapter; API transport and ENGINE execution remain in their own layers."""
from ..module_service import IBMProductCoreService
class IBMWatsonxDataCoreManager(IBMProductCoreService):
    PRODUCT_ID = "ibm_watsonx_data"
