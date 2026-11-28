"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class MicrosoftSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "microsoft"

def get_manager() -> MicrosoftSystemCoreManager:
    return MicrosoftSystemCoreManager()
