"""Provider-specific Core manager for Google Cloud storage inventory."""
from ..module_service import StorageProviderCoreService
class GoogleStorageCoreManager(StorageProviderCoreService):
 PROVIDER_ID="google"
def get_manager()->GoogleStorageCoreManager: return GoogleStorageCoreManager()
