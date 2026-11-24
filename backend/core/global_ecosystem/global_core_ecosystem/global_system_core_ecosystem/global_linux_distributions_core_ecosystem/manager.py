"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class LinuxDistributionsSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "LINUX_DISTRIBUTIONS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> LinuxDistributionsSystemCoreDomainManager:
    return LinuxDistributionsSystemCoreDomainManager()
