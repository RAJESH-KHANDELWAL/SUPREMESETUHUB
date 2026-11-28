"""Domain manager entry point for anthropic_managed_agents_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicManagedAgentsCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "MANAGED_AGENT_OPERATIONS"

def get_manager():
    return AnthropicManagedAgentsCoreEcosystemManager()

__all__ = ["get_manager"]
