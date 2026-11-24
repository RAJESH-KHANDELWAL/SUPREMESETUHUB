"""Manager for the SEARCH_PUBLISHING_AND_DISCOVERY Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class SearchPublishingDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "SEARCH_PUBLISHING_AND_DISCOVERY"


def get_manager() -> SearchPublishingDomainManager:
    return SearchPublishingDomainManager()


__all__ = ["SearchPublishingDomainManager", "get_manager"]
