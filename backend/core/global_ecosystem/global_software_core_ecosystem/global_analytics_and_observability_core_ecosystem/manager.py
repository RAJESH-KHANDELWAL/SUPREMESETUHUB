"""Domain manager for Analytics and Observability."""
from ..domain_runtime import SoftwareCoreDomainManager
class AnalyticsAndObservabilityManager(SoftwareCoreDomainManager):
    DOMAIN_ID="ANALYTICS_AND_OBSERVABILITY"
def get_manager(): return AnalyticsAndObservabilityManager()
