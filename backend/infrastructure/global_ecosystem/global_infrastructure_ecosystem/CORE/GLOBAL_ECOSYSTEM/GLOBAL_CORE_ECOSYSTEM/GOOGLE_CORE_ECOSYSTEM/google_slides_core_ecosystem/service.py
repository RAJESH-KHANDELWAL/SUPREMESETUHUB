"""GOOGLE-SLIDES-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleSlidesCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-SLIDES-CORE-ECOSYSTEM"


__all__ = ["GoogleSlidesCoreService"]
