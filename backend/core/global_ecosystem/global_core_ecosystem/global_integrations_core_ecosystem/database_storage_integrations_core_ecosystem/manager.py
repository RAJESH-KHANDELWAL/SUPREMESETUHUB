"""Manager for the DATABASE_STORAGE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class DatabaseStorageDomainManager(IntegrationDomainManager):
    DOMAIN_ID="DATABASE_STORAGE"
def get_manager(): return DatabaseStorageDomainManager()
__all__=["DatabaseStorageDomainManager","get_manager"]
