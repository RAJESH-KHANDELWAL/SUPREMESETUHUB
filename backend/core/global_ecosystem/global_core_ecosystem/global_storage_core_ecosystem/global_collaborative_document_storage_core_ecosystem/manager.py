"""Read-only domain manager for Collaborative Document Storage."""
from ..domain_runtime import StorageCoreDomainManager
class CollaborativeDocumentStorageManager(StorageCoreDomainManager):
 DOMAIN_ID="COLLABORATIVE_DOCUMENT_STORAGE"
def get_manager()->CollaborativeDocumentStorageManager: return CollaborativeDocumentStorageManager()
