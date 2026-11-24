"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class CanonicalSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "canonical"

def get_manager() -> CanonicalSystemCoreManager:
    return CanonicalSystemCoreManager()
