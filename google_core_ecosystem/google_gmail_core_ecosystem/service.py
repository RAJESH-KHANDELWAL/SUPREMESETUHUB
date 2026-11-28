"""GOOGLE-GMAIL-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleGmailProductCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-GMAIL-CORE-ECOSYSTEM"

    def status(self):
        result = super().status()
        result["provider"] = "google"
        return result


__all__ = ["GoogleGmailProductCoreService"]
