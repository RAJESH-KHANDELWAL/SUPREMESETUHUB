"""GOOGLE-SHEETS-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleSheetsCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-SHEETS-CORE-ECOSYSTEM"


__all__ = ["GoogleSheetsCoreService"]
