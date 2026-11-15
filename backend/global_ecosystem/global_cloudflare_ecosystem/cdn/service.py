"""Read-only CDN zone configuration inspection."""
from typing import Any
from ..client import CloudflareClient

class CDNService:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def get_zone(self, zone_id: str) -> dict[str, Any]:
        return self.client.get_zone(zone_id)
