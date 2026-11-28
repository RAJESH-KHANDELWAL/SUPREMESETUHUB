"""Model API and Inference domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIModelApiAndInferenceDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "MODEL_API_AND_INFERENCE"


def get_manager() -> OpenAIModelApiAndInferenceDomainManager:
    """Return the shared domain runtime bound to Model API and Inference."""
    return OpenAIModelApiAndInferenceDomainManager()
