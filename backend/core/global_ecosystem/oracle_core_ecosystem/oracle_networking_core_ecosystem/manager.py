"""Oracle Networking metadata binding; no Oracle API calls are made here."""
from ..module_service import OracleProductCoreService

PRODUCT_ID = "oracle-networking"

def get_manager() -> OracleProductCoreService:
    return OracleProductCoreService(PRODUCT_ID)
