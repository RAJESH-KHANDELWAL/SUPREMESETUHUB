"""Anthropic Models Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicModelsCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-MODELS-CORE-ECOSYSTEM"

__all__=["AnthropicModelsCoreService"]
