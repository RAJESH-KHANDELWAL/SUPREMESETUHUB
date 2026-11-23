"""GOOGLE-MEET-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleMeetCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-MEET-CORE-ECOSYSTEM"


__all__ = ["GoogleMeetCoreService"]
