"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class UnixAndBsdSystemsSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "UNIX_AND_BSD_SYSTEMS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> UnixAndBsdSystemsSystemCoreDomainManager:
    return UnixAndBsdSystemsSystemCoreDomainManager()
