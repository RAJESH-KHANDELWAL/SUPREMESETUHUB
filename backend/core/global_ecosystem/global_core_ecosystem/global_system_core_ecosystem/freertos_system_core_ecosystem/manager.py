"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class FreertosSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "freertos"

def get_manager() -> FreertosSystemCoreManager:
    return FreertosSystemCoreManager()
