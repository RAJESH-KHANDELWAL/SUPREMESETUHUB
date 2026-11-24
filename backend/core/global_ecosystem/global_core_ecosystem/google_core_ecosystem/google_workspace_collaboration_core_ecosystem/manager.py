"""Manager for the WORKSPACE_AND_COLLABORATION Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class WorkspaceCollaborationDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "WORKSPACE_AND_COLLABORATION"


def get_manager() -> WorkspaceCollaborationDomainManager:
    return WorkspaceCollaborationDomainManager()


__all__ = ["WorkspaceCollaborationDomainManager", "get_manager"]
