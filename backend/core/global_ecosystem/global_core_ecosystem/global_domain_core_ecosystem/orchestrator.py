"""Metadata-only provider lookup and request classification."""

from .service import GlobalDomainCoreService


class GlobalDomainCoreOrchestrator:
    def __init__(self, service=None):
        self.service = service or GlobalDomainCoreService()

    def dispatch(self, *, provider_id: str, operation: str, metadata=None):
        return self.service.plan_metadata_operation(
            provider_id=provider_id, operation=operation, metadata=metadata
        )
