"""Provider-specific entry point for GitHub software metadata."""
from ..module_service import SoftwareProviderCoreService
class ProviderManager(SoftwareProviderCoreService):
    PROVIDER_ID="github"
def get_manager(): return ProviderManager()
