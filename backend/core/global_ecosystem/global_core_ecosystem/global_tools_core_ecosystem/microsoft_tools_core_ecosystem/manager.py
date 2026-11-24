"""microsoft provider metadata facade; no API transport."""
from ..module_service import ToolProviderCoreService
class ProviderManager(ToolProviderCoreService):
 PROVIDER_ID="microsoft"
def get_manager(): return ProviderManager()
