"""Anthropic Files Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicFilesCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-FILES-CORE-ECOSYSTEM"

__all__=["AnthropicFilesCoreService"]
