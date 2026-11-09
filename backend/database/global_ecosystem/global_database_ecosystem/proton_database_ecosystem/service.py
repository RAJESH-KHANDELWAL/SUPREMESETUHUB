"""Proton service metadata. Proton is not a general-purpose database engine."""

from typing import Any
from ..provider_base import ProviderDataEcosystem


class ProtonDatabaseEcosystem(ProviderDataEcosystem):
    provider_id = "proton"
    display_name = "Proton Privacy Services Ecosystem"
    capabilities = ("authorized-service-integration", "privacy-aware-metadata")

    def describe(self) -> dict[str, Any]:
        return {"provider_id": self.provider_id, "display_name": self.display_name,
                "capabilities": list(self.capabilities), "connection_status": "not_configured",
                "note": "Only officially supported APIs or authorized integration methods will be used."}
