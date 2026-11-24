"""VICETEMPLE website provider metadata adapter; no remote operations."""
from ..module_service import WebsiteProviderCoreService

class ViceTempleWebsiteCoreManager:
    PROVIDER_ID = "vicetemple"

    def __init__(self) -> None:
        self._service = WebsiteProviderCoreService(self.PROVIDER_ID)

    def describe(self) -> dict:
        return self._service.describe()
