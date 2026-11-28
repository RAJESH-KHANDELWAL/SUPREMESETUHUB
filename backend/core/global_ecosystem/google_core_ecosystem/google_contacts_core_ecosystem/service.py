"""GOOGLE-CONTACTS-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleContactsCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-CONTACTS-CORE-ECOSYSTEM"


__all__ = ["GoogleContactsCoreService"]
