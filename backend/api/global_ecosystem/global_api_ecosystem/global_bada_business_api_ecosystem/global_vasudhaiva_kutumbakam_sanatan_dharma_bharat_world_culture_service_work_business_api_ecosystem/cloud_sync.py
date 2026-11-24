"""Remote synchronization delegated to the independent CLOUD layer."""
from __future__ import annotations

from typing import Any


class CultureServiceWorkBusinessCloudSync:
    def __init__(self, cloud: Any) -> None:
        self.cloud = cloud

    def status(self) -> dict[str, Any]:
        return self.cloud.status()

    def sync(self, payload: dict[str, Any]) -> Any:
        if not isinstance(payload, dict):
            raise ValueError("CLOUD_SYNC_PAYLOAD_MUST_BE_OBJECT")
        return self.cloud.sync(payload)
