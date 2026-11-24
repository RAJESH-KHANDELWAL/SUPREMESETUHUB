"""GOOGLE-ADS-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleAdsCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-ADS-CORE-ECOSYSTEM"


__all__ = ["GoogleAdsCoreService"]
