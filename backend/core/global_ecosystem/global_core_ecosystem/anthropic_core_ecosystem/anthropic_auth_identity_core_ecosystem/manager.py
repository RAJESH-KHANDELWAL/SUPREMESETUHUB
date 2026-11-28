"""Domain manager entry point for anthropic_auth_identity_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicAuthIdentityCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "AUTHENTICATION_AND_IDENTITY"

def get_manager():
    return AnthropicAuthIdentityCoreEcosystemManager()

__all__ = ["get_manager"]
