"""Amazon Web Services adapter scaffold for GLOBAL CLOUD ECOSYSTEM.

This module intentionally contains metadata only until an official, authorized
provider API client and its tests are implemented.
"""

from typing import Any


class AwsCloudEcosystem:
    provider_id = "aws_cloud"
    display_name = "Amazon Web Services"
    capabilities = ("cloud-compute-and-data-services",)

    def describe(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "not_configured",
        }
