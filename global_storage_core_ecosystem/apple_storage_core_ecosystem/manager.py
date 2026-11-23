"""Provider-specific Core manager for Apple storage inventory."""
from ..module_service import StorageProviderCoreService
class AppleStorageCoreManager(StorageProviderCoreService):
 PROVIDER_ID="apple"
def get_manager()->AppleStorageCoreManager: return AppleStorageCoreManager()
