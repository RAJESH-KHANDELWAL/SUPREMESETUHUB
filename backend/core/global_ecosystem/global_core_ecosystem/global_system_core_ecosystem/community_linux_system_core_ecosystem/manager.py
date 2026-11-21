"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class CommunityLinuxSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "community_linux"

def get_manager() -> CommunityLinuxSystemCoreManager:
    return CommunityLinuxSystemCoreManager()
