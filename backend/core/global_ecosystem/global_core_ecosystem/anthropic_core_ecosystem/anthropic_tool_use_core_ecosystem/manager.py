"""Domain manager entry point for anthropic_tool_use_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicToolUseCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "TOOL_INTERACTION"

def get_manager():
    return AnthropicToolUseCoreEcosystemManager()

__all__ = ["get_manager"]
