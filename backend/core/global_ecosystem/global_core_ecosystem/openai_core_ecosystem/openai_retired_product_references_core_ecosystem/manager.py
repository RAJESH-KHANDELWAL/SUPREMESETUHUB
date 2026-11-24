"""Retired Product References domain manager; implementation is shared at the provider root."""
from ..domain_runtime import OpenAICoreDomainManager


class OpenAIRetiredProductReferencesDomainManager(OpenAICoreDomainManager):
    DOMAIN_ID = "RETIRED_PRODUCT_REFERENCES"


def get_manager() -> OpenAIRetiredProductReferencesDomainManager:
    """Return the shared domain runtime bound to Retired Product References."""
    return OpenAIRetiredProductReferencesDomainManager()
