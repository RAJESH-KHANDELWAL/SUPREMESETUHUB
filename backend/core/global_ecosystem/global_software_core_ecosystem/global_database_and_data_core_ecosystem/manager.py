"""Domain manager for Database and Data."""
from ..domain_runtime import SoftwareCoreDomainManager
class DatabaseAndDataManager(SoftwareCoreDomainManager):
    DOMAIN_ID="DATABASE_AND_DATA"
def get_manager(): return DatabaseAndDataManager()
