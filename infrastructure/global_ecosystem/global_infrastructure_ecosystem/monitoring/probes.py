"""Read-only HTTP(S) endpoint probe helpers for infrastructure monitoring."""
from __future__ import annotations

import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


def check_http_endpoint(url: str, *, timeout: float = 8.0) -> dict[str, Any]:
    """Send a HEAD request and return status metadata without reading a response body."""
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Endpoint must be an absolute http:// or https:// URL.")
    if parsed.username or parsed.password:
        raise ValueError("Credentials must not be embedded in endpoint URLs.")
    if not 0 < timeout <= 60:
        raise ValueError("timeout must be greater than 0 and at most 60 seconds.")

    request = Request(url, method="HEAD", headers={"User-Agent": "SUPREMESETUHUB-HealthCheck/1.0"})
    started = time.monotonic()
    try:
        with urlopen(request, timeout=timeout) as response:
            elapsed_ms = round((time.monotonic() - started) * 1000, 2)
            status_code = int(response.status)
            return {
                "success": 200 <= status_code < 400,
                "status": "HEALTHY" if 200 <= status_code < 400 else "HTTP_ERROR",
                "host": parsed.hostname,
                "path": parsed.path or "/",
                "http_status": status_code,
                "elapsed_ms": elapsed_ms,
                "method": "HEAD",
                "response_body_read": False,
                "mutations_performed": False,
            }
    except HTTPError as exc:
        return {
            "success": False,
            "status": "HTTP_ERROR",
            "host": parsed.hostname,
            "path": parsed.path or "/",
            "http_status": int(exc.code),
            "elapsed_ms": round((time.monotonic() - started) * 1000, 2),
            "method": "HEAD",
            "response_body_read": False,
            "mutations_performed": False,
        }
    except (URLError, TimeoutError, OSError) as exc:
        return {
            "success": False,
            "status": "CONNECTION_ERROR",
            "host": parsed.hostname,
            "path": parsed.path or "/",
            "error_type": type(exc).__name__,
            "elapsed_ms": round((time.monotonic() - started) * 1000, 2),
            "method": "HEAD",
            "response_body_read": False,
            "mutations_performed": False,
        }


__all__ = ["check_http_endpoint"]
