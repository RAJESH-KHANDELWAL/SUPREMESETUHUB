"""Anthropic Managed Agents Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicManagedAgentsCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-MANAGED-AGENTS-CORE-ECOSYSTEM"

__all__=["AnthropicManagedAgentsCoreService"]
