"""GOOGLE-PEOPLE-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GooglePeopleCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-PEOPLE-CORE-ECOSYSTEM"


__all__ = ["GooglePeopleCoreService"]
