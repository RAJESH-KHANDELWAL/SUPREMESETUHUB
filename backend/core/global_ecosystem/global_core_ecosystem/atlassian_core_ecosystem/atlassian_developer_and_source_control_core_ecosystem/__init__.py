"""Atlassian Developer and Source Control domain package."""
DOMAIN_ID="DEVELOPER_AND_SOURCE_CONTROL"
from .manager import AtlassianDomainManager,get_manager
__all__=["DOMAIN_ID","AtlassianDomainManager","get_manager"]
