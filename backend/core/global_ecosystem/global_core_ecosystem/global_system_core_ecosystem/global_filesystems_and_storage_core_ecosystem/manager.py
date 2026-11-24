"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class FilesystemsAndStorageSystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "FILESYSTEMS_AND_STORAGE"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> FilesystemsAndStorageSystemCoreDomainManager:
    return FilesystemsAndStorageSystemCoreDomainManager()
