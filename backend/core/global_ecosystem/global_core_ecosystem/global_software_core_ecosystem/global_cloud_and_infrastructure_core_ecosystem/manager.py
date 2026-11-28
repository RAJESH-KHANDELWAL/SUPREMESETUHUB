"""Domain manager for Cloud and Infrastructure."""
from ..domain_runtime import SoftwareCoreDomainManager
class CloudAndInfrastructureManager(SoftwareCoreDomainManager):
    DOMAIN_ID="CLOUD_AND_INFRASTRUCTURE"
def get_manager(): return CloudAndInfrastructureManager()
