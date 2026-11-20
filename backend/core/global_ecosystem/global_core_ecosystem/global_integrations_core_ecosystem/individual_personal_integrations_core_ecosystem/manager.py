"""Manager for the INDIVIDUAL_PERSONAL integration domain."""
from ..domain_runtime import IntegrationDomainManager
class IndividualPersonalDomainManager(IntegrationDomainManager):
    DOMAIN_ID="INDIVIDUAL_PERSONAL"
def get_manager(): return IndividualPersonalDomainManager()
__all__=["IndividualPersonalDomainManager","get_manager"]
