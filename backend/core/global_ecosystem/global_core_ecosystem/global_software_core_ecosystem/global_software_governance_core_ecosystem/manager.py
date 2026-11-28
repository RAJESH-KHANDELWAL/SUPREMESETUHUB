"""Domain manager for Software Governance."""
from ..domain_runtime import SoftwareCoreDomainManager
class SoftwareGovernanceManager(SoftwareCoreDomainManager):
    DOMAIN_ID="SOFTWARE_GOVERNANCE"
def get_manager(): return SoftwareGovernanceManager()
