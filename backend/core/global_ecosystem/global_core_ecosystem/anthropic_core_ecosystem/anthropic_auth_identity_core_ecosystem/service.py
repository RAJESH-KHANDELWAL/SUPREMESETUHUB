"""Anthropic Authentication and Identity Core service entry point."""
from ..module_service import AnthropicProductCoreService

class AnthropicAuthIdentityCoreService(AnthropicProductCoreService):
    ECOSYSTEM_ID = "ANTHROPIC-AUTH-IDENTITY-CORE-ECOSYSTEM"

__all__=["AnthropicAuthIdentityCoreService"]
