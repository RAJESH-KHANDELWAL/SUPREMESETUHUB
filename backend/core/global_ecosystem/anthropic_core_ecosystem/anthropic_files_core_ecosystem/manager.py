"""Domain manager entry point for anthropic_files_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicFilesCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "FILE_ASSETS"

def get_manager():
    return AnthropicFilesCoreEcosystemManager()

__all__ = ["get_manager"]
