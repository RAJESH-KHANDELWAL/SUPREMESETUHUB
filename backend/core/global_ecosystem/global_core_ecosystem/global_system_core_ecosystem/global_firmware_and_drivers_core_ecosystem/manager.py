"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class FirmwareAndDriversSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "FIRMWARE_AND_DRIVERS"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> FirmwareAndDriversSystemCoreDomainManager:
    return FirmwareAndDriversSystemCoreDomainManager()
