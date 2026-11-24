"""Read-only domain manager for Provider Governance."""
from ..domain_runtime import StorageCoreDomainManager
class ProviderGovernanceManager(StorageCoreDomainManager):
 DOMAIN_ID="PROVIDER_GOVERNANCE"
def get_manager()->ProviderGovernanceManager: return ProviderGovernanceManager()
