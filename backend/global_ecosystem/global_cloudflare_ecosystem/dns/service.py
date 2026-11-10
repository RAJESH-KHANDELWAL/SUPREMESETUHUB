"""Read-only DNS operations."""
from typing import Any
from ..client import CloudflareClient

class DNSService:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def list_zones(self, *, name: str | None = None, page: int = 1, per_page: int = 50) -> dict[str, Any]:
        return self.client.list_zones(name=name, page=page, per_page=per_page)

    def list_records(self, zone_id: str, *, page: int = 1, per_page: int = 100) -> dict[str, Any]:
        return self.client.list_dns_records(zone_id, page=page, per_page=per_page)
