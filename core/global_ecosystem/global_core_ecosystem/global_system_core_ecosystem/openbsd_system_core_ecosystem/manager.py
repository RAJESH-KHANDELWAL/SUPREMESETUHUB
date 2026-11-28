"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class OpenbsdSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "openbsd"

def get_manager() -> OpenbsdSystemCoreManager:
    return OpenbsdSystemCoreManager()
