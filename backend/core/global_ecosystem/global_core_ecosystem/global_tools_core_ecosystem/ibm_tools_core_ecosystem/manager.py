"""ibm provider metadata facade; no API transport."""
from ..module_service import ToolProviderCoreService
class ProviderManager(ToolProviderCoreService):
 PROVIDER_ID="ibm"
def get_manager(): return ProviderManager()
