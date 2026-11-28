"""GOOGLE-CLOUD-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleCloudCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-CLOUD-CORE-ECOSYSTEM"


__all__ = ["GoogleCloudCoreService"]
