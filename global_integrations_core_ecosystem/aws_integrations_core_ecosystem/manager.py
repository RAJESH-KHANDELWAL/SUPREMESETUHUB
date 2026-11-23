"""Manager for the AWS integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AwsDomainManager(IntegrationDomainManager):
    DOMAIN_ID="AWS"
def get_manager(): return AwsDomainManager()
__all__=["AwsDomainManager","get_manager"]
