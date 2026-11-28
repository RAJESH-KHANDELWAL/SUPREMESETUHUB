"""Oracle Compute Instances metadata binding; no Oracle API calls are made here."""
from ..module_service import OracleProductCoreService

PRODUCT_ID = "oracle-compute-instances"

def get_manager() -> OracleProductCoreService:
    return OracleProductCoreService(PRODUCT_ID)
