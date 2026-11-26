"""Read-only domain manager for Edge and Hybrid Storage."""
from ..domain_runtime import StorageCoreDomainManager
class EdgeAndHybridStorageManager(StorageCoreDomainManager):
 DOMAIN_ID="EDGE_AND_HYBRID_STORAGE"
def get_manager()->EdgeAndHybridStorageManager: return EdgeAndHybridStorageManager()
