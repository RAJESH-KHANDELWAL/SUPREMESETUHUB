"""Manager for the DATING_RELATIONSHIPS integration domain."""
from ..domain_runtime import IntegrationDomainManager
class DatingRelationshipsDomainManager(IntegrationDomainManager):
    DOMAIN_ID="DATING_RELATIONSHIPS"
def get_manager(): return DatingRelationshipsDomainManager()
__all__=["DatingRelationshipsDomainManager","get_manager"]
