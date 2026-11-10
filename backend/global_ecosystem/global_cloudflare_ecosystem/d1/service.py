"""Read-only Cloudflare D1 database inventory."""
from typing import Any
from ..client import CloudflareClient

class D1Service:
    def __init__(self, client: CloudflareClient) -> None:
        self.client = client

    def list_databases(self, account_id: str, *, page: int = 1, per_page: int = 100) -> dict[str, Any]:
        account_id = str(account_id or "").strip()
        if not account_id or "/" in account_id:
            raise ValueError("valid account_id required")
        if page < 1 or not 1 <= per_page <= 100:
            raise ValueError("page must be >= 1 and per_page 1..100")
        return self.client._request(f"/accounts/{account_id}/d1/database", query={"page": page, "per_page": per_page})
