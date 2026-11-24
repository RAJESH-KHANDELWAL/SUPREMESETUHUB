"""GOOGLE-DRIVE-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleDriveCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-DRIVE-CORE-ECOSYSTEM"


__all__ = ["GoogleDriveCoreService"]
