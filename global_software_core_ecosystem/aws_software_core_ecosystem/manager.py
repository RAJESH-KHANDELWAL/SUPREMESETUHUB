"""Provider-specific entry point for Amazon Web Services software metadata."""
from ..module_service import SoftwareProviderCoreService
class ProviderManager(SoftwareProviderCoreService):
    PROVIDER_ID="aws"
def get_manager(): return ProviderManager()
