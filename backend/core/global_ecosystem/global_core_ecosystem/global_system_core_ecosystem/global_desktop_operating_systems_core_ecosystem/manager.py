"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class DesktopOperatingSystemsSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "DESKTOP_OPERATING_SYSTEMS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> DesktopOperatingSystemsSystemCoreDomainManager:
    return DesktopOperatingSystemsSystemCoreDomainManager()
