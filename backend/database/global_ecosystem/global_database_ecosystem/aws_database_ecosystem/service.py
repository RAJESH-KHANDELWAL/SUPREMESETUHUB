"""AWS data ecosystem capability metadata; live API work is a later phase."""

from typing import Any
from ..provider_base import ProviderDataEcosystem


class AWSDatabaseEcosystem(ProviderDataEcosystem):
    provider_id = "aws"
    display_name = "AWS Data Ecosystem"
    capabilities = ("iam", "managed-databases", "object-storage", "sync-metadata")

    def describe(self) -> dict[str, Any]:
        return {"provider_id": self.provider_id, "display_name": self.display_name,
                "capabilities": list(self.capabilities), "connection_status": "not_configured"}
