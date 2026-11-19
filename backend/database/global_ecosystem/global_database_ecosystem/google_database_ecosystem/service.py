"""Google data ecosystem capability metadata; live OAuth/API work is a later phase."""

from typing import Any
from ..provider_base import ProviderDataEcosystem


class GoogleDatabaseEcosystem(ProviderDataEcosystem):
    provider_id = "google"
    display_name = "Google Data Ecosystem"
    capabilities = ("oauth2", "cloud-databases", "data-apis", "sync-metadata")

    def describe(self) -> dict[str, Any]:
        return {"provider_id": self.provider_id, "display_name": self.display_name,
                "capabilities": list(self.capabilities), "connection_status": "not_configured"}
