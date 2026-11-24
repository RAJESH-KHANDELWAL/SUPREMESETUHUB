"""GOOGLE-CALENDAR-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleCalendarCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-CALENDAR-CORE-ECOSYSTEM"


__all__ = ["GoogleCalendarCoreService"]
