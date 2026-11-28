"""Provider-specific Core manager for Amazon Web Services storage inventory."""
from ..module_service import StorageProviderCoreService
class AwsStorageCoreManager(StorageProviderCoreService):
 PROVIDER_ID="aws"
def get_manager()->AwsStorageCoreManager: return AwsStorageCoreManager()
