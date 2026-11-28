"""Atlassian Knowledge and Collaboration domain package."""
DOMAIN_ID="KNOWLEDGE_AND_COLLABORATION"
from .manager import AtlassianDomainManager,get_manager
__all__=["DOMAIN_ID","AtlassianDomainManager","get_manager"]
