"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class ContainersAndSystemRuntimeSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "CONTAINERS_AND_SYSTEM_RUNTIME"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> ContainersAndSystemRuntimeSystemCoreDomainManager:
    return ContainersAndSystemRuntimeSystemCoreDomainManager()
