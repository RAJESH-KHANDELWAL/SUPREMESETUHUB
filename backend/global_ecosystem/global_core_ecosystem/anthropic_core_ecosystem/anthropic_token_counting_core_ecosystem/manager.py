"""Domain manager entry point for anthropic_token_counting_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicTokenCountingCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "TOKEN_ACCOUNTING"

def get_manager():
    return AnthropicTokenCountingCoreEcosystemManager()

__all__ = ["get_manager"]
