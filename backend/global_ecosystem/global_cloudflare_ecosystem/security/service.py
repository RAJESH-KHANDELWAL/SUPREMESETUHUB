"""Read-only Cloudflare security ruleset inventory."""
from typing import Any
from ..client import CloudflareClient

class SecurityService:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def list_zone_rulesets(self, zone_id: str) -> dict[str, Any]:
        zone_id = str(zone_id or "").strip()
        if not zone_id or "/" in zone_id:
            raise ValueError("valid zone_id required")
        return self.client._request(f"/zones/{zone_id}/rulesets")
