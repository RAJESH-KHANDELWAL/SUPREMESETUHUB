"""Domain manager for Mobile and Applications."""
from ..domain_runtime import SoftwareCoreDomainManager
class MobileAndApplicationsManager(SoftwareCoreDomainManager):
    DOMAIN_ID="MOBILE_AND_APPLICATIONS"
def get_manager(): return MobileAndApplicationsManager()
