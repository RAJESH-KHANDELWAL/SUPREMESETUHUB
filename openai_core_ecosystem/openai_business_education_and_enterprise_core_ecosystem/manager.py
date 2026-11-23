"""Business, Education and Enterprise domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIBusinessEducationAndEnterpriseDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "BUSINESS_EDUCATION_AND_ENTERPRISE"


def get_manager() -> OpenAIBusinessEducationAndEnterpriseDomainManager:
    """Return the shared domain runtime bound to Business, Education and Enterprise."""
    return OpenAIBusinessEducationAndEnterpriseDomainManager()
