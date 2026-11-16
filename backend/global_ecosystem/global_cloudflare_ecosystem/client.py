"""Read-only Cloudflare REST adapter. Inject a least-privilege token at runtime."""
from __future__ import annotations
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

_API_BASE="https://api.cloudflare.com/client/v4"
class CloudflareAPIError(RuntimeError):
    """Cloudflare HTTP, transport, or API-level error."""
class CloudflareClient:
    def __init__(self, api_token: str, *, timeout: float=15.0) -> None:
        token=str(api_token or "").strip()
        if not token: raise ValueError("api_token is required")
        if timeout<=0: raise ValueError("timeout must be positive")
        self._api_token=token
        self._timeout=timeout
    def _request(self, path: str, *, query: dict[str,Any]|None=None) -> dict[str,Any]:
        if not path.startswith("/") or ".." in path.split("/"):
            raise ValueError("path must be absolute and cannot contain traversal")
        url=_API_BASE+path
        if query: url+="?"+urlencode(query,doseq=True)
        request=Request(url,headers={"Authorization":f"Bearer {self._api_token}",
                                      "Accept":"application/json",
                                      "User-Agent":"SUPREMESETUHUB-Cloudflare-Adapter/1.0"})
        try:
            with urlopen(request,timeout=self._timeout) as response:
                payload=json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            detail=exc.read().decode("utf-8",errors="replace")[:1000]
            raise CloudflareAPIError(f"Cloudflare HTTP {exc.code}: {detail}") from exc
        except (URLError,TimeoutError,OSError) as exc:
            raise CloudflareAPIError(f"Cloudflare transport failure: {exc}") from exc
        except (UnicodeDecodeError,json.JSONDecodeError) as exc:
            raise CloudflareAPIError("Cloudflare returned invalid JSON") from exc
        if not isinstance(payload,dict) or payload.get("success") is not True:
            errors=payload.get("errors",[]) if isinstance(payload,dict) else []
            raise CloudflareAPIError(f"Cloudflare API reported failure: {errors}")
        return payload
    def list_zones(self, *, name: str|None=None, page: int=1, per_page: int=50) -> dict[str,Any]:
        """List zones visible to the token; permissions determine visibility."""
        if page<1 or not 1<=per_page<=100: raise ValueError("page must be >= 1 and per_page 1..100")
        query:dict[str,Any]={"page":page,"per_page":per_page}
        if name: query["name"]=name.strip()
        return self._request("/zones",query=query)
    def get_zone(self, zone_id: str) -> dict[str,Any]:
        """Fetch a zone by provider zone ID."""
        zone_id=str(zone_id or "").strip()
        if not zone_id or "/" in zone_id: raise ValueError("valid zone_id required")
        return self._request(f"/zones/{zone_id}")
    def list_dns_records(self, zone_id: str, *, page: int=1, per_page: int=100) -> dict[str,Any]:
        """List DNS records; requires appropriate zone DNS read permissions."""
        zone_id=str(zone_id or "").strip()
        if not zone_id or "/" in zone_id: raise ValueError("valid zone_id required")
        if page<1 or not 1<=per_page<=100: raise ValueError("page must be >= 1 and per_page 1..100")
        return self._request(f"/zones/{zone_id}/dns_records",query={"page":page,"per_page":per_page})
__all__=["CloudflareClient","CloudflareAPIError"]
