"""MEGA Storage adapter scaffold for GLOBAL STORAGE ECOSYSTEM.

This module intentionally contains metadata only until an official, authorized
provider API client and its tests are implemented.
"""

from typing import Any


class MegaStorageEcosystem:
    provider_id = "mega_storage"
    display_name = "MEGA Storage"
    capabilities = ("authorized-file-sync",)

    def describe(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "not_configured",
        }
