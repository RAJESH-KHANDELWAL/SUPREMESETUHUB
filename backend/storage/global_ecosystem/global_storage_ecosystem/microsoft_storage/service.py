"""Azure Blob Storage adapter scaffold for GLOBAL STORAGE ECOSYSTEM.

This module intentionally contains metadata only until an official, authorized
provider API client and its tests are implemented.
"""

from typing import Any


class MicrosoftStorageEcosystem:
    provider_id = "microsoft_storage"
    display_name = "Azure Blob Storage"
    capabilities = ("object-storage",)

    def describe(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "not_configured",
        }
