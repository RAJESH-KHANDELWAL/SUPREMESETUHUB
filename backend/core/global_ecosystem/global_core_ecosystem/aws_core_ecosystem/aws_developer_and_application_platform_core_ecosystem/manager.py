"""Manager for the Developer and Application Platform AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class DeveloperAndApplicationPlatformDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="DEVELOPER_AND_APPLICATION_PLATFORM"
def get_manager()->DeveloperAndApplicationPlatformDomainManager:return DeveloperAndApplicationPlatformDomainManager()
__all__=["DeveloperAndApplicationPlatformDomainManager","get_manager"]
