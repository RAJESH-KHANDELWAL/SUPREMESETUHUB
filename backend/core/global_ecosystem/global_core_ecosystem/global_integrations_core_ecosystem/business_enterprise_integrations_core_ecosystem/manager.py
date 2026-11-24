"""Manager for the BUSINESS_ENTERPRISE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class BusinessEnterpriseDomainManager(IntegrationDomainManager):
    DOMAIN_ID="BUSINESS_ENTERPRISE"
def get_manager(): return BusinessEnterpriseDomainManager()
__all__=["BusinessEnterpriseDomainManager","get_manager"]
