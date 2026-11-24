"""cloudflare provider metadata facade; no API transport."""
from ..module_service import ToolProviderCoreService
class ProviderManager(ToolProviderCoreService):
 PROVIDER_ID="cloudflare"
def get_manager(): return ProviderManager()
