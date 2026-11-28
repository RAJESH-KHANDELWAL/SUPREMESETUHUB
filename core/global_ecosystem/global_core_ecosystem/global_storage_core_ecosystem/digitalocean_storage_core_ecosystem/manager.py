"""Provider-specific Core manager for DigitalOcean storage inventory."""
from ..module_service import StorageProviderCoreService
class DigitaloceanStorageCoreManager(StorageProviderCoreService):
 PROVIDER_ID="digitalocean"
def get_manager()->DigitaloceanStorageCoreManager: return DigitaloceanStorageCoreManager()
