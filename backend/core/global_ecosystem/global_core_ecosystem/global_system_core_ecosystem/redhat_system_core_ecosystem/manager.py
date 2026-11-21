"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class RedhatSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "redhat"

def get_manager() -> RedhatSystemCoreManager:
    return RedhatSystemCoreManager()
