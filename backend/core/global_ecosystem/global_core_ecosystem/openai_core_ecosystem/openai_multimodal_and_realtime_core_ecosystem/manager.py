"""Multimodal and Realtime domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIMultimodalAndRealtimeDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "MULTIMODAL_AND_REALTIME"


def get_manager() -> OpenAIMultimodalAndRealtimeDomainManager:
    """Return the shared domain runtime bound to Multimodal and Realtime."""
    return OpenAIMultimodalAndRealtimeDomainManager()
