"""Manager for the Database and Data Services AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class DatabaseAndDataServicesDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="DATABASE_AND_DATA_SERVICES"
def get_manager()->DatabaseAndDataServicesDomainManager:return DatabaseAndDataServicesDomainManager()
__all__=["DatabaseAndDataServicesDomainManager","get_manager"]
