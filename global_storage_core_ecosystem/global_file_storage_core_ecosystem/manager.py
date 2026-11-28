"""Read-only domain manager for File Storage."""
from ..domain_runtime import StorageCoreDomainManager
class FileStorageManager(StorageCoreDomainManager):
 DOMAIN_ID="FILE_STORAGE"
def get_manager()->FileStorageManager: return FileStorageManager()
