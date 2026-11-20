"""STORAGE DATABASE AND DATA Google Core domain package."""
from .manager import StorageDatabaseDomainManager, get_manager

DOMAIN_ID = "STORAGE_DATABASE_AND_DATA"
__all__ = ["DOMAIN_ID", "StorageDatabaseDomainManager", "get_manager"]
