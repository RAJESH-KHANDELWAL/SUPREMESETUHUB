"""Read-only domain manager for Sharing and Access."""
from ..domain_runtime import StorageCoreDomainManager
class SharingAndAccessManager(StorageCoreDomainManager):
 DOMAIN_ID="SHARING_AND_ACCESS"
def get_manager()->SharingAndAccessManager: return SharingAndAccessManager()
