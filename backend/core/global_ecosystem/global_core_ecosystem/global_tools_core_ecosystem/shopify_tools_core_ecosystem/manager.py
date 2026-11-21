"""shopify provider metadata facade; no API transport."""
from ..module_service import ToolProviderCoreService
class ProviderManager(ToolProviderCoreService):
 PROVIDER_ID="shopify"
def get_manager(): return ProviderManager()
