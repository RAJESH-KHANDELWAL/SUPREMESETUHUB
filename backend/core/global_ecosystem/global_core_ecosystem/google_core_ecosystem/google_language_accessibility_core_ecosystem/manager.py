"""Manager for the LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class LanguageAccessibilityDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY"


def get_manager() -> LanguageAccessibilityDomainManager:
    return LanguageAccessibilityDomainManager()


__all__ = ["LanguageAccessibilityDomainManager", "get_manager"]
