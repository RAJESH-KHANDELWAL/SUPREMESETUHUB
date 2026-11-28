"""Anthropic Message Batches Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicBatchesCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-BATCHES-CORE-ECOSYSTEM"

__all__=["AnthropicBatchesCoreService"]
