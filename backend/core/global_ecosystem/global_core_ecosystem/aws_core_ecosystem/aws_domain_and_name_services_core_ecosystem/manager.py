"""Manager for the Domain and Name Services AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class DomainAndNameServicesDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="DOMAIN_AND_NAME_SERVICES"
def get_manager()->DomainAndNameServicesDomainManager:return DomainAndNameServicesDomainManager()
__all__=["DomainAndNameServicesDomainManager","get_manager"]
