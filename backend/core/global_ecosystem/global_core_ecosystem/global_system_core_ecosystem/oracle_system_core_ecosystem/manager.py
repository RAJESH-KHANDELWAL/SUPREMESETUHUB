"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class OracleSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "oracle"

def get_manager() -> OracleSystemCoreManager:
    return OracleSystemCoreManager()
