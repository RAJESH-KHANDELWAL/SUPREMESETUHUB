"""GOOGLE-CHAT-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleChatCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-CHAT-CORE-ECOSYSTEM"


__all__ = ["GoogleChatCoreService"]
