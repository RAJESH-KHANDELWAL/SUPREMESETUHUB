"""slack provider metadata facade; no API transport."""
from ..module_service import ToolProviderCoreService
class ProviderManager(ToolProviderCoreService):
 PROVIDER_ID="slack"
def get_manager(): return ProviderManager()
