"""WORKSPACE AND COLLABORATION Google Core domain package."""
from .manager import WorkspaceCollaborationDomainManager, get_manager

DOMAIN_ID = "WORKSPACE_AND_COLLABORATION"
__all__ = ["DOMAIN_ID", "WorkspaceCollaborationDomainManager", "get_manager"]
