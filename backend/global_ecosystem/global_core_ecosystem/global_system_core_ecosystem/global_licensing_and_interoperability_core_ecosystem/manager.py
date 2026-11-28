"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class LicensingAndInteroperabilitySystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "LICENSING_AND_INTEROPERABILITY"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> LicensingAndInteroperabilitySystemCoreDomainManager:
    return LicensingAndInteroperabilitySystemCoreDomainManager()
