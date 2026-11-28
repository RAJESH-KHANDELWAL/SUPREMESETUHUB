"""Atlassian Provider Governance domain package."""
DOMAIN_ID="PROVIDER_GOVERNANCE"
from .manager import AtlassianDomainManager,get_manager
__all__=["DOMAIN_ID","AtlassianDomainManager","get_manager"]
