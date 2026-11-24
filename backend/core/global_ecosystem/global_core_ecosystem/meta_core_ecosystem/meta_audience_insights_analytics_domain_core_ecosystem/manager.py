"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaAudienceInsightsAnalyticsCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("AUDIENCE_INSIGHTS_ANALYTICS")
