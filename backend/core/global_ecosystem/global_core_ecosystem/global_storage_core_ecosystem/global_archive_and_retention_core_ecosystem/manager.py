"""Read-only domain manager for Archive and Retention."""
from ..domain_runtime import StorageCoreDomainManager
class ArchiveAndRetentionManager(StorageCoreDomainManager):
 DOMAIN_ID="ARCHIVE_AND_RETENTION"
def get_manager()->ArchiveAndRetentionManager: return ArchiveAndRetentionManager()
