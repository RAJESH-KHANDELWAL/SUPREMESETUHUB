"""Google Cloud Storage adapter scaffold for GLOBAL STORAGE ECOSYSTEM.

This module intentionally contains metadata only until an official, authorized
provider API client and its tests are implemented.
"""

from typing import Any


class GoogleStorageEcosystem:
    provider_id = "google_storage"
    display_name = "Google Cloud Storage"
    capabilities = ("google-cloud-storage",)

    def describe(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "not_configured",
        }
