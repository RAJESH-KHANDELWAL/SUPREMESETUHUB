"""Provider-specific entry point for Apple software metadata."""
from ..module_service import SoftwareProviderCoreService
class ProviderManager(SoftwareProviderCoreService):
    PROVIDER_ID="apple"
def get_manager(): return ProviderManager()
