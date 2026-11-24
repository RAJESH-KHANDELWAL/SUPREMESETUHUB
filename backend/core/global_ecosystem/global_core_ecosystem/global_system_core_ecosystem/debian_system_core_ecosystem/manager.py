"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class DebianSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "debian"

def get_manager() -> DebianSystemCoreManager:
    return DebianSystemCoreManager()
