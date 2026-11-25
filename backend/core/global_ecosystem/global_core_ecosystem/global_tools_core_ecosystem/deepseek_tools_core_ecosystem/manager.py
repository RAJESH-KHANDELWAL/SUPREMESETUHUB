"""deepseek provider metadata facade; no API transport."""
from ..module_service import ToolProviderCoreService
class ProviderManager(ToolProviderCoreService):
 PROVIDER_ID="deepseek"
def get_manager(): return ProviderManager()
