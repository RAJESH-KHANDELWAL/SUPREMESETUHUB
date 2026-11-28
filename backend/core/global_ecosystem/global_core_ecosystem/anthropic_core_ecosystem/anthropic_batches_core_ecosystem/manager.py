"""Domain manager entry point for anthropic_batches_core_ecosystem."""
from ..domain_runtime import AnthropicCoreDomainManager

class AnthropicBatchesCoreEcosystemManager(AnthropicCoreDomainManager):
    DOMAIN_ID = "BATCH_PROCESSING"

def get_manager():
    return AnthropicBatchesCoreEcosystemManager()

__all__ = ["get_manager"]
