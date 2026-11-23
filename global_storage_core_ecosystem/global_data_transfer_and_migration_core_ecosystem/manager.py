"""Read-only domain manager for Data Transfer and Migration."""
from ..domain_runtime import StorageCoreDomainManager
class DataTransferAndMigrationManager(StorageCoreDomainManager):
 DOMAIN_ID="DATA_TRANSFER_AND_MIGRATION"
def get_manager()->DataTransferAndMigrationManager: return DataTransferAndMigrationManager()
