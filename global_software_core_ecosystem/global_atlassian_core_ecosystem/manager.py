"""Provider-specific entry point for Atlassian software metadata."""
from ..module_service import SoftwareProviderCoreService
class ProviderManager(SoftwareProviderCoreService):
    PROVIDER_ID="atlassian"
def get_manager(): return ProviderManager()
