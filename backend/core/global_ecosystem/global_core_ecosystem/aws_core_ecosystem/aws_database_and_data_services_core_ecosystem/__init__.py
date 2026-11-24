"""Database and Data Services AWS Core domain package."""
from .manager import DatabaseAndDataServicesDomainManager,get_manager
DOMAIN_ID="DATABASE_AND_DATA_SERVICES"
__all__=["DOMAIN_ID","DatabaseAndDataServicesDomainManager","get_manager"]
