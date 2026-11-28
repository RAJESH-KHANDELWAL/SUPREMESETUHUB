"""IDENTITY ACCESS AND ADMIN Google Core domain package."""
from .manager import IdentityAccessDomainManager, get_manager

DOMAIN_ID = "IDENTITY_ACCESS_AND_ADMIN"
__all__ = ["DOMAIN_ID", "IdentityAccessDomainManager", "get_manager"]
