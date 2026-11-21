"""Read-only domain manager for Object Storage."""
from ..domain_runtime import StorageCoreDomainManager
class ObjectStorageManager(StorageCoreDomainManager):
 DOMAIN_ID="OBJECT_STORAGE"
def get_manager()->ObjectStorageManager: return ObjectStorageManager()
