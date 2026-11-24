"""Atlassian Work Management and Planning domain package."""
DOMAIN_ID="WORK_MANAGEMENT_AND_PLANNING"
from .manager import AtlassianDomainManager,get_manager
__all__=["DOMAIN_ID","AtlassianDomainManager","get_manager"]
