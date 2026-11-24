"""Read-only AWS Storage Core metadata service."""
from typing import Any

from ..catalog import get_storage_provider


class AwsStorageCoreService:
    ECOSYSTEM_ID = "AWS-STORAGE-CORE-ECOSYSTEM"
    PROVIDER_ID = "aws"

    def status(self) -> dict[str, Any]:
        provider = get_storage_provider(self.PROVIDER_ID)
        return {
            "success": provider is not None,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "provider": provider,
            "live_connection_verified": False,
            "storage_operations_performed": 0,
        }
