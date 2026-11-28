"""Read-only domain manager for Backup and Recovery."""
from ..domain_runtime import StorageCoreDomainManager
class BackupAndRecoveryManager(StorageCoreDomainManager):
 DOMAIN_ID="BACKUP_AND_RECOVERY"
def get_manager()->BackupAndRecoveryManager: return BackupAndRecoveryManager()
