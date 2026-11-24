"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class SystemSecurityAndHardeningSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "SYSTEM_SECURITY_AND_HARDENING"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> SystemSecurityAndHardeningSystemCoreDomainManager:
    return SystemSecurityAndHardeningSystemCoreDomainManager()
