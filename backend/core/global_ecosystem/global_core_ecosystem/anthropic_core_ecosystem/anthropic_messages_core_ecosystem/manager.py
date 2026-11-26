"""Domain manager entry point for anthropic_messages_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicMessagesCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "MESSAGING_AND_CONVERSATION"

def get_manager():
    return AnthropicMessagesCoreEcosystemManager()

__all__ = ["get_manager"]
