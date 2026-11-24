"""Oracle Object Storage metadata binding; no Oracle API calls are made here."""
from ..module_service import OracleProductCoreService

PRODUCT_ID = "oracle-object-storage"

def get_manager() -> OracleProductCoreService:
    return OracleProductCoreService(PRODUCT_ID)
