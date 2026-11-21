"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class AppleSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "apple"

def get_manager() -> AppleSystemCoreManager:
    return AppleSystemCoreManager()
