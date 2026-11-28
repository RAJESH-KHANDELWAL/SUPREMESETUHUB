"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class FreebsdSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "freebsd"

def get_manager() -> FreebsdSystemCoreManager:
    return FreebsdSystemCoreManager()
