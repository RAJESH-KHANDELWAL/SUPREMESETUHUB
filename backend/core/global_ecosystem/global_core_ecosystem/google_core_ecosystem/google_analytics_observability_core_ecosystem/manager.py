"""Manager for the ANALYTICS_AND_OBSERVABILITY Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class AnalyticsObservabilityDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "ANALYTICS_AND_OBSERVABILITY"


def get_manager() -> AnalyticsObservabilityDomainManager:
    return AnalyticsObservabilityDomainManager()


__all__ = ["AnalyticsObservabilityDomainManager", "get_manager"]
