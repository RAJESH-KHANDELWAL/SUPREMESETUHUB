"""Google Cloud adapter scaffold for GLOBAL CLOUD ECOSYSTEM.

This module intentionally contains metadata only until an official, authorized
provider API client and its tests are implemented.
"""

from typing import Any


class GoogleCloudEcosystem:
    provider_id = "google_cloud"
    display_name = "Google Cloud"
    capabilities = ("cloud-compute-and-data-services",)

    def describe(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "not_configured",
        }
