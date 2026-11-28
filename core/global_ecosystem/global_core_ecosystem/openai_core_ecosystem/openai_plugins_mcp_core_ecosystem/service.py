"""Plugins and MCP product-specific binding to the shared OpenAI Core service."""
from ..module_service import OpenAIProductCoreService


class PluginsMcpCoreService(OpenAIProductCoreService):
    ECOSYSTEM_ID = "OPENAI-PLUGINS-MCP-CORE-ECOSYSTEM"


def get_manager() -> PluginsMcpCoreService:
    """Return the shared Core service bound to Plugins and MCP."""
    return PluginsMcpCoreService()
