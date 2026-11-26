"""Provider-scoped read-only facade."""
from ..module_service import SystemProviderCoreService

class AmazonSystemCoreManager(SystemProviderCoreService):
    PROVIDER_ID = "amazon"

def get_manager() -> AmazonSystemCoreManager:
    return AmazonSystemCoreManager()
