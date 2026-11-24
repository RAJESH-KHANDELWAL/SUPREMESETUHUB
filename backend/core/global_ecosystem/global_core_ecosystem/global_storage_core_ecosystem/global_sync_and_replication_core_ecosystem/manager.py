"""Read-only domain manager for Sync and Replication."""
from ..domain_runtime import StorageCoreDomainManager
class SyncAndReplicationManager(StorageCoreDomainManager):
 DOMAIN_ID="SYNC_AND_REPLICATION"
def get_manager()->SyncAndReplicationManager: return SyncAndReplicationManager()
