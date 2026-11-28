"""Provider-specific Core manager for Microsoft storage inventory."""
from ..module_service import StorageProviderCoreService
class MicrosoftStorageCoreManager(StorageProviderCoreService):
 PROVIDER_ID="microsoft"
def get_manager()->MicrosoftStorageCoreManager: return MicrosoftStorageCoreManager()
