"""Provider Governance domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIProviderGovernanceDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "PROVIDER_GOVERNANCE"


def get_manager() -> OpenAIProviderGovernanceDomainManager:
    """Return the shared domain runtime bound to Provider Governance."""
    return OpenAIProviderGovernanceDomainManager()
