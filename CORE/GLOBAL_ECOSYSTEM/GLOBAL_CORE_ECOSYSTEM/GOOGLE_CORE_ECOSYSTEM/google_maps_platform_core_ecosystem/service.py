"""GOOGLE-MAPS-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleMapsPlatformCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-MAPS-CORE-ECOSYSTEM"


__all__ = ["GoogleMapsPlatformCoreService"]
