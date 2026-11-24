"""Manager for the Storage and Data Management AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class StorageAndDataManagementDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="STORAGE_AND_DATA_MANAGEMENT"
def get_manager()->StorageAndDataManagementDomainManager:return StorageAndDataManagementDomainManager()
__all__=["StorageAndDataManagementDomainManager","get_manager"]
