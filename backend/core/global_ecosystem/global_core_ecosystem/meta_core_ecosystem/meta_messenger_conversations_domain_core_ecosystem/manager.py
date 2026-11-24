"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaMessengerConversationsCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("MESSENGER_CONVERSATIONS")
