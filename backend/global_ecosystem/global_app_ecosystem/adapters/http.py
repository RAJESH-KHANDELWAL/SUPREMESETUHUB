"""Opt-in HTTPS transport; no provider endpoint is assumed or called implicitly."""
from __future__ import annotations
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from .errors import ProviderRequestError

class HttpsJsonClient:
    def __init__(self, base_url: str, *, timeout: float = 15.0, transport=None):
        normalized = str(base_url).rstrip("/")
        if not normalized.startswith("https://"):
            raise ValueError("base_url must use HTTPS")
        self.base_url = normalized
        self.timeout = timeout
        self._transport = transport or urlopen

    def request(self, method: str, path: str, *, headers=None, body: bytes | None = None) -> bytes:
        if not path.startswith("/") or path.startswith("//"):
            raise ValueError("path must be an absolute API path beginning with one slash")
        request = Request(self.base_url + path, data=body, headers=dict(headers or {}), method=method.upper())
        try:
            with self._transport(request, timeout=self.timeout) as response:
                return response.read()
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            raise ProviderRequestError(f"HTTPS provider request failed: {type(exc).__name__}") from exc

__all__ = ["HttpsJsonClient"]
