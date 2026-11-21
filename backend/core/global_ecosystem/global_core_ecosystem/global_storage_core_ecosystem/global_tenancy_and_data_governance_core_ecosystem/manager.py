"""Read-only domain manager for Tenancy and Data Governance."""
from ..domain_runtime import StorageCoreDomainManager
class TenancyAndDataGovernanceManager(StorageCoreDomainManager):
 DOMAIN_ID="TENANCY_AND_DATA_GOVERNANCE"
def get_manager()->TenancyAndDataGovernanceManager: return TenancyAndDataGovernanceManager()
