"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class GoogleSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "google"

def get_manager() -> GoogleSystemCoreManager:
    return GoogleSystemCoreManager()
