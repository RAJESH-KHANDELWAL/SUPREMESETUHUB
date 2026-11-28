"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class LinuxFoundationSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "linux_foundation"

def get_manager() -> LinuxFoundationSystemCoreManager:
    return LinuxFoundationSystemCoreManager()
