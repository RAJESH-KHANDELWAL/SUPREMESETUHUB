"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class VirtualizationAndHypervisorsSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "VIRTUALIZATION_AND_HYPERVISORS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> VirtualizationAndHypervisorsSystemCoreDomainManager:
    return VirtualizationAndHypervisorsSystemCoreDomainManager()
