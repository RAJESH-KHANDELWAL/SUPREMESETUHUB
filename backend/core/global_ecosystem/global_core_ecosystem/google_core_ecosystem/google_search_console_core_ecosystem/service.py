"""GOOGLE-SEARCH-CONSOLE-CORE-ECOSYSTEM product-family Core service."""
from ..module_service import GoogleProductCoreService


class GoogleSearchConsoleCoreService(GoogleProductCoreService):
    ECOSYSTEM_ID = "GOOGLE-SEARCH-CONSOLE-CORE-ECOSYSTEM"


__all__ = ["GoogleSearchConsoleCoreService"]
