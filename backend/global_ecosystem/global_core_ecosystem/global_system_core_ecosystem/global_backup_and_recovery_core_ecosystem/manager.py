"""Domain facade backed by the shared System Core runtime."""
from ..domain_runtime import SystemCoreDomainManager

class BackupAndRecoverySystemCoreDomainManager(SystemCoreDomainManager):
    DOMAIN_ID = "BACKUP_AND_RECOVERY"
    def __init__(self) -> None:
        super().__init__(self.DOMAIN_ID)

def get_manager() -> BackupAndRecoverySystemCoreDomainManager:
    return BackupAndRecoverySystemCoreDomainManager()
