"""Anthropic Token Counting Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicTokenCountingCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-TOKEN-COUNTING-CORE-ECOSYSTEM"

__all__=["AnthropicTokenCountingCoreService"]
