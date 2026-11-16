"""Anthropic Admin Workspaces Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicAdminWorkspacesCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-ADMIN-WORKSPACES-CORE-ECOSYSTEM"

__all__=["AnthropicAdminWorkspacesCoreService"]
