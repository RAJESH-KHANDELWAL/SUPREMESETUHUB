"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaWebhookEventDeliveryCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("WEBHOOK_EVENT_DELIVERY")
