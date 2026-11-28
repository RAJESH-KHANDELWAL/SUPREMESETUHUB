"""Provider-specific entry point for Microsoft software metadata."""
from ..module_service import SoftwareProviderCoreService
class ProviderManager(SoftwareProviderCoreService):
    PROVIDER_ID="microsoft"
def get_manager(): return ProviderManager()
