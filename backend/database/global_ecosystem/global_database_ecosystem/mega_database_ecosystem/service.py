"""MEGA storage metadata. MEGA is treated as a storage service, not a DB engine."""

from typing import Any
from ..provider_base import ProviderDataEcosystem


class MegaDatabaseEcosystem(ProviderDataEcosystem):
    provider_id = "mega"
    display_name = "MEGA Storage Ecosystem"
    capabilities = ("storage-integration", "authorized-file-sync", "sync-metadata")

    def describe(self) -> dict[str, Any]:
        return {"provider_id": self.provider_id, "display_name": self.display_name,
                "capabilities": list(self.capabilities), "connection_status": "not_configured",
                "note": "Use supported and authorized integration methods only."}
