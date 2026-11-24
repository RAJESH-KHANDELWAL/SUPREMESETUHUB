"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class SuseSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "suse"

def get_manager() -> SuseSystemCoreManager:
    return SuseSystemCoreManager()
