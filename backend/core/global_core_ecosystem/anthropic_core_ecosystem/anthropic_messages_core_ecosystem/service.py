"""Anthropic Messages Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicMessagesCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-MESSAGES-CORE-ECOSYSTEM"

__all__=["AnthropicMessagesCoreService"]
