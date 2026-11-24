"""Extensibility and Tool Integration domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIExtensibilityAndToolIntegrationDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "EXTENSIBILITY_AND_TOOL_INTEGRATION"


def get_manager() -> OpenAIExtensibilityAndToolIntegrationDomainManager:
    """Return the shared domain runtime bound to Extensibility and Tool Integration."""
    return OpenAIExtensibilityAndToolIntegrationDomainManager()
