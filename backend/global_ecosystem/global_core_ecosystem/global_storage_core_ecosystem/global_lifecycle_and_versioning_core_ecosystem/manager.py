"""Read-only domain manager for Lifecycle and Versioning."""
from ..domain_runtime import StorageCoreDomainManager
class LifecycleAndVersioningManager(StorageCoreDomainManager):
 DOMAIN_ID="LIFECYCLE_AND_VERSIONING"
def get_manager()->LifecycleAndVersioningManager: return LifecycleAndVersioningManager()
