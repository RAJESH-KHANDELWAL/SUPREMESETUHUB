"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class VmwareSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "vmware"

def get_manager() -> VmwareSystemCoreManager:
    return VmwareSystemCoreManager()
