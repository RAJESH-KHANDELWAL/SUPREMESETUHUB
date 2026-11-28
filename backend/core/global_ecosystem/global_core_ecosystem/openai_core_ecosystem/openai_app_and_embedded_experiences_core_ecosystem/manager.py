"""Apps and Embedded Experiences domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIAppAndEmbeddedExperiencesDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "APP_AND_EMBEDDED_EXPERIENCES"


def get_manager() -> OpenAIAppAndEmbeddedExperiencesDomainManager:
    """Return the shared domain runtime bound to Apps and Embedded Experiences."""
    return OpenAIAppAndEmbeddedExperiencesDomainManager()
