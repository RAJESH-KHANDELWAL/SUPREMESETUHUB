"""Domain manager entry point for anthropic_models_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicModelsCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "MODEL_DISCOVERY_AND_METADATA"

def get_manager():
    return AnthropicModelsCoreEcosystemManager()

__all__ = ["get_manager"]
