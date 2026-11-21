"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaGraphPlatformAndObjectModelCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("GRAPH_PLATFORM_AND_OBJECT_MODEL")
