"""Read-only Cloudflare Pages project inventory."""
from typing import Any
from ..client import CloudflareClient

class PagesService:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def list_projects(self, account_id: str) -> dict[str, Any]:
        account_id = str(account_id or "").strip()
        if not account_id or "/" in account_id:
            raise ValueError("valid account_id required")
        return self.client._request(f"/accounts/{account_id}/pages/projects")
