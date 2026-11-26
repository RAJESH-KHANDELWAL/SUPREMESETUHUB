"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class KernelsAndBootSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "KERNELS_AND_BOOT"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> KernelsAndBootSystemCoreDomainManager:
    return KernelsAndBootSystemCoreDomainManager()
