"""Domain manager for Licensing Support and Interoperability."""
from ..domain_runtime import SoftwareCoreDomainManager
class LicensingSupportAndInteroperabilityManager(SoftwareCoreDomainManager):
    DOMAIN_ID="LICENSING_SUPPORT_AND_INTEROPERABILITY"
def get_manager(): return LicensingSupportAndInteroperabilityManager()
