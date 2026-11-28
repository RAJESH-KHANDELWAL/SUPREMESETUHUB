"""Domain and Name Services AWS Core domain package."""
from .manager import DomainAndNameServicesDomainManager,get_manager
DOMAIN_ID="DOMAIN_AND_NAME_SERVICES"
__all__=["DOMAIN_ID","DomainAndNameServicesDomainManager","get_manager"]
