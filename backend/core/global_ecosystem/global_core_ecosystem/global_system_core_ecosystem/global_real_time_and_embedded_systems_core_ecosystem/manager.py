"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class RealTimeAndEmbeddedSystemsSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "REAL_TIME_AND_EMBEDDED_SYSTEMS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> RealTimeAndEmbeddedSystemsSystemCoreDomainManager:
    return RealTimeAndEmbeddedSystemsSystemCoreDomainManager()
