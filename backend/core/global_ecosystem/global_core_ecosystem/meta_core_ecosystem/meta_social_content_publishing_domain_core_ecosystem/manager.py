"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaSocialContentPublishingCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("SOCIAL_CONTENT_PUBLISHING")
