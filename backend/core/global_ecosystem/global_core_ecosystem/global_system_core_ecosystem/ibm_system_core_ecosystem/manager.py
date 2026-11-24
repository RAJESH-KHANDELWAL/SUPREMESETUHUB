"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class IbmSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "ibm"

def get_manager() -> IbmSystemCoreManager:
    return IbmSystemCoreManager()
