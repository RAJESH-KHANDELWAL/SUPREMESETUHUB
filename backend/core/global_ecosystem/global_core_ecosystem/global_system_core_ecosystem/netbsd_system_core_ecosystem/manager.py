"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class NetbsdSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "netbsd"

def get_manager() -> NetbsdSystemCoreManager:
    return NetbsdSystemCoreManager()
