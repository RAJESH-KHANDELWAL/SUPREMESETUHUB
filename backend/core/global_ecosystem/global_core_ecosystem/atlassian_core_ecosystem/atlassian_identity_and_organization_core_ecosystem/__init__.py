"""Atlassian Identity and Organization domain package."""
DOMAIN_ID="IDENTITY_AND_ORGANIZATION"
from .manager import AtlassianDomainManager,get_manager
__all__=["DOMAIN_ID","AtlassianDomainManager","get_manager"]
