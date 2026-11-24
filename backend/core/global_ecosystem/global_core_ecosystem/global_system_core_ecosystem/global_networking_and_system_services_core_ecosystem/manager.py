"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class NetworkingAndSystemServicesSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "NETWORKING_AND_SYSTEM_SERVICES"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> NetworkingAndSystemServicesSystemCoreDomainManager:
    return NetworkingAndSystemServicesSystemCoreDomainManager()
