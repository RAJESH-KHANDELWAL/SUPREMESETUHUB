"""Database & Storage domain package."""
from .manager import DatabaseStorageDomainManager, get_manager
DOMAIN_ID="DATABASE_STORAGE"
__all__=["DOMAIN_ID","DatabaseStorageDomainManager","get_manager"]
