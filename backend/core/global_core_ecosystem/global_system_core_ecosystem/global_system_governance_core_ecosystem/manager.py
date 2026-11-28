"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class SystemGovernanceSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "SYSTEM_GOVERNANCE"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> SystemGovernanceSystemCoreDomainManager:
    return SystemGovernanceSystemCoreDomainManager()
