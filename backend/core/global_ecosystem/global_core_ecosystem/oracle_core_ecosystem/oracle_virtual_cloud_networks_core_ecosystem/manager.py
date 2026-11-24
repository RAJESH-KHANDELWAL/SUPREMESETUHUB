"""Oracle Virtual Cloud Networks metadata binding; no Oracle API calls are made here."""
from ..module_service import OracleProductCoreService

PRODUCT_ID = "oracle-virtual-cloud-networks"

def get_manager() -> OracleProductCoreService:
    return OracleProductCoreService(PRODUCT_ID)
