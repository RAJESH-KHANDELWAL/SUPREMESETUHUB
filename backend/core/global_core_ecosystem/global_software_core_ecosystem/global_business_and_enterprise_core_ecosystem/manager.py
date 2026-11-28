"""Domain manager for Business and Enterprise."""
from ..domain_runtime import SoftwareCoreDomainManager
class BusinessAndEnterpriseManager(SoftwareCoreDomainManager):
    DOMAIN_ID="BUSINESS_AND_ENTERPRISE"
def get_manager(): return BusinessAndEnterpriseManager()
