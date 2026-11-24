"""Provider-specific entry point for Adobe software metadata."""
from ..module_service import SoftwareProviderCoreService
class ProviderManager(SoftwareProviderCoreService):
    PROVIDER_ID="adobe"
def get_manager(): return ProviderManager()
