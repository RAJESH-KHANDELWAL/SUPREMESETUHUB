"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class UpdatesAndLifecycleSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "UPDATES_AND_LIFECYCLE"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> UpdatesAndLifecycleSystemCoreDomainManager:
    return UpdatesAndLifecycleSystemCoreDomainManager()
