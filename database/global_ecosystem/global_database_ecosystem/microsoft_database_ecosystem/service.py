"""Microsoft data ecosystem capability metadata; live API work is a later phase."""

from typing import Any
from ..provider_base import ProviderDataEcosystem


class MicrosoftDatabaseEcosystem(ProviderDataEcosystem):
    provider_id = "microsoft"
    display_name = "Microsoft Data Ecosystem"
    capabilities = ("oauth2", "azure-databases", "graph-api", "sync-metadata")

    def describe(self) -> dict[str, Any]:
        return {"provider_id": self.provider_id, "display_name": self.display_name,
                "capabilities": list(self.capabilities), "connection_status": "not_configured"}
