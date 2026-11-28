"""Read-only zone analytics retrieval."""
from typing import Any
from ..client import CloudflareClient

class ObservabilityService:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def zone_analytics(self, zone_id: str, *, since: str, until: str) -> dict[str, Any]:
        zone_id = str(zone_id or "").strip()
        if not zone_id or "/" in zone_id:
            raise ValueError("valid zone_id required")
        if not since or not until:
            raise ValueError("since and until are required")
        return self.client._request(f"/zones/{zone_id}/analytics/dashboard", query={"since": since, "until": until})
