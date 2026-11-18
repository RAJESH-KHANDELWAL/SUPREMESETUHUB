"""GOOGLE-DOCS-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleDocsCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-DOCS-CORE-ECOSYSTEM"


__all__ = ["GoogleDocsCoreService"]
