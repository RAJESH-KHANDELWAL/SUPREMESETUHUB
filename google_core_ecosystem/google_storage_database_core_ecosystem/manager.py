"""Manager for the STORAGE_DATABASE_AND_DATA Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class StorageDatabaseDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "STORAGE_DATABASE_AND_DATA"


def get_manager() -> StorageDatabaseDomainManager:
    return StorageDatabaseDomainManager()


__all__ = ["StorageDatabaseDomainManager", "get_manager"]
