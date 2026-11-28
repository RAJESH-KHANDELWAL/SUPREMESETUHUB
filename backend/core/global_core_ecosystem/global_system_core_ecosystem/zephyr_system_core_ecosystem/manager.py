"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class ZephyrSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "zephyr"

def get_manager() -> ZephyrSystemCoreManager:
    return ZephyrSystemCoreManager()
