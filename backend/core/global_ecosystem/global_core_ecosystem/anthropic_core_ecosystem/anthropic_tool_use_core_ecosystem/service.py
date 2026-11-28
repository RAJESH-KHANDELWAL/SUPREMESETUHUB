"""Anthropic Tool Use Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicToolUseCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-TOOL-USE-CORE-ECOSYSTEM"

__all__=["AnthropicToolUseCoreService"]
