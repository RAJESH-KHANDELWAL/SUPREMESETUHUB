"""Domain manager entry point for anthropic_admin_workspaces_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicAdminWorkspacesCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "WORKSPACE_GOVERNANCE"

def get_manager():
    return AnthropicAdminWorkspacesCoreEcosystemManager()

__all__ = ["get_manager"]
