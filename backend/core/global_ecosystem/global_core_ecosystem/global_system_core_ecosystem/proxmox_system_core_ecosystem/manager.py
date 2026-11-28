"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class ProxmoxSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "proxmox"

def get_manager() -> ProxmoxSystemCoreManager:
    return ProxmoxSystemCoreManager()
