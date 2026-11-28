"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaWhatsappBusinessMessagingCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("WHATSAPP_BUSINESS_MESSAGING")
