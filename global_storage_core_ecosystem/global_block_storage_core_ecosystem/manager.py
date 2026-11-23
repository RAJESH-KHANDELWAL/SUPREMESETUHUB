"""Read-only domain manager for Block Storage."""
from ..domain_runtime import StorageCoreDomainManager
class BlockStorageManager(StorageCoreDomainManager):
 DOMAIN_ID="BLOCK_STORAGE"
def get_manager()->BlockStorageManager: return BlockStorageManager()
