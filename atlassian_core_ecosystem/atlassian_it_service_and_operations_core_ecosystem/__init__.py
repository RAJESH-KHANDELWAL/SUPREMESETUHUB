"""Atlassian IT Service and Operations domain package."""
DOMAIN_ID="IT_SERVICE_AND_OPERATIONS"
from .manager import AtlassianDomainManager,get_manager
__all__=["DOMAIN_ID","AtlassianDomainManager","get_manager"]
