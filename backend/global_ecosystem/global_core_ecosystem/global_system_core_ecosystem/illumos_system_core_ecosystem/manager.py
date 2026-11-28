"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class IllumosSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "illumos"

def get_manager() -> IllumosSystemCoreManager:
    return IllumosSystemCoreManager()
