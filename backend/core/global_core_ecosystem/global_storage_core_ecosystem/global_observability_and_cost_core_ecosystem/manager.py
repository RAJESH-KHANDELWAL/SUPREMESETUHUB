"""Read-only domain manager for Observability and Cost."""
from ..domain_runtime import StorageCoreDomainManager
class ObservabilityAndCostManager(StorageCoreDomainManager):
 DOMAIN_ID="OBSERVABILITY_AND_COST"
def get_manager()->ObservabilityAndCostManager: return ObservabilityAndCostManager()
