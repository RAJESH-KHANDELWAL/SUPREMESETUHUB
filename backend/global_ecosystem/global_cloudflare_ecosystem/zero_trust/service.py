"""Read-only Cloudflare Zero Trust access application inventory."""
from typing import Any
from ..client import CloudflareClient

class ZeroTrustService:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def list_access_apps(self, account_id: str) -> dict[str, Any]:
        account_id = str(account_id or "").strip()
        if not account_id or "/" in account_id:
            raise ValueError("valid account_id required")
        return self.client._request(f"/accounts/{account_id}/access/apps")
